import socket


# Creates the socket, makes the connection, and sends the GET request
sock_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_1.connect(("192.168.0.12", 80))
sock_1.send("GET /index.html HTTP/1.0\r\n\r\n")

sock_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_2.connect(("192.168.0.12", 80))
sock_2.send("GET /images/pic.jpg HTTP/1.0\r\n\r\n")


# Opens the file for writing
file1 = open ("index.html", "w")
file2 = open ("pic.jpg", "w")


# Buffer to receive the complete file
recv_1 = ''
recv_2 = ''


# Loops through the receive buffer until the end of the file
while True:
    result_1 = sock_1.recv(1024)
    recv_1 += result_1
    if not result_1: break

while True:
    result_2 = sock_2.recv(1024)
    recv_2 += result_2
    if not result_2: break


# Splits the data from the header
result_s_1 = recv_1.split("\r\n\r\n")
result_s_2 = recv_2.split("\r\n\r\n")


# Writes the file to disk
file1.write(result_s_1[1])
file2.write(result_s_2[1])


# Close the files
file1.close()
file2.close()


# Closes the sockets
sock_1.close()
sock_2.close()