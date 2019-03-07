#redefine as NetworkServer.py
from socket import *
from struct import *

#IPAddress = 10.128.102.165
serverPort = 1337

#bind the socket to the server
s = socket(AF_INET, SOCK_STREAM)
#then set it to reuse the address for multiple connections to this server
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#for a sever we bind it
s.bind(("", serverPort))
#listen for one connection
s.listen(1)
#take the connection and seperate the message into data/IPaddress
c, a = s.accept()
#grab our data
data = c.recv(1024)

#this simply unpacks the data given by the client server, 
#which was packed when it was sent in big endian format
print struct.unpack('>iiiiii', data)