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
        

opcoesArvore={
    '0':'Mostrar o tamanho da árvore',
    '1': 'Adicionar Nó raiz',
    '2':'Inserir Nó. ',
    '3':'Remover Nó.',
    '4':'Esvaziar a Árvore',
    '5':'Buscar se existe um Nó.',
    '6':'Mostrar Nós em Pré-Ordem',
    '7':'Mostrar Nós em In-Ordem',
    '8':'Mostrar Nós em Pós-Ordem',
    '9': 'Contar a quantidade de nós folhas',
    '10': 'Calcular a altura da árvore',
    '11': 'Encontrar o nível de um nó ',
    '-':'finalizar o programa',
}

opcoesArvoreChaves= list(opcoesArvore.keys())
arv=ArvoreBusca()
#== == Árvore já preenchida:
arv.InserirNode(20,'por seus')
arv.InserirNode(11,'ele')
arv.InserirNode(22,'pobre')
arv.InserirNode(13,'te')
arv.InserirNode(15,'encontrará')
arv.InserirNode(19,'pagará')
arv.InserirNode(40,'lazarento')
arv.InserirNode(23,'homem')
arv.InserirNode(10,'dia')
arv.InserirNode(5,'Um')
arv.InserirNode(21,'pecados')
arv.InserirNode(12,'virá e')
arv.InserirNode(18,'você')
#arv.emordem()

print('==========================')
print('nó removido',arv.removerNo(20))
print(arv)
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