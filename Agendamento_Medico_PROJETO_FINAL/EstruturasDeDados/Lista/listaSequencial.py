#== == == == lista Exception
class ListaException(Exception):
    def __init__(self, msg,codeError:int=0):
        super().__init__(msg)
        self.__codError=codeError
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.

#== == == == A estrutura de dado lista, ou LIFO.
class Lista:
    def __init__(self):
        self.__lista=[] # A lista inicia vazia.

#== == == == Método para examinar se a lista está vazia
    def estaVazia(self)->bool:
        return len(self.__lista) == 0
    
#== == == == Método para checar o tamanho da lista
    def tamanho(self):
        return len(self.__lista)

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->any:
        try:
            #== == Só funciona se: a lista NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.tamanho()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da lista é de {self.tamanho()} nó(s)!'
            
            return self.__lista[posicao-1]
        
        except AssertionError as AE:
            raise ListaException(AE)
        except Exception as E:
            raise ListaException(E)
        else:
            return valorNo

#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, conteudo:any)->int:
        try:
            #== == O método só não funciona quando a lista estiver vazia
            assert not self.estaVazia() ,'A lista está vazia!'
            
            for i in range(len(self.__lista)):
                if self.__lista[i]==conteudo:
                    return i
                              
            raise ListaException('Contéudo inserido não foi encontrado!') # o contéudo não foi Achado.
    
        except AssertionError as AE:
            raise ListaException(AE)
        except Exception as E:
            raise ListaException(E)
                
##== == == == Método que Modificará o contéudo de um nó a partir da possição exigida.
    def modificar(self, posicao:int, conteudo: any):
        try:
            #== == Só funciona se: a lista NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.tamanho()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da lista é de {self.tamanho()} nó(s)!'
        
            self.__lista[posicao-1]= conteudo
 
        except AssertionError as AE:
            raise ListaException(AE)
        
        except Exception as E:
            raise ListaException(E)
        
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
    

