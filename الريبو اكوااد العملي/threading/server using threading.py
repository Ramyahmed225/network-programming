
import socket
import threading



def send_thread(c) : 
    while True : 
        y=input('server : ' )
        c.send(y.encode('utf-8'))
    
# Function to handle client connections
def handle_client(c):
    
    send=threading.Thread(target=send_thread,args=(c,))
    send.start()
    
    while True:
        # Receive data from the client
        x= c.recv(1024).decode('utf-8')
        if not x:
            break
        print("client :", x)
        
        # Echo the received message back to the client
        c.send( "client :",x.encode('utf-8'))
    
    # Close the client connection
    c.close()

# Create a socket object
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host='127.0.0.1'
port=7000
s.bind((host,port))



# Listen for incoming connections
s.listen(5)


while True:
    # Accept a client connection
    c,add = s.accept()
    print("Accepted connection from:", add[0])
    
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(c,))
    client_thread.start()
    

