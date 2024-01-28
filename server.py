# import pynput
import socket

# from pynput.keyboard import Key, Listener

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

server_socket.bind(server_address)

server_socket.listen(1)

client_socket, client_address = server_socket.accept()

server_socket.close()