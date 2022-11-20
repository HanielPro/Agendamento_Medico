#== == == == Fila Exception
from mimetypes import init


class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.

class No:
    def __init__(self,carga) -> None:
        self.carga=carga
        self.prox=None

class NoCabeca:
    tamanho=0
    start=None
    end=None

#== == == == A estrutura de dado Fila, ou FIFO.

class Fila:
    def __init__(self):
        self.__Cabeca=NoCabeca()


#== == == == Método para examinar se a fila está vazia
    def estaVazia(self)->bool:
        return self.__Cabeca.tamanho == 0
    
#== == == == Método para checar o tamanho da fila

#== == Checa a quantidade de nós inserido
    def __len__(self):
        return self.__Cabeca.tamanho
    
#== == Checa o tamanho Máximo    
    def tamanho(self):
        return self.__Cabeca.tamanho

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->any:
        try:
            #== == Só funciona se: a fila NÃO estiver vazia e a posição inserida não exceda o tamanho limite da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__len__()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da fila é de {self.__len__()} nó(s)!'
            
            cont=1
            cursor=self.__Cabeca.start
            while cont < posicao:
                cursor= cursor.prox
                cont+=1
            return cursor.carga
        
        except AssertionError as AE:
            raise FilaException(AE)
        except Exception as E:
            raise FilaException(E)


#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, conteudo:any)->int:
        try:
            #== == O método só não funciona quando a lista estiver vazia
            assert not self.estaVazia() ,'A lista está vazia!'
            
            cursor=self.__Cabeca.start
            posicao=1
            
            while cursor!=None:
                if cursor.carga==conteudo:
                    return posicao
                cursor=cursor.prox
                posicao+=1
                
            raise FilaException('Contéudo inserido não foi encontrado!') # o contéudo não foi Achado.
    
        except AssertionError as AE:
            raise FilaException(AE)
        except Exception as E:
            raise FilaException(E)
                
##== == == == Método que Modificará o contéudo de um nó a partir da possição exigida.
    def modificar(self, posicao:int, conteudo: any):
        try:
            #== == Só funciona se: a fila NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__len__()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da fila é de {self.__len__()} nó(s)!'

            cursor=self.__Cabeca.start
            cont=1
            while cont< posicao:
                cursor=cursor.prox
                cont+=1
            cursor.carga=conteudo
 
        except AssertionError as AE:
            raise FilaException(AE)
        
        except Exception as E:
            raise FilaException(E)
        
    #== == Adiciona um novo Nó na fila.
    def enfileira(self, conteudo:any):
        
        novoNo=No(conteudo)
        if self.__Cabeca.tamanho>0:
            self.__Cabeca.end.prox=novoNo
            self.__Cabeca.end=novoNo    

        else: # não tem nenhum nó na lista
            self.__Cabeca.start=novoNo
            self.__Cabeca.end=novoNo
        
        self.__Cabeca.tamanho+=1
        
    #== == Remove o primeiro Nó adicionado na Fila.
    def desenfileira(self)->any:
        try:
            assert not self.estaVazia() ,'A lista está vazia!'
            
            valorStartNo=self.__Cabeca.start.carga
            self.__Cabeca.start=self.__Cabeca.start.prox
            self.__Cabeca.tamanho-=1
    
            return valorStartNo
            
        except AssertionError as AE:
            raise FilaException(AE)
        
        except Exception as E:
            raise FilaException(E)

    #== == Desenfila a fila até ela possuir Zero Nós.
    def esvazia(self):
        try:
            while self.__Cabeca.tamanho>0:
             self.desenfileira()
        except:
            pass


    def __str__(self)->str:
        if self.__Cabeca.tamanho==0:
            raise FilaException('Empty')
        s = ''
        cursor=self.__Cabeca.start
        cont=0
        
        while cursor != None:
            
            s += f' =|{cont + 1}: {cursor.carga}|= '
            
            cursor=cursor.prox
            cont+=1 

        return s + f'\n Nós inseridos até agora: {self.__Cabeca.tamanho}'