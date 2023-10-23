import socket
import threading

PORT = 55555
ADDR = ('172.20.10.3', PORT)

# Define a data structure to store client information
clients = []

# Function to handle individual client connections
def handle_client(conn, addr):
    print("[NEW CONNECTION] " + str(addr) + " connected.")
    
    while True:
        # Receive client message
        data = conn.recv(1024).decode()
        
        # Check if the client wants to close the connection
        if "CLOSE SOCKET" in data:
            conn.close()
            clients.remove(conn)
            print(f"[CONNECTION CLOSED] {addr}")
            break
        
        # Capitalize the received message
        capitalized_msg = data.upper()
        
        # Send the capitalized message back to the client
        conn.send(capitalized_msg.encode())

# Main server function
def main():
    print("Server is starting...")
    
    # Create server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server socket to an address
    server.bind(ADDR)
    
    while True:
        # Listen for incoming connections
        server.listen()
        conn, addr = server.accept()
        
        # Store client information
        clients.append(conn)
        
        # Start a new thread to handle the client
        threading.Thread(target=handle_client, args=(conn, addr)).start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()