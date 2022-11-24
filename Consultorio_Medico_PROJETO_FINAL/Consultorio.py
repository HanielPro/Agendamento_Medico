from EstruturasDeDados.Lista.ListaEncadeada import *
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
         
    def consultarEspecialidade(self,key:any)->str:# Retorna as informações de uma especialidade
        try:
            posicao=self.__Escpecialidades.busca(key)
            return self.__Escpecialidades.elemento(posicao)
        except ListaException as LE:
            raise ClinicException(LE)
            