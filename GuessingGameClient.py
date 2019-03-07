#Lab5_Client

import socket

HOSTNAME = 'localhost'
PORTNUMBER = 10000
BUFFER = 80

SERVER = (HOSTNAME, PORTNUMBER)
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect(SERVER)

print('client is ready to guess')

while True:
    GUESS = raw_input('Enter a number: ')
    CLIENT.send(GUESS.encode())
    ANSWER = CLIENT.recv(BUFFER)
    print(ANSWER)

    if ANSWER == 'found the number':
        break

CLIENT.close()