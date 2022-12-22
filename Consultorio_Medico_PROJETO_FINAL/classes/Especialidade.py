
from classes.Paciente import Paciente
from threading import Semaphore
from classes.EstruturasDeDados.Lista.ListaEncadeada import Lista, ListException

class Especialidade:
    def __init__(self,nomeclatura:str,consultorio) -> None:
        self.__nomeclatura= nomeclatura.upper()
        self.__listaEspera= Lista()
        self.__consultorio=consultorio
        self.__quantyPacientes=Semaphore(0)#inicia vazia, pois ela serve para indicar a quantidade de pacientes naquela especialidade
        self.__patientCriticalMutex=Semaphore(1)

    def __str__(self) -> str:
        s=f'{self.__nomeclatura}\n Patients:\n {self.__listaEspera}'
        return s
    
    @property
    def nomeclatura(self)->str:
        return self.__nomeclatura
    
    @property
    def listaEspera(self)->Lista:
        return self.__listaEspera
    
    def inserirPaciente(self,key:any,paciente:Paciente): #Método que insere um paciente na lista de espera
        '''Insere um paciente na lista de espera'''
        #self.__patientCriticalMutex.acquire()

        posicao=self.__checarPosicaoPorGravidade(paciente,1)
        self.__listaEspera.inserir(key,paciente,posicao)
        
        #self.__patientCriticalMutex.release()
        self.__quantyPacientes.release()

    

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


    def RemoverPaciente(self,key): #Método que remove um paciente na lista de espera
        '''Remove um paciente da lista de espera'''
        
        if len(self.__listaEspera)==0:
            return '-ERR The list is empty'
        try:
            
            #self.__quantyPacientes.acquire()
            self.__patientCriticalMutex.acquire()#entra na zona critica
            
            posicao=self.__listaEspera.busca(key)#procura por uma detemrinada chave
            paciente=self.__listaEspera.remover(posicao)#remove o paciente atraves da posicao fornecida

            self.__patientCriticalMutex.release()

            return paciente

        except ListException:#caso seja retornado um erro#
            self.__patientCriticalMutex.release()#ele rapidamente sai da área crítica
            
            return '-ERR Key not found'

    
    def RemoverPrimeiroPaciente(self)->Paciente:        
        '''Remove o primeiro paciente da lista de espera e também do consultório'''
        try:
            #== == -- --Entrada na zona crítica da especialidade
            self.__quantyPacientes.acquire()
            self.__patientCriticalMutex.acquire()#entra na zona critica
        
            paciente=self.__listaEspera.remover(1)
            #print(paciente)
            #== == -- --Entrada da zona critica do consultório
            self.__patientCriticalMutex.release()
            #== == -- --Saída da zona critica da especialidade
            self.__consultorio.removerPacienteConsultado(paciente.cpf)
            
            
            
            #== == -- --Saída da zona critica do consultório
            return paciente
        
        except ListException:#caso seja retornado um erro
            self.__patientCriticalMutex.release()#ele rapidamente sai da área crítica
            self.__quantyPacientes.acquire()#ele retorna a quantidade de paciente para o antigo estado
            return '-ERR Key not found'
        