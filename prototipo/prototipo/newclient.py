import time
import random
import socket
HOST = 'localhost'
PORT = 5000

conect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

while True:
    time.sleep(1)
    msg=input('')
    msg=f'{msg}'
    conect.sendto(msg.encode(),dest )
    msg= conect.recvfrom(1024)
    print(f'{msg}')
    time.sleep(1)

