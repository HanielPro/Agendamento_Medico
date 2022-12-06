class PacientException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(f'PACIENT EXCEPTION: {msg}')


class Paciente:
    
    def __init__(self,cpf:str, nome:str, especialidadeDesejada:str, gravidade:str) -> None:
        self.__nome=nome
        self.__especialidadeDesejada=especialidadeDesejada
        
        #if tempoEstimadoConsultaMinutos<0: raise PacientException('INVALID ENTERED TIME')
        #self.__tempoEstimadoConsultaMinutos= tempoEstimadoConsultaMinutos
        
        try:self.__cpf= self.validarCPF(cpf)
        except: raise PacientException('INVALID CPF ASSIGNMENT')
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def especialidadeDesejada(self):
        return self.__especialidadeDesejada
    
    @especialidadeDesejada.setter
    def especialidadeDesejada(self,especialidadeDesejada):
        self.__especialidadeDesejada=especialidadeDesejada
    
    '''
    @property
    def tempoEstimadoConsultaMinutos(self):
        return self.__tempoEstimadoConsultaMinutos

    
    @tempoEstimadoConsultaMinutos.setter
    def tempoEstimadoConsultaMinutos(self,tempoEstimado:int):
        try:
            assert tempoEstimado>0 and type(tempoEstimado)==int
            self.__tempoEstimadoConsultaMinutos=tempoEstimado

        except:
            raise PacientException('INVALID ENTERED TIME')
    '''
        
    #== == == Responsável por checar se o CPF é válido   
    def validarCPF(self,cpf:str):
        if len(cpf)==14: # Se for 14 caractéres, removerá os pontos e hífens. 
            cpf=cpf.replace('-','')
            cpf=cpf.replace('.','')
        assert len(cpf)== 11 # Primeiro checa o tamanho do cpf
        
        if self.__validarCPF(cpf):#Checará se todos os caractéres são dígitos
            return  cpf
        else:
            raise Exception('INVALID CPF')
    
    #== == == Verifica quais foram os caractéres inseridos no cpf, precisa checar se de fat
    def __validarCPF(self,cpf:str)->bool:
        
        if len(cpf)==0: #== == Caso tenha chegado até o final da recurssão 
            return True

        elif '0123456789'.find(cpf[0]): # testa se o caractere é um digito
            return self.__validarCPF(cpf[1:]) # envia o próximo caractere
        
        return False # o caractere não era um número
             
    def __str__(self) -> str:
        #return f'Nome: {self.__nome}, CPF: {self.__cpf} especialidadeDesejada desejado: {self.__especialidadeDesejada}, tempo estimadoda consulta em minutos: {self.__tempoEstimadoConsultaMinutos}'
        return f'Nome: {self.__nome}, CPF: {self.__cpf} especialidadeDesejada desejado: {self.__especialidadeDesejada}'
    