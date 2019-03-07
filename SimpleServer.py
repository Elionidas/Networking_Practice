import socket
#Specify server port and IP (where you want to listen and receive data)
HOST = ''
PORT = 8888
#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind to the socket
s.bind((HOST, PORT))
#Listen for incoming connections (how many to allow pending)
s.listen(1)
# Accept incoming connection and split socket file descriptor and IP/Port tuple
conn, addr = s.accept()
print 'Connected by', addr # Success message

while 1:
    data = conn.recv(1024) # Connection received
    if not data: break # If an error occurs break the loop, close the connection
    str_reverse = data.split() # Split the words into a list, assign assign to a variable
    str_reverse.reverse() # Reverse the words
    data = " ".join(str_reverse) # Join them back together into a string
    conn.sendall(data) # Send back to the client
    print data # Print out reversed string
conn.close() # Close the sockets