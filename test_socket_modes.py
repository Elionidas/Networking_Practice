#import libraries
import socket

def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print "Trival server launched on socket: %s" %str(socket_address)
    while(1):
        s.listen(1)

#run it
test_socket_modes()