from ListaSimplesmenteEncadeada import *

l1 = Lista()
print(l1)
print('Tamanho: ', len(l1))


l1.inserir(1,20)
l1.inserir(2,30)
l1.inserir(1,40)
print(l1)
print('Tamanho: ', len(l1))


while(not l1.estaVazia()):
    print(l1.remover(1))
