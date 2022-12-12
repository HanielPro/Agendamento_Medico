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
        return f'{self.carga}'

class NodeLeader:
    def __init__(self) -> None:
        self.start=None
        self.end=None
        self.quantyNodes=0
        
#== == == == A estrutura de dado lista, ou LIFO.
class Lista:
    def __init__(self):
        self.__NodeLeader=NodeLeader()
    
    @property
    def NodeLeader(self):
        return self.__NodeLeader.__str__()

#== == == == Método para examinar se a lista está vazia
    def estaVazia(self)->bool:
        return self.__NodeLeader.quantyNodes == 0
    
#== == == == Método para checar o tamanho da lista
    def tamanho(self):
        return self.__NodeLeader.quantyNodes

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->any:
        try:
            #== == Só funciona se: a lista NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'THE LIST IS EMPTY'
            assert self.tamanho()>=posicao and posicao>0, 'INVALID POSITION' 
            
            return self.__elemento(posicao,self.__NodeLeader.start)

        except AssertionError as AE:
            raise ListaException(AE)
    
    def __elemento(self, posicao:int, Node:Node) -> any:
        if posicao==1: # chegou na posição do Nó 
            return Node.carga # retorna o nó na tal posição
        return self.__elemento(posicao - 1, Node.prox) #Quero andar passo por passo, confiando que chegarei no 0

#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, key:any)->int: #== ==  Ele busca a partir de uma chave
        ''' 
        return
            -1: Sem incidências da chaves
            n>0: posição da chave
        '''
        #== == O método só não funciona quando a lista estiver vazia
        if self.__NodeLeader.quantyNodes==0: # caso não haja elementos na lista, retorna um 
            raise  ListaException('EMPTY LIST')
        return self.__busca(key,self.__NodeLeader.start) #Chama a função recursiva
                              
        
    def __busca(self, key:any, Node:Node)->int:
        NodePosition=1
        if Node==None: # Chegou ao final a lista e não achou o Nó
           raise ListaException('KEY NOT FOUND')
        
        elif key == Node.key: # Vê se o nó da vez possui a chave  
            return 1 # Ele achou!
        NodePosition+=self.__busca(key,Node.prox) # Não achou, então vai para o próximo nó
        
        return NodePosition
    
        
#== == == == Método que Modificará o contéudo de um nó a partir de uma key exigida.
    def modificarNode(self, key:any, content: any)->None:
        ''' key: chave, contentType: o que deverá ser alterado, content: a alteração que deverá ser feita'''
        posicao=self.busca(key)
        NodeToChange=self.elemento(posicao)
        NodeToChange.carga=content
        #NodeToChange.carga.ChangeValue(contentName,content) # Implementar dentro da carga do nó este método
            
    #== == Adiciona um novo Nó na lista,dependendo da posição.
    def inserir(self, key:any, conteudo:any,posicao:int=1):
        try:
            assert posicao > 0 and \
                posicao <= self.__NodeLeader.quantyNodes + 1
                
            if(self.autenticarChave(key)):
                raise ListaException('THE KEY IS IN USE')
                
            newNode=Node(key,conteudo)
            
            if self.__NodeLeader.start==None: #adicionando o primeiro nó  da lista    
                
                self.__NodeLeader.start=newNode
                self.__NodeLeader.end= newNode
            
            elif posicao==1: #Adicionando no começo da lista
                
                newNode.prox=self.__NodeLeader.start
                self.__NodeLeader.start=newNode
            
            elif self.__NodeLeader.quantyNodes + 1 == posicao: #Adicionando no final da lista
                
                self.__NodeLeader.end.prox=newNode
                self.__NodeLeader.end=newNode

            else: # Adicionando no meio da lista
                self.__inserir( self.__NodeLeader.start, posicao, newNode)
            
            self.__NodeLeader.quantyNodes+=1

        except AssertionError:
            raise ListaException('INVALID POSITION')
        except Exception as E:
            raise ListaException(E)
    
    def __inserir(self, Node:Node, posicao:int, newNode:Node):

        if posicao-1 == 1: #Ele para antes de chegar na posicação desejada
            newNode.prox= Node.prox
            Node.prox= newNode
            return

        self.__inserir(Node.prox,posicao-1,newNode)
        
    #== == Remove o  Nó  a partir de uma determinada posição
    def remover(self,posicao:int)->any:
        try:
            assert not self.estaVazia() ,'EMPTY LIST'
            assert posicao > 0 and posicao <= self.__NodeLeader.quantyNodes, 'INVALID POSITION'
            NodeRemotion=None
            
            if posicao==1: # caso seja o primeiro nó da lista para ser removido

                NodeRemotion=self.__NodeLeader.start
            
                if self.__NodeLeader.start == self.__NodeLeader.end: #Ele é tanto o primeiro quanto o último
                    self.__NodeLeader.end= None
                    self.__NodeLeader.start=None
                else: # Ele é apenas o primeiro
                    self.__NodeLeader.start= self.__NodeLeader.start.prox

            else:
                NodeRemotion=self.__remover(posicao,self.__NodeLeader.start)
            
            self.__NodeLeader.quantyNodes-=1 #Diminui a quantidade de Nós da lista
            return NodeRemotion.carga #== == Retorna o nó que foi removido
    
        except AssertionError as AE:
            raise ListaException(AE)

    def __remover(self,position:int,Node:Node)->Node:
    
        if position - 1 == 1: # ele deve parar um antes do que será removido    
            NodeToRemove=Node.prox

            if NodeToRemove==self.__NodeLeader.end: #caso seja o final da lista
                Node.prox=None
                self.__NodeLeader.end=Node
                
            Node.prox=NodeToRemove.prox
            return NodeToRemove

        return self.__remover(position-1, Node.prox)

    #== == remover a lista até ela possuir Zero Nós.
    def esvazia(self):
        ArrayNodes=list() #cria um Array vazio
        self.__esvazia(ArrayNodes) # retorna o resultado  da função recurssiva
        return ArrayNodes
         
    def __esvazia(self,array:list)->list[Node]:
        
        if self.__NodeLeader.quantyNodes==0: # caso não haja mais nós para ser excluídos ou a Lista já está vazia
            return array #retorna o array contendo todos.
        
        array.append(self.remover(1)) # o array vai adicionar no final da lista o primeiro nó  
        
        return self.__esvazia(array) # a função se 'chamará' de novo passando o array para adicionar o próximo 'primeiro' nó, caso haja
    
    def __str__(self)->str:
        s=f'Quantidade:{self.__NodeLeader.quantyNodes}\n'
        for i in range(self.__NodeLeader.quantyNodes): #não queria usar uma repetição, mas fiquei com preguiça :(
            s+= f'{i+1}|{self.elemento(i+1)}\n{ "===" * 30 }\n'
        return s
    
    def autenticarChave(self,key)->bool: #Este método percorerá toda a lista a fim de conferir se já existe a chave
        try:
            if self.busca(key):
                return True
        except ListaException:
            return False
    