from EstruturasDeDados.estrutura import Estrutura

class Especialidade:
    def __init__(self,nomeclatura:str) -> None:
        self.__nomeclatura= nomeclatura
        self.__listaEspera= Estrutura
    
    @property
    def nomeclatura(self):
        return self.__nomeclatura
    
    @property
    def listaEspera(self):
        return self.__listaEspera