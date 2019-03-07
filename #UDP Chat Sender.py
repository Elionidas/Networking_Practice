#UDP Chat Sender

import socket
import struct

UDP_IP = "FF02::A:C:7:9"
PORT = 5005
TTL = 5

ttl_bin = struct.pack('@I', TTL)

# Socket Creation
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
# Setting Multicast options
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl_bin)
sock.settimeout(50)

"""Does not work in VM due to IPv6.
Will not loop back to message prompt,
because it will wait for a response
from multicast group."""
while True:
	MESSAGE = raw_input(">")
	if MESSAGE == "exit": sock.close()

	try:
	    sock.sendto(MESSAGE, (UDP_IP, PORT))
	    data, server = sock.recvfrom(1024)
	    ip, port, a, b = server

	    print '[%s]: "%s"' % (ip, data)

	except socket.timeout: break