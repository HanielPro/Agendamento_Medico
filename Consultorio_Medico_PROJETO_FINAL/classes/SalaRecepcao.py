if __name__!='__main__':
    from classes.EstruturasDeDados.Lista.ListaEncadeada import Lista,ListException
    from classes.Paciente import Paciente,PatientException
#from Consultorio import Consultorio,ClinicException,consultorio1

#== Caso o usuário Digite uma escolha indevida
class ReceptionException(Exception):
    def __init__(self,code, msg) -> None:
        '''
        0:Algo extraordinariamente extraordiordinário 
        1: Foi fornecido dados insuficientes ou errados a respeito do Paciente [PATIENTEXCEPTION]   
        2: Ocorreu algum erro ao inserir, remover ou consultar algum elemento na lista de aguardo [LISTEXCEPTION]
        3: Ocorreu algum erro na entrada dos dados [RECEPTIONEXCEPTION]
        '''
        super().__init__(f'Reception Exception {code}: {msg}')
        
class SalaRecepcao():
    '''Apressenta todas os métodos e variáveis que o CLIENTE precisa.'''
    def __init__(self):
        self.__listaAguardo= Lista() #lista de Aguardo é onde os pacientes ficam localizados até serem chamados para entrar na área do consultório
        #self.__consultorio= consultorio
    
    def __str__(self) -> str:
        return str(self.__listaAguardo)
    
    #== == Esta função insere o paciente na lista de aguardo da Sala de Recepção
    def ListarPaciente(self,cpf:str, nome:str, especialidadeDesejada:str, gravidade:str)-> None:
        '''Adiciona um novo paciente a lista de espera'''
        try:
            
            cpf=self.__translateCPF(cpf)
            newPaciente=Paciente(cpf,nome,especialidadeDesejada,gravidade)
            posicao=self.__checarPosicaoPorGravidade(newPaciente,1) # a posição é gerada a partir de uma busca na lista pela menor prioridade
            self.__listaAguardo.inserir(cpf,newPaciente,posicao) 
            return '+OK PATIENT INSERTED'
        
        except PatientException as PE:
            raise ReceptionException(1,f'INVALID DATA PROVIDED ABOUT THE PATIENT: \n{PE}')
        
        except ListException as LE:
            raise ListException(2,f'SOMETHING DID WRONG WHEN I TRIED TO INSERT A PATIENT:\n{LE}')
    
    #== == Este método deverá retornar a posição da lista de aguardo o paciente deverá ser inserido. O índice é gerado a partir da gravidade do tal.
    #-- -- Na dúvida, cheque o dicionário de gravidades do cliente
    
    def __checarPosicaoPorGravidade(self,paciente:Paciente,posicaoAtual:int) -> int:
        '''
        Esta função permite organizar os pacientes na listaAguardo a partir da gravidade. Segue um exemplo de como a lista ficaria:
        G G G M2 M1 L2 L1 L1
         
        Melhor Caso é quando a lista vazia ou a primeira posição é a certa: O(1)
        Maior parte dos caso quando a resposta está no meio da lista: O(N)
        Pior caso é quando a resposta está no final da lista: O(N)
        '''
        if self.__listaAguardo.tamanho()< posicaoAtual : # Caso a lista esteja vazia, ou caso tenha chegado no final desta.
            return posicaoAtual
        
        pacienteAlocado= self.__listaAguardo.elemento(posicaoAtual)
        if paciente > pacienteAlocado :# Checa se o paciente tem mais prioridade que o que já está na lista 
            return posicaoAtual
        
        return self.__checarPosicaoPorGravidade(paciente, posicaoAtual + 1) # caso a prioridade do paciente seja igual ou menor que o tal, ele irá tentar inserir depois deste.

    #== == Esta função remove permanentemente o paciente da lista de aguardo da Sala de Recepção    
    def removerPaciente(self,cpf:str)->str:
        '''Remove um único paciente da lista de aguardo'''
        try:
            cpf= self.__translateCPF(cpf)
            self.__listaAguardo.remover(self.__listaAguardo.busca(cpf))
            return '+OK PATIENT REMOVED'
        except ListException as LE:
            raise ReceptionException(2,f'SOMETHING DID WRONG WHEN I TRIED TO REMOVE A PATIENT:\n{LE}')
    
    
    #== == Esta função remove permanentemente o paciente da lista de aguardo da Sala de Recepção    
    def consultarPaciente(self,cpf:str)->str:
        '''Obtem a informação de um paciente através de seu cpf'''
        try:
            cpf= self.__translateCPF(cpf)
            posicao=self.__listaAguardo.busca(cpf)
            paciente=self.__listaAguardo.elemento(posicao)
        
        except ListException as LE:
            raise ReceptionException(2,f'SOMETHING DID WRONG WHEN I TRIED TO CATCH A PATIENT:\n{LE}')
        return str(paciente)
    
    #== == Esta função remove permanentemente Todos os pacientes da lista de aguardo da Sala de Recepção
    def removerTodosPacientes(self):
        ''' Remove todos os pacientes da lista de aguardo'''
        self.__listaAguardo.esvazia()
    
    #== == Esta função envia um paciente da lista de aguardo da Sala de Recepção para o consultório
    
    def despacharPaciente(self,cpf:str)->str:
        '''Envia um único paciente da lista de aguardo para o consultório'''
        try:
            cpf= self.__translateCPF(cpf)
            pacienteDespacho=self.__listaAguardo.remover(self.__listaAguardo.busca(cpf))

        except ListException as LE:
            raise ReceptionException(2,f'SOMETHING DID WRONG WHEN I TRIED TO CATCH A PATIENT:\n{LE}')

        
        nome=pacienteDespacho.nome.split()
        nome='#'.join(nome)
        return f'{pacienteDespacho.cpf}/{nome}/{pacienteDespacho.especialidadeDesejada}/{pacienteDespacho.stringuificarGravidade()}'

    #== == Esta função envia todos os pacientes da lista de aguardo da Sala de Recepção para o consultório
    def despacharTodosPacientes(self)->str:
        '''Retorna uma lista contendo todos os pacientes da lista de aguardo'''
        todosPacienteParaDespachar=[]
        while not(self.__listaAguardo.estaVazia()):
            
            pacienteParaDespachar=self.__listaAguardo.elemento(1)
            
            pacienteParaDespachar=self.despacharPaciente(pacienteParaDespachar.cpf)
            
            todosPacienteParaDespachar.append(pacienteParaDespachar)
        
        return ' '.join(todosPacienteParaDespachar)
    
    def __translateCPF(self,cpf:str)->str:
        '''Este método serve para transforma o CPF contendo sinais e transforma em uma cadeia de números'''
        
        if len(cpf)>11: # Se for acima de 11 caractéres, removerá os pontos e hífens. 
            cpf=cpf.replace('-','')
            cpf=cpf.replace('.','')
        elif len(cpf) != 11:
            raise ReceptionException(3,'WRONG CPF ENTRY')
        return cpf
        
if __name__=='__main__':
    from EstruturasDeDados.Lista.ListaEncadeada import Lista
    from Paciente import Paciente

    sala1=SalaRecepcao()
    sala1.ListarPaciente("34823019705","Joaseiro da Costa","Pediatria","L2")
    sala1.ListarPaciente("56567424223","Pedro Neto SIlveira","Psiquiatria","G")
    sala1.ListarPaciente("12321313323","Rogerio SIlveira","Pediatria","M2")
    sala1.ListarPaciente("12321313301","Paulo Florinopolis","Pediatria","G")
    sala1.ListarPaciente("12321313820","Paulo Cantando","Pediatria","G")
    sala1.ListarPaciente("12321313834","Paulo lanchando","Pediatria","L1")
    sala1.ListarPaciente("12321313853","Paulo bebendo","Pediatria","L1")
    sala1.ListarPaciente("12321313872","Paula Sorrino","Pediatria","L1")
    sala1.ListarPaciente("12321313651","Paulo Subindo","Psiquiatria","G")
    sala1.ListarPaciente("12321313303","Paulo Chorando","Pediatria","G")
    sala1.ListarPaciente("12321313356","Paula Equinó","Pediatria","L1")
    
    print(sala1)
    input()

    print(sala1.despacharPaciente('12321313356'))
    print(sala1.despacharTodosPacientes())
    print(sala1)
    input('Mostrando as informações do consultório')

    #-- -- Testando o consultorio