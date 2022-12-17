import time
import threading
import random
from threading import Thread
import socket


HOST = 'localhost'
PORT = 5000
conect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conect.bind((HOST, PORT))

c=threading.Semaphore(1)

class CPU:

    def __init__(self):
        self.quant=0
        self.lista=list()
    

    def adicionar(self,id):
        self.lista.append(Nucleo(id))
        self.quant+=1

    def __str__(self):
        s=''
        for i in range(self.quant):
            print(self.lista[i])
            s+=str(self.lista[i])
        return s
    def timeToWork(self):

        for i in range(self.quant):
            print(self.lista[i])
            l=threading.Thread(target=self.lista[i].start())
            l.start()
            print('chega')

class Storage:

    def __init__(self,size):
        self.size=size
        self.lista=list()
        self.ocupados=0

    def add(self,new):#Não levar em conta
        self.lista.append(new)
        print(self.lista)
        self.ocupados+=1 

    def remove(self):#Não levar em conta
        aux=self.lista[0]
        self.lista=self.lista[1::]
        self.ocupados-=1
        return aux
    
    def armazenar(self,new):
        c.acquire()
        self.critical(1,new)
        time.sleep(0.2)
        c.release()
        time.sleep(0.1)

    
    def critical(self,flag,new=0):
        if flag==1:
            if self.ocupados==self.size:
                return False
            else:
                num=random.randint(1,99)
                self.add(new)
                return True
            
        elif flag==0:
            if self.ocupados==0:
                return 'nothing to do'
            else:
                return self.remove()


    def plot(self):
        x=threading.Thread(target=self.produce)
        x.start()
    
    def produce(self):#serviu apenas para teste, pois ela gera automaticamente numeros
        while True:
            c.acquire()
            self.critical(1)
            time.sleep(0.3)
            c.release()
            time.sleep(0.2)
            

class Nucleo:

    def __init__(self,id):
        self.id=id
        print('Nucleo criado')

    def __str__(self):
        return f'|Nucleo {self.id}|'

    def start(self):
        t=threading.Thread(target=self.process)
        t.start()
    
    def process (self):
        while True:
            c.acquire()
            x=storage.critical(0)
            print({self.id},'Objeto ',x,' Removido')
            time.sleep(0.2)
            c.release()
            time.sleep(0.4)

def servidor():
    while True:
        msg, cliente = conect.recvfrom(1024)
        msg=msg.decode().split('|')
        print(msg[1],'enviou',msg[0])
        st=threading.Thread(target=storage.armazenar(msg[0]))
        st.start()

cpu=CPU()

num=int(input('numero de nucleos: '))
y=int(input('tamanho máximo da memória: '))
storage=Storage(y)
#irá gerar os nucleos do processador
for i in range(1,num+1):
    cpu.adicionar(i)
cp=threading.Thread(target=cpu.timeToWork())
#st=threading.Thread(target=storage.produce())#ignore
cp.start()
tr=threading.Thread(target=servidor)
tr.start()
#st.start()