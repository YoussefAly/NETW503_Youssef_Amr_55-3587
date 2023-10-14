import socket

# initiate Client socket with a TCP connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_ip = '192.168.1.55'
port = 65501

# connect to the server
client_socket.connect((server_ip, port))

# open a connection until sending "Close Connection"
while True:
    message = input("Enter your message: ")

    # send the message to the server
    client_socket.sendall(message.encode())

    # check if the client wants to close the connection
    if message.lower() == "close connection":
        break

    # receive response from the server
    response = client_socket.recv(1024).decode()
    print("Server response:", response)

# close the client socket
client_socket.close()