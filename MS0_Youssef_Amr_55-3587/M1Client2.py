import socket

def start_client():
    server_address = ('172.20.10.3', 55555)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    while True:
        # Prompt user for a message
        message = input("Enter a message: ")
        
        # Send message to server
        client_socket.send(message.encode())

        # Check if client wants to close the connection
        if message == 'CLOSE SOCKET':
            client_socket.close()
            break

        # Receive response from server
        response = client_socket.recv(1024).decode()
        print("Response from server:", response)

start_client()
