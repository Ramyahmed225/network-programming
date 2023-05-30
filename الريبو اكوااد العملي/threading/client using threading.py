import socket
import threading


def receive_thread(s):
    while True:
        # Receive the echoed message from the server
        data = s.recv(1024).decode('utf-8')
        print("Received server message:", data)

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host = '127.0.0.1'
port = 7000

# Connect to the server
s.connect((host, port))

# Start the receive thread
receive = threading.Thread(target=receive_thread, args=(s,))
receive.start()

while True:
    # Send a message to the server
    message = input("client: Enter message (type 'exit' to quit): ")
    s.send(message.encode('utf-8'))

    if message == 'exit':
        break

# Close the client socket
s.close()
