import os
import time
from ArvoreBusca import *
#from listaSequencial import *


def MostrarDicionario(dicionario:dict, Chave:str = '0'):

    if dicionario.get(Chave,False)==False:
        print(f'{"-":^5}=> {dicionario["-"]:^5} ')
        return
    print(f'{Chave :^5}=> {dicionario[Chave]:^5} ')
    MostrarDicionario(dicionario, str(int(Chave) +1 ) )
        
def MostrarDicionario(dicionario:dict, Chave:str = '1'):

    if dicionario.get(Chave,False)==False:
        print(f'{"-":^5}=> {dicionario["-"]:^5} ')
        return
    print(f'{Chave :^5}=> {dicionario[Chave]:^5} ')
    MostrarDicionario(dicionario, str(int(Chave) +1 ) )
        

opcoesArvore=[
    'Mostrar o tamanho da árvore',
    'Adicionar Nó raiz',
    'Inserir Nó. ',
    'Remover Nó.',
    'Esvaziar a Árvore',
    'Buscar se existe um Nó.',
    'Mostrar Nós em Pré-Ordem',
    'Mostrar Nós em In-Ordem',
    'Mostrar Nós em Pós-Ordem',
    'Contar a quantidade de nós folhas',
    'Calcular a altura da árvore',
    'Encontrar o nível de um nó ',
    'finalizar o programa',
]
arv=ArvoreBusca()
while True:
    for i in range(len(opcoesArvore)):#achei meio desnecessário
        print('\033[32m'+str(i)+' = '+opcoesArvore[i]+'\033[0;0m')
    cmd=int(input('digite o comendo: '))
    if cmd == 12:
        break
    elif cmd==11:
        pass
    elif cmd==10:
        pass
    elif cmd==9:
        pass
    elif cmd==8:
        print('\033[33m'+'Pós-Ordem'+'\033[0;0m')
        arv.posordem()
    elif cmd==7:
        print('\033[33m'+'In-Ordem'+'\033[0;0m')
        arv.emordem()
    elif cmd==6:
        print('\033[33m'+'Pré-Ordem'+'\033[0;0m')
        arv.preordem()
    elif cmd==5:
        pass
    elif cmd==4:
        pass
    elif cmd==3:
        print('\033[33m'+'Removendo:'+'\033[0;0m')
        key=int(input('número inteiro para a key: '))
        arv.removerNo(key)
    elif cmd==2:
        print('\033[33m'+'Adicionando:'+'\033[0;0m')
        key=int(input('número inteiro para a key: '))
        carga=input('qualquer porcaria para a carga: ')
        arv.InserirNode(key,carga)
    elif cmd==1:
        pass
    elif cmd==0:
        pass
    else:
        print('Comando inválido, seu animal')
'''
while True:
    try:
        print()
        print('Escolha uma das seguintes opções: ')
        MostrarDicionario(opcoesArvore)
        escolha=input('\n escolha: ')
#== == == == == ==        
        if escolha== '1' or escolha== '2' or escolha== '3' or escolha=='10'  or escolha=='11':
            
            origem= str.lower(input('Digite a Origem: (raiz/cursor) '))
            if origem=='raiz':
                origem=1
            elif origem=='cursor':
                origem=2
            else:
                raise(Exception('por favor, escolha: raiz ou cursor '))
            
            if escolha=='1': #== == == Mostra a árvore em pré-ordem
                arv.preordem(origem)
            
            elif escolha=='2':#== == == Mostra a árvore em in-ordem
                arv.emordem(origem)
            
            elif escolha=='3':#== == == Mostra a árvore em pós-ordem
                arv.posordem(origem)
                
            elif escolha=='10' or escolha=='11' : 
                NodeValue= int(input('digite o valor do Nó: '))#-- POR SER NÚMEROS, USEI O INT
                
                if escolha=='10':
                    arv.busca(NodeValue,origem)
                if escolha=='11': #== == == Procura a existência de um nó à partir de uma determinada origem
                    arv.busca(NodeValue,origem)

            
        
        elif escolha=='4': #== == == Mostra o valor da raiz
            print(arv.getRaiz())
            
        elif escolha=='5': #== == == Mostra o valor do cursor
            print(arv.getCursor())
        
        elif escolha=='6': #== == == Move o cursor à sua esquerda
            print(arv.descerEsquerda())
        
        elif escolha=='7': #== == == Move o cursor à sua direita
            print(arv.descerDireita())

#== == == == == ==
        elif escolha=='8' or escolha=='9' or escolha=='12' or escolha=='16' or escolha =='19':
            NodeValue= int(input('digite o valor do Nó: '))#-- POR SER NÚMEROS, USEI O INT
            
            if escolha=='8': #== == == Adiciona um nó à esquerda do cursor
                arv.addFilhoEsquerdo(NodeValue)
                print(f'Nó {NodeValue} adicionado a esquerda!')
            
            elif escolha=='9': #== == == Adiciona um nó à direita do cursor
                arv.addFilhoDireito(NodeValue)
                print(f'Nó {NodeValue} adicionado a direita!')
                
            elif escolha=='12': #== == == Move o cursor para um determinado nó
                arv.go(NodeValue)
                print(f'Cursor movido para o Nó {NodeValue}!')
                    
            elif escolha=='16':#== == == Adiciona uma raiz
                arv.adicionarRaiz(NodeValue)
                print('Raiz criada com sucesso!')
            
            elif escolha=='19': #== == == Descobre o nível de um Nó
                nivel=arv.getLevel(NodeValue)
                print(f'o Nó com a chave: {NodeValue}, se encontra no nível: {nivel}')
        elif escolha=='13': #== == ==Esvazia a árvore
            print(arv.esvazia())
        
        elif escolha=='14':#== == == Mostra a quantidade de Nós
            print('Quantidade de nós até agora: ', arv.__len__())
        
        elif escolha=='15':#== == == Reseta o cursor
           arv.resetCursor()
           print('cursor movido para a raiz, com sucesso!')
        
        elif escolha=='17':#== == == Reseta o cursor
            print('Quantidade de nós folhas: ',arv.leafs())
                
        elif escolha=='18':#== == == Reseta o cursor
            print('Altura: ',arv.profundidade())        #=======ERRRO! CONTANDO A MAIOR QUANTIDADE DE NÒS


        elif escolha=='-':#== == == Encerra o programa
            break
        else:
            raise(Exception('CHOICE NOT FOUND'))
        input()
        os.system('clear')

    except NodeException as NE:
        os.system('clear')
        print(NE)
        time.sleep(2)

    except BinaryArborException as BAE:
        os.system('clear')
        print(BAE)
        time.sleep(2)
    except Exception as E:
        os.system('clear')
        print(E)
        time.sleep(2)
'''