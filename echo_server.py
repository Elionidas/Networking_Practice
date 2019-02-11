#import libraries needed for an echo server
import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    #create tcp socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #enable reuse of the address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #bind socket to port
    server_address = (host, port)
    print "Starting up echo server on port: %s" %server_address
    sock.bind(server_address)
    #listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print "Waiting to receive message from client"
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print "Data: %s" %data
            client.send(data)
            print "sent %s bytes back to %s" %(data, address)
        #close the connection, just like a file
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)