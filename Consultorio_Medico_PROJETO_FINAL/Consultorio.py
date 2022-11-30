from EstruturasDeDados.Lista.ListaEncadeada import *
from EstruturasDeDados.Arvore.ArvoreBusca import *
from Medico import *
from Paciente import *
from Especialidade import *
import random
#from EstruturasDeDados.Arvore.ArvoreBusca import *

class ClinicException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
        

class Consultorio:   
    
    def __init__(self) -> None:
        self.__Escpecialidades=Lista()#O nome está errado
        self.__IndexEspecialidades=Lista()#index para as especialidades
        self.__Pacientes=ArvoreBusca()
        self.__Medicos= ArvoreBusca()
        self.idcounter=list()
    
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
         
    def ConsultarEspecialidade(self,key:any)->any:# Retorna as informações de uma especialidade
        try:
            posicao=self.__Escpecialidades.busca(key)
            return self.__Escpecialidades.elemento(posicao)
        except ListaException as LE:
            raise ClinicException('MEDICAL SPECIALITY NOT FOUND')
        
    #== == == -- Métodos relacionados ao Médico
    
    def inserirMedico(self,nome:str,especialidade:str,ConsultasIntervalo:int=15)->None: #== == Adiciona um novo médico a Árvore de médicos
        try:
            
            key=self.ConsultarEspecialidade(especialidade)
            id=self.getId()
            NewMedic=Medico(id,nome,especialidade,ConsultasIntervalo)
            self.__Medicos.InserirNode(id,key,NewMedic)
            #self.__Medicos.inserir(key,NewMedic)
        except Exception as E:
            print(E)
    def ExibirMedicos(self):
        self.__Medicos.imprimir()
        return ''
    
    def RemoverMedico(self, key:any)->None: # Remove um médico da lista
        try:
            self.__Medicos.removerNo(key)
            print('\033[31m'+'O médico com o id ',key,' foi demitido'+'\033[0;0m')
        except Exception as E:
            print(E)
    def RemoverPaciente(self,key:any)->None:
        try:
            self.__Pacientes.removerNo(key)
            print('\033[31m'+'O médico com o id ',key,' foi morto'+'\033[0;0m')
        except Exception as E:
            print(E)
    
    def ConsultarMedico(self,key:any)->any:# Retorna as informações de uma especialidade
        #try:
            #posicao=self.__Medicos.busca(key)
            #return self.__Medicos.elemento(posicao)
        print('Já Já Consulta ', key)
        #except ListaException as LE:
        #    raise ClinicException('MEDICAL SPECIALITY NOT FOUND')
    
    def __str__(self):
        print(self.__Escpecialidades)
        return 'a'       
    # Metodos relacionados ao paciente
    def inserirPaciente(self,cpf:int,nome:str,especialidade:str,gravidade:str):
        try:
            key=self.ConsultarEspecialidade(especialidade)
            NewPaciente=Paciente(cpf,nome,especialidade,gravidade)
            self.__Pacientes.InserirNode(cpf,key,NewPaciente)
            #self.__Medicos.inserir(key,NewMedic)
        except Exception as E:
            print(E)
    def ExibirMedicos(self):
        self.__Medicos.imprimir(0)
        return ''
    def ExibirPacientes(self):
        self.__Pacientes.imprimir(1)
        return ''
    def getId(self):
        #num=(f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}')
        flag=True
        while flag:
            num=''
            for i in range(8):
                num+=str(random.randint(0,9))
            if num in self.idcounter:
                flag=True
            else:
                self.idcounter.append(num)
                return num
    #METODOS DE TESTES
    def findthesmaller(self):
        self.__Medicos.smaller()
        return ''