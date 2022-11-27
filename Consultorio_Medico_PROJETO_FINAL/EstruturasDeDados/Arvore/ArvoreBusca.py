

#== == == ==Criador da Exceções da Árvore binário
class SearchArborException(Exception):
        #-- -- Codes Error
        # 1, The arbor is empty
    def __init__(self, code, msg) -> None:
        super().__init__(f'Binary Arbor Exception {code}: ', msg)

#== == == ==Criador da Exceções dos Nós

class NodeException(Exception):
    #-- -- Codes Error
        # 1, key in use, use another key
        # 2, key not found, insert this key first.
    def __init__(self, code, msg) -> None:
        super().__init__(f'Node Exception {code}: ', msg)         

#== == == ==Aqui onde os nós são criados
class Node:
    def __init__(self,key:any, carga:any):
        self.__key=key
        self.carga = carga
        self.esq = None
        self.dir = None
    
    @property    
    def key(self):
        return self.__key
    def __str__(self):
        return f'key:{self.__key}| carga: {str(self.carga)}'
    
#== == == ==Classe que contém todos os métodos aárvore binária
class ArvoreBusca:
    #== == == Método que cria a raiz               
    def __init__(self, carga_da_raiz=None):
        self.__raiz=Node(carga_da_raiz) if carga_da_raiz  !=  None else carga_da_raiz#== == Caso não seja declarado um nó raiz, a árvore existirá, porém vazia.

    ''' Exemplo de árvore binária co busca
                    20
                11        24
             5         21     49
          3    8          23
    '''
    @property
    def raiz(self):
        return self.__raiz
    
    #== == == Método que confere se a raiz está vazia            
    def estaVazia(self)->bool:
        if self.__raiz==None: return True
        else: return False
    
    #== == == Retorna o Nó raiz, caso ele exista            
    def getRaiz(self)->any:
        try:
            assert self.__raiz  !=  None 
            return self.__raiz
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')
    
    #== == == Retorna os elementos em préordem
     
    def preordem(self):
        try:
            assert not(self.estaVazia())
            self.__preordem(self.__raiz)
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')
    
    def __preordem(self, no:Node):
        if no==None:
            return
        print(no, end='=+=\n')
        self.__preordem(no.esq)
        self.__preordem(no.dir)
        
    #== == == Retorna os elementos em in-ordem
  
    def emordem(self):
        try:
            assert not(self.estaVazia())
            self.__emordem(self.__raiz)
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')


    def __emordem(self, no:Node):
        if no==None:
            return
        self.__emordem(no.esq)
        print(no, end='=+=\n')
        self.__emordem(no.dir)
        
    #== == == Retorna os elementos em pós-ordem 
    def posordem(self):
        try:
            assert not(self.estaVazia())
            self.__posordem(self.__raiz)
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')

    def __posordem(self, no:Node):
        if no==None:
            return
        self.__posordem(no.dir)
        self.__posordem(no.esq)
        print(no, end='=+=\n')
        

#== == == INSERIR NÒ
    '''
        A parte crucial de uma Árvore binária de busca, 
        Ela deverá inserir um nó a direita caso NewNodeKey > NodeKey 
        Ou a esquerda caso o NewNodeKey < NodeKey
        Não deverá ser permitido este caso: NewNodeKey == NodeKey      
    '''
    
    def InserirNode(self,key:any,carga:any):
        newNode=Node(key,carga)
        if self.__raiz==None:
            self.__raiz=newNode
            return
        self.__InserirNode(self.__raiz,newNode)

    def __InserirNode(self,Node:Node,newNode:Node):
        
        if newNode.key==Node.key: #== A key já foi usada na árvore:
            raise NodeException(1,'AUTHENTICATION KEY ERROR')
        
        elif newNode.key > Node.key: # caso a key do Nó seja maior que a key do Nó atual
            if Node.dir==None: # Não há sub-árvores a direita do nó
                Node.dir=newNode
                return # encerra a recursão
            
            else: #Caso haja algum(uns) nó(s) a direita, terá a tentativa de inserir o nó lá
                self.__InserirNode(Node.dir,newNode)
        
        elif newNode.key < Node.key: # caso a key do Nó a ser criado seja menor que a key do Nó atual
            if Node.esq==None: # Não há sub-árvores a esquerda do nó
                Node.esq=newNode
            else:#Caso haja algum(uns) nó(s) a esquerda, terá a tentativa de inserir o nó lá
                self.__InserirNode(Node.esq,newNode)
                return # encerra a recursão
            
    #== == == Retorna a quantiade de Nós
        
    def __len__(self):
        return self.__count(self.__raiz)
    
    def __count(self, no:Node)->int:
        if no==None:
            return 0 #== == Chegou ao fim.
        
        quantidadeNo= 1 +self.__count(no.esq) # quantidade nó é criado e é somado com a quantiade de nós a sua  do nó a esquerda
        quantidadeNo+= self.__count(no.dir) # quando não há nós a esquerda, ele tentará a sua direita.
        return quantidadeNo #finalizado, ele retornará a soma.

    #Procura a existência de um Nó
    def busca(self, key:any)->bool:
        try:
            assert not(self.estaVazia())
            self.__busca(key,self.__raiz)
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')
    
    #== == == == procura se existe um determinado. se orientando pelo cursor
    def __busca(self, key:any, node:Node) ->bool:
        
        if node==None: # chegou ao final da sub-árvore
            return False
        
        elif node.key==key: #testa se esta é a chave 
            return True 
        
        elif key < node.key:  #testa se a chave está a esquerda do nó
            return self.__busca(key, node.esq)
        
        elif key < node.key:  #se a chave não está a esquerda, então testa se está a direita
            return self.__busca(key, node.esq)
    
    #== == == Método para remover Nós em uma árvore de busca
    '''
    Este método precisa ser corrigido
     |||||||||||||||||||
     |||||||||||||||||||
     |||||||||||||||||||
   \|||||||||||||||||||||/
    \|||||||||||||||||||/
      \|||||||||||||||/               
         \||||||||||/
           \||||||/
             \||/
    '''
    def removerNo(self,key:any)->Node:
        try:
            '''
            # 1º caso: O Node é um nó folha
            # 2º caso: O Node possui um Nó ou a direita ou a esquerda 
            # 3º caso: O Node possui uma sub-árvore
            # 4º caso: O Node é a raiz
            # o 4º é o que precisa de mais atenção pois a raiz não pode ser removida com um método convencional.
            '''
            assert not(self.estaVazia())
            if key == self.__raiz.key: # testa se é o 4° caso
                nodeRemoved=self.__raiz
                if nodeRemoved.esq != None and nodeRemoved.dir != None: # testa se há nós a esquerda e a direita da raiz.
                
                    NodeChanged=self.__changeNode(nodeRemoved.dir)
                    NodeChanged.esq= nodeRemoved.esq
                    NodeChanged.dir=nodeRemoved.dir
                    self.__raiz=NodeChanged
                    
                elif nodeRemoved.esq != None: self.__raiz= nodeRemoved.esq #Caso haja apenas um Node a esquerda 
                elif nodeRemoved.dir != None: self.__raiz= nodeRemoved.dir #Caso haja apenas um Node a direita
            
            else:    
                nodeRemoved= self.__removerNo(key,self.__raiz)
            return nodeRemoved
   
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')
    
    #== == método que faz toda a chama recurssiva
    def __removerNo(self,key:any,node:Node)->Node:
        
        #-- -- Caso tenha achado o nó:
        if node.esq != None or node.dir != None: #checa se é possível dirigir-se para a direita ou para a esquerda
            
            if key<node.key: #checa se a chave é menor
                nextNode=node.esq # o nó para testar será a esquerda deste
                
                if key==nextNode.key: # depois checa se o nó a esquerda é o procurado
                    
                    if nextNode.dir != None and nextNode.esq != None: # checa se ele é o 3º caso
                        node.esq=self.__changeNode(nextNode.dir) 
                    
                    elif nextNode.esq != None: node.esq= nextNode.esq # checa se ele é 2º caso esquerda
                    elif nextNode.dir != None: node.esq= nextNode.dir # checa se ele é 2º caso direita
                    
                    return nextNode #caso seja o nó procurado será retornado 

         
            elif key > node.key:#checa se a chave é maior
                nextNode=node.dir # o nó para testar será a direita
                if key==nextNode.key: # depois checa se o nó a direita é o procurado
                    
                    if nextNode.esq != None and nextNode.dir != None: # checa se ele é o 3º caso
                        node.dir=self.__changeNode(nextNode.dir) 
                    
                    elif nextNode.esq != None: node.dir= nextNode.esq # checa se ele é 2º caso esquerda
                    elif nextNode.dir != None: node.dir= nextNode.dir # checa se ele é 2º caso direita
                    
                    return nextNode #caso seja o nó procurado será retornado      
    
            return self.__removerNo(key,nextNode) #Há algum caminho para seguir, então continua
        
        else: raise SearchArborException(2,'KEY NOT FOUND!') #Não há mais caminho para este nó


    def __changeNode(self, node:Node): #Checado, tá tranquilo  eu acho...
        lowerNode=node #O node é atribuido como o menor node daquela sub-árvore
        '''Caso o node possua uma sub-árvore, ele deverá trocado pelo menor nó a sua direita, ou seja, o node mais a esquerda da sua direita'''
        
        if node.esq==None: #caso ele seja o node que possua a menor chave daquela sub-árvore
            node=None # Ele irá se tornar vazio, pois irá ser movido para a posição do nó que será removido.
            return lowerNode
        
        elif node.esq.esq==None: # caso ele não seja o menor, mas o seu próximo seja.
            lowerNode=node.esq # o Menor nó será considerado a sua esquerda
            
            if lowerNode.dir != None: # Checa se há algo a direita do menor nó
                node.esq= lowerNode.dir #o Nó que aponta para o menor nó, passará a apontar para a direita desse.
        
            return lowerNode
        
        return self.__changeNode(node.esq) #se houver algum nó a esquerda deste, ele irá fazer o teste naquele.
            
        
    #== == == Método que remove todos os nós de maneira que não deixe vestígios na memória 
    def esvazia(self):
        try:
            assert not(self.estaVazia())
            self.__raiz=self.__libera(self.__raiz)
            
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')
        
    def libera(self,proximoNo)->None:
        
        if ( not self.estaVazia() and proximoNo  !=  None):
            
            proximoNo.esq= self.libera(proximoNo.esq)
            
            proximoNo.dir= proximoNo=self.libera(proximoNo.dir)
        return None
    
    #== == == Método que mostra a quantidade de nós folhas presente na árvore
    def leafs(self):
        try:
            assert not( self.estaVazia())
            return self.__leafs(self.__raiz)
        except AssertionError:
            raise SearchArborException('THERE IS NOT A ROOT')
    
    
    def __leafs(self,proximoNo:Node):
        leafsQuanty=0
        if proximoNo==None: #== == Só por precaução...
            return leafsQuanty
        if proximoNo.dir==None and proximoNo.esq==None:
            return 1
        leafsQuanty+=self.__leafs(proximoNo.esq)
        leafsQuanty+=self.__leafs(proximoNo.dir)
        return leafsQuanty
    
    def profundidade(self):
        try:
            assert not( self.estaVazia())
            return (self.__profundidade(self.__raiz) -1)
        except AssertionError:
            raise SearchArborException('THERE IS NOT A ROOT')
        
    def __profundidade(self, proximoNo:Node):
        alturaEsquerda=0
        alturaDireita=0
        if proximoNo==None:
            return 0
        alturaEsquerda= 1 + self.__profundidade(proximoNo.esq)
        alturaDireita= 1 + self.__profundidade(proximoNo.dir)
        return (max(alturaEsquerda,alturaDireita))
    
    def getLevel(self,key)->int:
        try:
            assert not( self.estaVazia())
            level=(self.__getLevel(key,self.__raiz) - 1 )
            return level

        except AssertionError:
            raise SearchArborException('THERE IS NOT A ROOT')

    def __getLevel(self,key, NodeAtual:Node)->int:
        level=0

        if NodeAtual==None:
            return level # caso tenha chegado no extremo da árvore
        
        if NodeAtual.carga == key:  # ele achou a carga, então retornará 1
            return level + 1
        
        level = self.__getLevel(key,NodeAtual.esq)
        if level: 
            return level + 1 # encontrou o nó na esqueda
        
        level = self.__getLevel(key,NodeAtual.dir)
        if level: 
            return level + 1 # encontrou o nó na direita
        
        return level + 1# Não achou em nenhum dos casos
    
    