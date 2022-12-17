import time
import random
import socket
HOST = 'localhost'
PORT = 5000

conect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
id=input('id deste cliente')
while True:
    time.sleep(1)
    msg=str(random.randint(1,99))
    print('gerei ',msg)
    msg=f'{msg}|{id}'
    conect.sendto(msg.encode(),dest )
    time.sleep(1)

