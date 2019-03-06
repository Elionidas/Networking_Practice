#redefine as NetworkServer.py
import socket
import struct

#IPAddress = 10.128.102.165
serverPort = 1337

#bind the socket to the server
s = socket.socket(AF_INET, SOCK_STREAM)
serversocket.bind(())
#setup to receive the message
s.listen()
s.accept()
data = ''
s.recv(data)
message = struct.unpack(data)
#print out the message to reveal its contents
print message
s.send(data)
s.close()
