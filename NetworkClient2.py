import socket 
import struct 

#IPAddress = 10.128.102.165
accept_port_1 = 12345 
accept_port_2 = 54321 

serverPort = 1337 

cmd_list = {
		'success'	:	0x800,
		'error'		:	0x801,
		'query_mode':	0x802,
		'get_key'	:	0x803,
}

padding = 0x0000 

c = socket.socket()
serversocket.bind(())
c.connect(('10.128.102.165',serverPort))
message = struct.pack('ll', 0x802, padding)
c.send((message))
data = s.recv(1024)
c.close() 
#r = socket.socket() 
#r.connect(('10.128.102.165',serverPort))
#r.send('0x803')
#r.send(data)
#serverReturn = r.recv(1024)
#r.close()

print('Received:', data)
#print('Returned', repr(serverReturn))