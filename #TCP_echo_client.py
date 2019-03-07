#TCP_echo_client

import socket, struct

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
s.connect((HOST, PORT)) #initiate connection

# Pack values in Network byte order, specify format for each
packed_2 = struct.pack('!ii2cii', 12345, 56789, '&', '*', 0x7d0, 0b11111010000)
s.sendall(packed_2) # Send packed struct

data = s.recv(4024) # Receive data back from server
print data # Print results

a, b, c, d, e, f = data.split(", ") # Split the values into separate variables

# Convert 0x3039 and 0xddd5 back into decimal integers
a2 = int(a, 16)
b2 = int(b, 16)

# Print all values in original form
print
print a2
print b2
print c
print d
print e
print f

s.close() # Close socket