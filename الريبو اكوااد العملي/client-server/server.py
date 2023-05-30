import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 7002
s.bind((host, port))
s.listen(5)
client, address = s.accept()
print("connection from ", address[0])

while True:

    received_data = client.recv(2048)
    if received_data.decode("utf-8") == "Q":
        break
    print("client :", received_data.decode('utf-8'))

    send_data = input(" server :")

    if send_data == 'Q':
        break

    client.send(send_data.encode('utf-8'))
s.close()
