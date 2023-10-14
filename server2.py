import socket

# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_ip = '192.168.1.55'  
port = 65501

# bind the server socket to the IP address and port number
server_socket.bind((server_ip, port))

# allow only client for the server
server_socket.listen(1)

# accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to client: {client_address}")

# keep the connection open until receiving "Close Connection" from client
while True:
    # receive message from the client
    message = client_socket.recv(1024).decode()
    print("Received message:", message)

    # check if the client wants to close the connection
    if message.lower() == "close connection":
        break

    # capitalize the message
    capitalized_message = message.upper()

    # send the capitalized message back to the client
    client_socket.send(capitalized_message.encode())

# close the client socket
client_socket.close()

# close the server socket
server_socket.close()
