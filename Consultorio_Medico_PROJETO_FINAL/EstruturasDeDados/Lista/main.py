import os
import time
from ListaEncadeada import *
#from listaSequencial import *


def MostrarDicionario(dicionario:dict, Chave:str = '0'):

    if dicionario.get(Chave,False)==False:
        print(f'{"-":^5}=> {dicionario["-"]:^5} ')
        return
    print(f'{Chave :^5}=> {dicionario[Chave]:^5} ')
    MostrarDicionario(dicionario, str(int(Chave) +1 ) )
        
opcoesLista={
    '0':'Obter informações da Lista',
    '1':'Inserir Novo Nó',
    '2':'Remover Nó',
    '3':'Verificar se está vazia',
    '4':'Modificar a carga de um Nó',
    '5':'Descobrir a carga de um Nó apartir da posição',
    '6':'Buscar a posição de Um Nó',
    '7':'Obter a quantidade de Nós',
    '8':'Obter informações do Node Leader',
    '9': 'Esvaziar a Lista',
    '-':'Finalizar o programa'
}
opcoesListaChaves= list(opcoesLista.keys())

L1=Lista()
#-- -- Preenchendo sozinho:
for i in range(1,17,3):
    L1.inserir(i, (i*3)//2)
while True:
    try:
        print()
        Posicao=0
        Chave=0
        Carga=''
        print('Escolha uma das seguintes opções: ')
        MostrarDicionario(opcoesLista)
        escolha=input('\n escolha: ')
#== == == == == ==
        if escolha=='-':#== == == Encerra o programa
            break
        escolha=int(escolha)  
        
        if escolha<6 and escolha not in [0,3,4]: #Escolhas que precisam de um informação
            Posicao=int(input('Digite qual a posição desejada para realizar tal operação: '))
        
        if escolha==1 or escolha==4 or escolha==6 : #Escolhas que precisam de uma chave
            Chave= int(input('Digite o valor da chave do Nó: '))
        
        if escolha==0:# Informações da Lista
            print(L1)
        
        elif escolha== 1: # Inserir um Novo nó  
            Carga= int(input('Digite a Carga do nó: '))
            L1.inserir(Chave,Carga,Posicao)
        
        elif escolha==2:#Remove Nó
            print(L1.remover(Posicao))      
        
        elif escolha==3: #Vê se a lista está vazia
            print(L1.estaVazia())
        
        elif escolha==4:#Modificar o Nó
            modificacao=int(input('Digite o valor que desja inserir no Node: '))
            print(L1.modificarNode(Chave,modificacao)) 
        
        elif escolha==5:#Descobre o nó pela posição
            print(L1.elemento(Posicao))
        
        elif escolha==6: #Recebe uma chave, busca a posição de um nó
            print(L1.busca(Chave))
        
        
        elif escolha==7:# Informações da Lista
            print(L1.tamanho())

        elif escolha==8:# Informa o que tem no nó leader
            print(L1.NodeLeader)
       
        elif escolha==9:# Esvaziar a Lista
            print(L1.esvazia())
    
        else:
            raise(Exception('CHOICE NOT FOUND'))
        input()
        os.system('clear')


    except ListaException as LE:
        os.system('clear')
        print(LE)
        time.sleep(2)
    except Exception as E:
        os.system('clear')
        print(E)
        time.sleep(2)