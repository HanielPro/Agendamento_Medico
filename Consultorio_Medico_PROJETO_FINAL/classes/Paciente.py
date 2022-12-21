class PatientException(Exception):
    '''
        1: O CPF inserido não possui a quantidade permitidade de caracteres numéricos
        2: A gravidade Inserida não está contida no dicionário.
    '''
    def __init__(self, code:int, msg) -> None:
        super().__init__(f'PATIENT EXCEPTION {code}: {msg}')


class Paciente:
    __gravidadeValores={
        'L1': 1,
        'L2': 3,
        'M1': 9,
        'M2': 15,
        'G': 21,
    }
    __TraducoesPesosGravidade={
         '1': 'L1',
         '3': 'L2',
         '9': 'M1',
         '15': 'M2',
         '21': 'G',
    }
        
    def __init__(self,cpf:str, nome:str, especialidadeDesejada:str, gravidade:str) -> None:

        self.__cpf= self.validarCPF(cpf)
        self.__nome=nome.upper()
        self.__especialidadeDesejada=especialidadeDesejada.upper()
        self.__gravidadePeso=self.__gravidadeValores.get(gravidade)
        if self.__gravidadePeso==None:
            raise PatientException(2,'INVALIDY GRAVITY ENTRY')  

    def __eq__(self, __outroPaciente: object) -> bool:
        if isinstance(__outroPaciente,Paciente):
            return self.__gravidadePeso == __outroPaciente.gravidadePeso
        return False
    
    def __gt__(self, __outroPaciente: object)->bool:
        if isinstance(__outroPaciente,Paciente):
            return self.__gravidadePeso > __outroPaciente.gravidadePeso
        return False
    
    #== == == Property e setters
    @property
    def cpf(self)->str:
        return self.__cpf

    @property
    def nome(self)->str:
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome
 
    @property
    def especialidadeDesejada(self):
        return self.__especialidadeDesejada
    
    @property
    def gravidadePeso(self)->int:
        return self.__gravidadePeso
    
    @especialidadeDesejada.setter
    def especialidadeDesejada(self,especialidadeDesejada):
        self.__especialidadeDesejada=especialidadeDesejada
    
    #== == == Métodos da classe   
    
    #==  == Responsável por checar se o CPF é válido   
    def validarCPF(self,cpf:str):
        '''Verifica se o CPF inserido  É coerente'''
        try:
            if len(cpf)>11: # Se for acima de11 caractéres, removerá os pontos e hífens. 
                cpf=cpf.replace('-','')
                cpf=cpf.replace('.','')
            assert len(cpf)== 11 #Primeiro checa o tamanho do cpf
            
            if self.__validarCPF(cpf):#Checará se todos os caractéres são dígitos
                return cpf
            
            else:
                raise PatientException(1,'INVALID CPF ASSIGNMENT')
        
        except AssertionError:
            raise PatientException(1,'INVALID CPF ASSIGNMENT')  
        
    #==  == Verifica quais foram os caractéres inseridos no cpf, precisa checar se de fat
    def __validarCPF(self,cpf:str)->bool:
        
        if len(cpf)==0: #== == Caso tenha chegado até o final da recurssão 
            return True

        elif '-0123456789'.find(cpf[0]): # testa se o caractere é um digito
            return self.__validarCPF(cpf[1:]) # envia o próximo caractere
        
        return False # o caractere não era um número
        
    
    def stringuificarGravidade(self)->str:
        '''Transforma o peso da gravidade na String Original'''
        peso= self.__TraducoesPesosGravidade.get(str(self.__gravidadePeso))
        return peso
    
    def transalteCPF(self)->str:
        '''Este método serve para transformar uma cadeia de números de CPF,  e transforma em um CPF com sinais'''
        cpfConjunto=[]
        cpf=self.__cpf
        
        for i in range(len(cpf)):
        
            if i ==2 or i==5:
                cpfConjunto.append( f'{cpf[i]}.')
            elif i==8:
                cpfConjunto.append( f'{cpf[i]}-')
            else:
                cpfConjunto.append(cpf[i])       
        
        return ''.join(cpfConjunto)      
    
    def __str__(self) -> str:
        return f'cpf: {self.transalteCPF()}| Nome: {self.__nome}| Desejo: {self.__especialidadeDesejada}| Gravidade: {self.stringuificarGravidade()}'
    