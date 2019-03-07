#TCP_Echo_Server

import socket, struct

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket
s.bind((HOST, PORT)) # Bind IP and port
s.listen(1) # Listen for new connections
conn, addr = s.accept() # Accept new connection
print 'Connected: ', addr # Print success message

while 1:
    packed_2 = conn.recv(4024) # Receive data
    if not packed_2: break # If error, break connection
    a, b, c, d, e, f = struct.unpack('!ii2cii', packed_2) # Unpack and split into separate variables

    # Print out unpacked values
    print a
    print b
    print c
    print d
    print e
    print f
    print
    #Convert values for retransmission
    a2 = hex(a)
    b2 = hex(b)
    e2 = hex(e)
    f2 = hex(f)
    f3 = bin(f)
    #Join them together in one string
    x = ", "
    seq = (a2, b2, c, d, e2, f3)
    data2 = x.join(seq)
    print data2

    conn.sendall(data2) # Send values back to client
    # Print converted values
    print
    print a2
    print b2
    print c
    print d
    print e2
    print f3

conn.close() # Close connection