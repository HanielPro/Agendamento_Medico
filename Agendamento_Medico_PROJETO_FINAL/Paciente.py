class PacientException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(f'PACIENT EXCEPTION: {msg}')


class Paciente:
    '''
    #== == == == O Paciente deverá conter:
    #CPF= STRING, terá que ser de tamanho 11 (excluindo os '.' e o '-') ou tamanho 14 (incluindo os '.' e '-') {Será a responsável por identificar os pacientes.
     # Não poderá existir pacientes com o mesmo CPF.
     # Deverá ser uma propriedade inalterável. 
    }

    #Nome= String sem restrição {O nome do Paciente em questão}
    
    #EspecialistaDesejado= String, sem restrição{
        Ela é responsável por ditar com qual  Médico o Paciente deverá interagir{
            EX: Paciente que busca um Oftamologísta, deve ser atendido por um Medico com especialidade em Oftalmologia             
        }
        O paciente pode desejar qualquer tipo de especialidade, mas o Hospital só poderá admitir uma consulta com  um Médico que contenha a tal especialidade.  
        O Paciente só poderá desejar a consulta com um único especialista.
    }
    
    #tempoEstimadoConsultaMinutos= Int, só pode ser aceito, consultas de 1 minuto ou acima{
            Ela é  a responsável por permitir que  um paciente  entrar ou não na lista de espera do Médico{
            EX: Um Paciente que possui uma consulta de 70 minutos, e o médico só possui  1 minuto livre, o paciente poderá entrar na fila, pois o limite ainda não foi atingido.
        }         
    }
    '''
    '''
    #== == == == O Paciente deverá Fazer:
    #Ele Poderá alterar seus atributos quando quiser desde que as modificações estejam de acordo com as restrições dos atributos.
    '''
    
    def __init__(self,cpf:str, nome:str,especialista:str, tempoEstimadoConsultaMinutos:int) -> None:
        self.__nome=nome
        self.__especialista=especialista
        
        if tempoEstimadoConsultaMinutos<0: raise PacientException('INVALID ENTERED TIME')
        self.__tempoEstimadoConsultaMinutos= tempoEstimadoConsultaMinutos
        
        try:self.__cpf= self.validarCPF(cpf)
        except: raise PacientException('INVALID CPF ASSIGNMENT')
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def especialista(self):
        return self.__especialista
    
    @especialista.setter
    def especialista(self,especialista):
        self.__especialista=especialista
    
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
        return f'Nome: {self.__nome}, CPF: {self.__cpf} Especialista desejado: {self.__especialista}, tempo estimadoda consulta em minutos: {self.__tempoEstimadoConsultaMinutos}'
    