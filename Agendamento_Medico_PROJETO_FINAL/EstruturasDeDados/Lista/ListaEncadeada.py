#== == == == lista Exception
class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        #self.__codError=codeError:int
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.
class Node:
    def __init__(self,key:any,carga:any) -> None:
        self.key=key #se fez como necessário uma key para tal
        
        self.carga=carga
        
        self.prox=None

    def __str__(self) -> str:
        return f'key:{self.key}, Carga: {self.carga}'

class NodeLeader:
    def __init__(self) -> None:
        self.start=None
        self.end=None
        self.quantyNodes=0

#== == == == A estrutura de dado lista, ou LIFO.
class Lista:
    def __init__(self):
        self.__NodeLeader=NodeLeader()

#== == == == Método para examinar se a lista está vazia
    def estaVazia(self)->bool:
        return self.__NodeLeader.quantyNodes == 0
    
#== == == == Método para checar o tamanho da lista
    def tamanho(self):
        return self.__NodeLeader.quantyNodes

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->Node:
        try:
            #== == Só funciona se: a lista NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'THE LIST IS EMPTY'
            assert self.tamanho()>=posicao and posicao>0, 'INVALID POSITION'
            
            return self.__elemento(posicao,self.__NodeLeader.start)

        except AssertionError as AE:
            raise ListaException(AE)
    
    def __elemento(self, posicao:int, Node:Node) -> Node:
        if posicao==0: # chegou na posição do Nó 
            return Node
        return self.__elemento(posicao - 1, Node.prox)

#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, key:any)->int: #================================================= PRECISA SER IMPLEMENTADO COM O OBJETIVO DO PROJETO
        try:
            #== == O método só não funciona quando a lista estiver vazia
            assert not self.estaVazia() ,'THE LIST IS EMPTY'
            return self.__busca(key,self.__NodeLeader.start)
                              
        
    
        except AssertionError as AE:
            raise ListaException(AE)
        
        
    def __busca(self, key:any, Node:Node)->Node:
        if Node==None:
            raise ListaException('KEY NOT FOUND')
        
        elif key == Node.key:
            return Node.carga
        
        return self.__busca(key,Node.prox)
        
#== == == == Método que Modificará o contéudo de um nó a partir de uma key exigida.
    def modificar(self, key:any, contentType:any, content: any):
        ''' key: chave, contentType: o que deverá ser alterado, content: a alteração que deverá ser feita'''
        try:
            #== == Só funciona se: a lista NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'THE LIST IS EMPTY'
            
            self.__modificar(key, contentType, content, self.__NodeLeader)
            return f'NODE WITH KEY: {key}, MODIFIED SUCCESSFULLY'
            
        except AssertionError as AE:
            raise ListaException(AE)
    
    def __modifciar(self,key:any, contentType, content:any, Node:Node):
        
        if Node==None:
            raise ListaException('KEY NOT FOUND')
        
        elif Node.key== key:
            Node.carga=content
    
    #== == Adiciona um novo Nó na lista.
    def inserir(self, posicao:int, conteudo:any):
        self.__lista.insert(posicao-1,conteudo) # O final da lista é considerado o topo.
        
    #== == Remove o Ùltimo Nó adicionado na lista.
    def remover(self,posicao)->any:
        try:
            assert not self.estaVazia() ,'A lista está vazia!'
            return self.__lista.pop(posicao) # Remove no final da lista, o topo.
            
        except AssertionError as AE:
            raise ListaException(AE)
        
        except Exception as E:
            raise ListaException(E)

    #== == remover a lista até ela possuir Zero Nós.
    def esvazia(self):
        try:
            return self.__lista.clear()
        except:
            pass
    
    def __str__(self)->str:
        if self.tamanho()==0:
            return 'Empty'
        s = ''
        for i in range(len(self.__lista)):
            s+= f'=|Nó {i+1}: {self.__lista[i]} |= '
        return s + f'\n tamanho: {len(self.__lista)}'
    

