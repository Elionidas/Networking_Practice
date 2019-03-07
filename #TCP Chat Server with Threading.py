#TCP Chat Server with Threading

import socket, threading

def accept_client():
    while True:
        #accept new connection, add them to the connection list, create a new thread, and start broadcast thread.
        client_sock, client_add = serv_sock.accept()
        CONNECTION_LIST.append(client_sock)
        thread_client = threading.Thread(target = broadcast_usr, args=[client_sock])
        thread_client.start()

def broadcast_usr(client_sock):
    while True:
        try:
            data = client_sock.recv(1024) #Receive new data from client(s)
            if data:
               b_usr(client_sock, data)
        except Exception as x: #error occurred
            print(x.message)
            break

def b_usr(cs_sock, msg):
    #Check the connection list and only send to clients that are not the source of the data.
    for client in CONNECTION_LIST:
        if client != cs_sock:
            client.send(msg)

if __name__ == "__main__":
    CONNECTION_LIST = []

    # socket
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind
    HOST = 'localhost'
    PORT = 5555
    serv_sock.bind((HOST, PORT))

    # listen
    serv_sock.listen(10)
    print('Chat server started on port: ' + str(PORT))
    #Accept connection and create a new thread
    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()