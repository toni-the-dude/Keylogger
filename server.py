# import pynput
import socket
import pickle

# from pynput.keyboard import Key, Listener

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
print("Server socket:{0}:{1}".format(server_address[0], server_address[1]))

server_socket.bind(server_address)

server_socket.listen(1)
print("Listening...")


try:
    client_socket, client_address = server_socket.accept()
    print("Outbound connection received.")
    print("Client socket:{0}:{1}".format(client_socket, client_address))

    while True:
        received_data = pickle.loads(client_socket.recv(1024))
        print("Received data:{0}".format(received_data))
finally:
    server_socket.close()