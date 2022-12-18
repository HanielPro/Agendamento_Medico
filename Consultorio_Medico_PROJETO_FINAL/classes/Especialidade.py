from EstruturasDeDados.Lista.ListaEncadeada import *
from Paciente import Paciente
from threading import Semaphore


class Especialidade:
    def __init__(self,nomeclatura:str) -> None:
        self.__nomeclatura= nomeclatura.upper()
        self.__listaEspera= Lista()
        self.__quantyPacientes=Semaphore(0)
        self.__patientMutex=Semaphore(1)
    
    @property
    def nomeclatura(self)->str:
        return self.__nomeclatura
    
    @property
    def listaEspera(self)->Lista:
        return self.__listaEspera
    
    def inserirPaciente(self,key:any,paciente:Paciente): #Método que insere um paciente na lista de espera
        '''Insere um paciente na lista de espera'''
        self.__patientMutex.acquire()

        posicao=self.__checarPosicaoPorGravidade(paciente,1)
        self.__listaEspera.inserir(key,paciente,posicao)
        
        self.__patientMutex.release()
        self.__quantyPacientes.release()
        
    def RemoverPaciente(self,key): #Método que remove um paciente na lista de espera
        '''Remove um paciente da lista de espera'''
        #self.__quantyPacientes.acquire()
        self.__patientMutex.acquire()

        posicao=self.__listaEspera.busca(key)
        paciente=self.__listaEspera.remover(posicao)
        self.__patientMutex.release()
        return paciente
    
    def RemoverPrimeiroPaciente(self)->Paciente:
        
        '''Remove o primeiro paciente da lista de espera'''
        self.__quantyPacientes.acquire()
        self.__patientMutex.acquire()
        paciente=self.__listaEspera.remover(1)
        self.__quantyPacientes.release()
        return paciente
        
    
    def __checarPosicaoPorGravidade(self,paciente:Paciente,posicaoAtual:int) -> int:

        '''

        Melhor Caso é quando a lista vazia ou a primeira posição é a certa: O(1)

        Maior parte dos caso quando a resposta está no meio da lista: O(N)

        Pior caso é quando a resposta está no final da lista: O(N)

        '''
        if self.__listaEspera.tamanho()< posicaoAtual : # Caso a lista esteja vazia, ou caso tenha chegado no final desta.
            return posicaoAtual

        pacienteAlocado= self.__listaEspera.elemento(posicaoAtual)
        if paciente > pacienteAlocado :# Checa se o paciente tem mais prioridade que o que já está na lista 

            return posicaoAtual

        return self.__checarPosicaoPorGravidade(paciente, posicaoAtual + 1) # caso a prioridade do paciente seja igual ou menor que o tal, ele irá tentar inserir depois deste.

    
    def __str__(self) -> str:
        #s=f'Especialidade Médica:{self.__nomeclatura}\nLista de espera:\n{self.__listaEspera.__str__()}'
        s=f'Especialidade Médica:{self.__nomeclatura}\n'
        return s