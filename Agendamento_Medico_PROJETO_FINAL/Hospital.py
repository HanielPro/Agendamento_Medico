from EstruturasDeDados.Lista.ListaEncadeada import *
from Medico import *
from Paciente import *
from Especialidade import *
#from EstruturasDeDados.Arvore.ArvoreBusca import *

class ClinicException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
        

class Consultorio:   
    
    def __init__(self) -> None:
        self.__Escpecialidades=Lista()
        #self.__Pacientes=Arvore()
        #self.__Medicos= Arvore()
    
    #== == == -- Métodos Relacionados Com A especialidade
    def inserirEspecilidade(self,nomeclatura:str)->None: # Insere uma especialidade na Lista de especialidades na clínica
        try:
            self.__Escpecialidades.inserir(nomeclatura, nomeclatura) # por enquanto, a chave será o próprio nome da lista
        
        except ListaException as LE:
            raise ClinicException(LE)
    
    def removerEspecialidade(self,key:any)->None:# Remove uma especialidade na Lista de especialidades na clínica
        try:
            posicao=self.__Escpecialidades.busca(key)
            self.__Escpecialidades.remover(posicao)
        except ListaException as LE:
            raise ClinicException(LE)
         
    def ConsultarEspecialidade(self,key:any)->Especialidade[object]:# Retorna as informações de uma especialidade
        try:
            posicao=self.__Escpecialidades.busca(key)
            return self.__Escpecialidades.elemento(posicao)
        except ListaException as LE:
            raise ClinicException('MEDICAL SPECIALITY NOT FOUND')
        
    #== == == -- Métodos relacionados ao Médico
    
    def inserirMedico(self, key:any, nome:str,especialidade:str,ConsultasIntervalo:int=15)->None: #== == Adiciona um novo médico a Árvore de médicos
        try:
            especialidadeMedica=self.ConsultarEspecialidade(especialidade)
            NewMedic=Medico(nome,especialidadeMedica,ConsultasIntervalo)
            #self.__Medicos.inserir(key,NewMedic)
            print(NewMedic)
        except Exception as E:
            print(E)
    
    def RemoverMedico(self, key:any)->None: # Remove um médico da lista
        try:
            #self.__Medicos.remover(key)
            print('Já Já sai ', key)
        except Exception as E:
            print(E)
    
    def ConsultarMedico(self,key:any)->memoryview[object]:# Retorna as informações de uma especialidade
        #try:
            #posicao=self.__Medicos.busca(key)
            #return self.__Medicos.elemento(posicao)
        print('Já Já Consulta ', key)
        #except ListaException as LE:
        #    raise ClinicException('MEDICAL SPECIALITY NOT FOUND')
        