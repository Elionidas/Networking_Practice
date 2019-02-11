#import stuffs peeps
import sys, socket, select

def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage: python chat_client.py hostname port'
        sys.exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    #try to connect to remote host
    try:
        s.connect((host, port))
    except:
        print 'unable to connect'
        sys.exit()
    
    print 'connected to remote host. You may now send messages'
    sys.stdout.write('[Me] '); sys.stdout.flush()

    while 1:
        socket_list = [sys.stdin, s]

        #Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                #incoming message from the remote server, s
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from the chat server'
                    sys.exit()
                else:
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me ]'); sys.stdout.flush()

#run it
chat_client()