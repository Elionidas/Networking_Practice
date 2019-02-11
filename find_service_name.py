#first off import socket
import socket

#define your function
def find_service_name():
    #claiming our first protocol can be a variable, in this case TCP
    protocolname = 'tcp'
    for port in [80, 25]:
        print "Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))
    print "Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))

find_service_name()