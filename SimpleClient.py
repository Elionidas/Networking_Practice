import socket
#Specify server IP and Port (where data is being transmitted)
HOST = 'localhost'
PORT = 8888
#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Initiate a connection
s.connect((HOST, PORT))
#Send data
s.sendall('Hello my name is World')
#Receive data (buffer)
data = s.recv(1024)
#Close the socket
s.close()
#Print the results
print 'Received', repr(data)
