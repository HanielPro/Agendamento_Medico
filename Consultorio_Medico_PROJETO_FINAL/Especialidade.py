from EstruturasDeDados.Lista.ListaEncadeada import *

class Especialidade:
    def __init__(self,nomeclatura:str) -> None:
        self.__nomeclatura= nomeclatura
        self.__listaEspera= Lista()
    
    @property
    def nomeclatura(self):
        return self.__nomeclatura
    
    @property
    def listaEspera(self):
        return self.__listaEspera
    
    def __str__(self) -> str:
        s=f'Especialidade Médica:{self.__nomeclatura}\nLista de espera:\n{self.__listaEspera.__str__()}'
        return s