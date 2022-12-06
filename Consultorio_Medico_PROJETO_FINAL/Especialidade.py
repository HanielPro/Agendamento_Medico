from EstruturasDeDados.Lista.ListaEncadeada import *

class Especialidade:
    def __init__(self,nomeclatura:str) -> None:
        self.__nomeclatura= nomeclatura
        self.__listaEspera= Lista()
    
    @property
    def nomeclatura(self)->str:
        return self.__nomeclatura
    
    @property
    def listaEspera(self)->Lista:
        return self.__listaEspera
    
    def inserirPaciente(self,key,paciente): #Método que insere um paciente na lista de espera
        self.listaEspera.inserir(key,paciente)
    
    def RemoverPaciente(self,key): #Método que remove um paciente na lista de espera
        return self.listaEspera.remover(key)
    
    def organizarPaciente(self): #Organiza os pacientes que estão na lista apartir da gravidade, decrescente.
        pass
    
    def __str__(self) -> str:
        s=f'Especialidade Médica:{self.__nomeclatura}\nLista de espera:\n{self.__listaEspera.__str__()}'
        return s