#UDP Chat receiver

import socket
import struct

UDP_IP = "FF02::A:C:7:9"
UDP_PORT = 5005
# Socket Creation
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT))
# Setting Multicast options
group_bin = socket.inet_pton(socket.AF_INET6, UDP_IP)
group = group_bin + struct.pack('@I', 0)
# Host needs to join multicast group to send messages
# to everyone in group (everyone with multicast socket options set).
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, group)

while True:
    data, addr = sock.recvfrom(1024)
    ip, port, a, b = addr
    print '[%s]: "%s"' % (ip, data)