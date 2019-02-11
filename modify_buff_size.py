#import time
import socket

#now some macros
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

#define function
def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #get the size of the socket's end buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [Before]:%d" %bufsize

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [After]:%d" %bufsize

#run the program
modify_buff_size()