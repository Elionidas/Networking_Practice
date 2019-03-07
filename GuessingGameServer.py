#Lab5_Server

from random import randint
import socket

HOSTNAME = ''
PORTNUMBER = 10000
BUFFER = 80

SERVER_ADDRESS = (HOSTNAME, PORTNUMBER)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(SERVER_ADDRESS)
SERVER.listen(1)

print('server waits for client to connect')
CLIENT, CLIENT_ADDRESS = SERVER.accept()
#print('server accepted connection request from %d', % CLIENT_ADDRESS)

SECRET = randint(0, 100)
print('The number is %d' % SECRET)

while True:
    print('server waits for a guess')
    GUESS = CLIENT.recv(BUFFER).decode()
    print('server received ' + GUESS)

    if int(GUESS) < SECRET:
        REPLY = 'too low'
    elif int(GUESS) > SECRET:
        REPLY = 'too high'
    else:
        REPLY = 'found the number'
    CLIENT.send(REPLY)

    if REPLY =='found the number':
        break

SERVER.close()