#import needed libraries
import socket
import os
import threading
import SocketServer

#define needed variables outside the functions
SERVER_HOST = 'localhost'
SERVER_PORT = 0 #tells kernel to pick up a port dynamically (any port it can get its hands on)
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class Forked_Client():
    """A client to test the forking server"""
    def __init__(self, ip, port):
        #create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect to server
        self.sock.connect((ip, port))
    
    def run(self):
        """Client playing with server"""
        #send data to server
        current_process_id = os.getpid()
        print 'PID %s Sending echo message to the server : "%s"' %(current_process_id, ECHO_MSG)
        sent_data_length = self.sock.send(ECHO_MSG)
        print "Sent: %d characters, so far..." %sent_data_length

        #display server response
        response = self.sock.recv(BUF_SIZE)
        print "PID %s received: %s" % (current_process_id, response[5:])

    def shutdown(self):
        """Cleanup the client socket"""
        self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        #send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s : %s' % (current_process_id, data)
        print "Server sending response [current_process_id, data] = %s" %response
        self.request.send(response)
        return

class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    """nothing to add here, as it inherits everythinig it needed from its parent classes"""
    pass

def main():
    #launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address #retrieve the port number
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True) #dont hang on exit
    server_thread.start()
    print 'server loop running PID: %s' %os.getpid()

    #launch the client
    client1 = Forked_Client(ip, port)
    client1.run()
    client2 = Forked_Client(ip, port)
    client2.run()

    #clean em up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()

if __name__ == '__main__':
    main()