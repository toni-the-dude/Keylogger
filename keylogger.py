import os

pid = os.fork()

print(pid)

while True:
    x = input()
    print(pid)
    
    