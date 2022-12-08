class PacientException(Exception):
    def __init__(self, code:int, msg) -> None:
        #1: O CPF inserido não possui a quantidade permitidade de caracteres numéricos
        #2: A gravidade Inserida não está contida no dicionário.
        super().__init__(f'PACIENT EXCEPTION {code}: {msg}')


class Paciente:
    __gravidadePeso={
        'L1': 1,
        'L2': 3,
        'M1': 9,
        'M2': 15,
        'G': 21,
    }
    
    def __init__(self,cpf:str, nome:str, especialidadeDesejada:str, gravidade:str) -> None:
        try:self.__cpf= self.validarCPF(cpf)
        except: raise PacientException(1,'INVALID CPF ASSIGNMENT')

        self.__nome=nome
        self.__especialidadeDesejada=especialidadeDesejada
        self.__gravidade=self.__traduzirGravidade(gravidade)

    #== == == Property e setters
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
    
    #== == == Métodos da classe   
    
    #==  == Responsável por checar se o CPF é válido   
    def validarCPF(self,cpf:str):
        if len(cpf)==14: # Se for 14 caractéres, removerá os pontos e hífens. 
            cpf=cpf.replace('-','')
            cpf=cpf.replace('.','')
        assert len(cpf)== 11 # Primeiro checa o tamanho do cpf
        
        if self.__validarCPF(cpf):#Checará se todos os caractéres são dígitos
            return cpf
        else:
            raise Exception('INVALID CPF')
    
    #==  == Verifica quais foram os caractéres inseridos no cpf, precisa checar se de fat
    def __validarCPF(self,cpf:str)->bool:
        
        if len(cpf)==0: #== == Caso tenha chegado até o final da recurssão 
            return True

        elif '0123456789'.find(cpf[0]): # testa se o caractere é um digito
            return self.__validarCPF(cpf[1:]) # envia o próximo caractere
        
        return False # o caractere não era um número
    
    def __traduzirGravidade(self,gravidadeNome:str)->int:#retorna o valor contido no dicionário, referente a um valor de gravidade
    
        peso=self.__gravidadePeso.get(gravidadeNome)
        if peso ==None:
            raise PacientException(2,'INVALID GRAVITY ENTRY')
    
    def __str__(self) -> str:
        return f'cpf: {self.__cpf}| Nome: {self.__nome}| Desejo: {self.__especialidadeDesejada}| Gravidade: {self.__gravidade}'
    