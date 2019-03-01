#lets import needed libraries
import select
import sys
import socket
import signal
import cPickle
import struct
import argparse

#time to set the server parameters
SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'

#lets set up some utilities next
def send(channel, *args):
    buffer = cPickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)

def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size) [0])
    except struct.error, e:
        return ''
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size-len(buf))
    return cPickle.loads(buf)[0]

class ChatServer(object):
    """ An example chat server using select """
    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #make sure we can reusing socket addresses
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print 'Server listening to port: %s...' %port
        self.server.listen(backlog)
        #Catch keyboard interuppts
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        """ Clean up client outputs """
        #close the server
        print 'Shutting down server...'
        #close existing client sockets
        for output in self.outputs:
            output.close()
        self.server.close()

    def get_client_name(self, client):
        """ Return the name of the client """
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True
        while running:
            try:
                readable, writeable, exceptional = select.select(inputs, self.outputs, [])
            except select.error, e:
                break
            for sock in readable:
                if sock == self.server:
                    #handle the server socket
                    client, address = self.server.accept()
                    print "Chat server: got connection %d from %s" %(client.fileno(), address)
                    #read the login name
                    cname = receive(client).split('NAME: ')[1]
                    #compute client name and send back
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)
                    #sending joining information to other clients
                    msg = "\n(Connected: New client (%d) from %s" %(self.clients, self.get_client_name(client))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client)
                elif sock == sys.stdin:
                    #handle standard input
                    junk = sys.stdin.readline()
                    running = False
                else:
                    #handle all other sockets
                    try:
                        data = receive(sock)
                        if data:
                            #send as new clients message
                            msg = '\n#[' + self.get_client_name(sock) + ']>>' + data
                            #send data to all except ourself
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                        else:
                            print "Chat server: %d hung up" % sock.fileno()
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)
                            #sending client leaving info to others
                            msg = "\n(Now hung up: Client from %s)" %self.get_client_name(sock)
                            for output in self.outputs:
                                send(output, msg)
                    except socket.error, e:
                        #remove
                        inputs.remove(sock)
                        self.outputs.remove(sock)
            self.server.close()

class Chatclient(object):
    """ a command line chat client using select """

    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.Connected = False
        self.host = host
        self.port = port
        #initial prompt
        self.prompt='[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        #connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connected = True
            #send my name
            send(self.sock,'NAME: ' + self.name )
            data = receive(self.sock)
            #contains client addresses, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except socket.error, e:
            print "Failed to connect to chat server @ port %d" % self.port
            sys.exit(1)

    def run(self):
        """ chat client main loop """
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                #wait for input from stdin and socket
                readable, writeable, exceptional = select.select([0, self.sock], [], [])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print 'Client shutting down.'
                            self.connected = False
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print " Client interuppted. """
                self.sock.close()
                break