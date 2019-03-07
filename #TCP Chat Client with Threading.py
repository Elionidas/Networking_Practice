#TCP Chat Client with Threading

import socket, threading

def send(uname): #Send function
    while True:
        msg = raw_input('') #take incoming text, format for chat, send it to server.
        data = uname + ':  ' + msg
        client_sock.send(data)

def receive(): #Receive function
    while True:
        data = client_sock.recv(1024) #Receive incoming data, format and print to chat.
        print('\n'+ str(data))

if __name__ == "__main__":
    # Create socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to information:
    HOST = 'localhost'
    PORT = 5555

    uname = raw_input('Enter your username > ') #Prompt for client username

    client_sock.connect((HOST, PORT)) #Initiate a connection to the server.
    print('Connected to remote host...') #Success

    #Start thread for send function and specify argument
    thread_send = threading.Thread(target=send, args=[uname])
    thread_send.start()
    #Start thread for receive function
    thread_receive = threading.Thread(target=receive)
    thread_receive.start()