import random
import time

from threading import Thread
from classes.Paciente import Paciente
from classes.EstruturasDeDados.Lista.ListaEncadeada import ListException

class MedicException(Exception):
    def __init__(self,code,msg) -> None:
        '''1: Entrada de dados inválida'''
        super().__init__(f'MEDIC EXCEPTION {code}: {msg}')

class Medico:
    
    def __init__(self,matricula,nome:str,especialidade) -> None:
        
        self.__matricula=matricula
        self.__nome=nome.upper()
        self.__especialidade=especialidade
        self.__ConsultasIntervalo=random.randint(15,30)
        self.consultar=Thread(name= self.__nome, target=self.BuscarPaciente)
        self.consultar.start()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def especialidade(self):
        return self.__especialidade
    
    #== == == Só insere se a especialidade estiver na lista de especialidades no consultório
    @especialidade.setter
    def especialidade(self,especialidade):
        #assert especialidade in Hospital.especialidadesLista, MedicException('SPECIALTY NOT REGISTERED IN HOSPITAL')
        self.__especialidade=especialidade
    
    @property
    def ConsultasIntervalo(self):
        return self.__ConsultasIntervalo
    
    @ConsultasIntervalo.setter
    def ConsultasIntervalo(self,novoIntervalo:int):
        try:
            assert novoIntervalo>=1 and type(novoIntervalo)==int
            self.__ConsultasIntervalo=novoIntervalo
        except AssertionError:
            raise MedicException(1,'INVALID ENTERED TIME')

    #== == == -- Metodos do Médico
    
    def BuscarPaciente(self): #== == == O médico ficará esperando receber um paciente
        try:
            paciente=self.__especialidade.RemoverPrimeiroPaciente()
            
            #time.sleep(2)
            self.AtenderPaciente(paciente) # O médico n precisa saber dos semáforos, ele apenas segue a orientação da especialidade
            
        except ListException as LE:
            time.sleep(1)
            print(LE)
        #time.sleep(2)
    
    def AtenderPaciente(self,paciente:Paciente): #== == ==O médico deverá atender o paciente que contém a sua especialidade
        TempoConsulta= random.randint(10,20)
        #print(f"{'==='*30 :^20}")
        
        #self.consulta.join()
        print( f'O paciente:{paciente.nome}, acabou de entrar no consultório do médico: {self.__nome}, especialidade: {self.__especialidade.nomeclatura}, a consulta levará: {TempoConsulta} segundos\n{"==="*30:^20}')
        
        time.sleep(TempoConsulta) # momento do atendimento
        #self.consulta.join()
        print(f"{'==='*30 :^20}")
        print( f'A consulta do paciente:{paciente.nome}, com o médico: {self.__nome}, especialidade: {self.__especialidade.nomeclatura}, acabou!')

    def __str__(self) -> str:
        return f' | matrícula: {self.__matricula}|  nome:{self.__nome}| especialide: {self.__especialidade.nomeclatura}| consultas sequenciais: {self.__ConsultasIntervalo}'