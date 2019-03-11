#step 1: import your libraries
import socket

#step 2: create the beginning of a server
def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 9000))
    s.listen()
    s.accept()
    data = ''
    s.recv(data)
    s.close()

def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((9000))
    data = "Wasssup"
    c.send(data)
    c.recv(data)
    c.close()