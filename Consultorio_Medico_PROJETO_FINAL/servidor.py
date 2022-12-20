from classes.Consultorio import Consultorio, ClinicException
import socket
#from threading import Thread, Semaphore

class ServerException(Exception):

    def __init__(self, code:int, msg:str) -> None:
        '''
        0: Método não encontrado.
        1: O cliente escreveu o método certo, mas não inseriu os parametros adequado
        2: Ocorreu algum erro dentro do consultorio
        '''
        super().__init__(f'Server Exception {code}: \n', msg)
        
#== == == == Métodos
def ExecMessage(msg:str,cliente:str): 
    '''
    Ele receberá a mensagem do cliente e execultará  o método transcrito nela. 
    '''
    global serverConection
    try:
        msg=msg.upper()
        msgTrunc=msg.split()
        method=MethodsServerDict[msgTrunc[0]]
        
        print(method)
        
        if method==1:
            
            if len(msgTrunc)==1 or len(msgTrunc)==2:
                serverConection.sendto(inform('CLINIC',cliente).encode(),cliente )
                return inform('CLINIC',cliente)
                    
            elif len(msgTrunc)==3:
                if msgTrunc[1]=='SPECIALITY':
                    return inform('SPECIALITY',msgTrunc[2])
            
                elif msgTrunc[1]=='MEDIC':
                    return inform('MEDIC',msgTrunc[2])
                
                elif msgTrunc[1]=='PATIENT':
                    return inform('PATIENT',msgTrunc[2])
      
            else:
                raise ServerException(1,'DID YOU KNOW HOW WRITE THE COMAND?')
        
        elif method==2:
            patient=msgTrunc[1].split('/')
            return dispatch(patient)
        
        elif method==3:
            patients=msgTrunc[1].split('/')
            return dispatchAll(patients)    
        
        elif method==4:
            return removePatient(msgTrunc[1])    
        
    except KeyError as KE:
        raise ServerException(0,'METHOD NOT FOUND')
    
def inform(type:str,cliente:str,key:str=None,):
    '''O MÉTODO RETORNA AS INFORMAÇÕES DEPENDENDO DA EXIGÊNCIA DO USUÁRIO
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [METHOD] ?[WHOM] ?[KEY]
    '''
    try:
        if type=='CLINIC':
            return str(consultorio)
        
        elif key==None:
            raise ServerException(1,'DID YOU KNOW HOW WRITE THE COMAND?')
            
        elif type=='SPECIALITY':
            return str(consultorio.captarEspecialidade(key))
        
        elif type=='MEDIC':
            return str(consultorio.ConsultarMedico(key))
        
        elif type=='PATIENT':
            return str(consultorio.ConsultarPaciente(key))

    except ClinicException as CE:
        raise ServerException(2,'The clinic sayed: ',CE)

def dispatch(patient:list[str]):
    '''O MÉTODO INSERE UM PACIENTE NO CONSULTORIO 
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [DISPATCH] [CPF/NOME COMPLETO/ESPECIALIDADE/GRAVIDADE]
    '''
    try:
        nome=patient[0].split('#')
        nome=' '.join(nome)
        
        consultorio.inserirPaciente(nome,patient[1],patient[2],patient[3])
    
    except ClinicException as CE:
        raise ServerException(2,'The clinic sayed: ',CE)
        

def dispatchAll(pacientes:list[list[str]]):
    '''O MÉTODO INSERE VÁRIOS PACIENTES NO CONSULTORIO 
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [DISPATCHALL] [LISTA[CPF/NOME COMPLETO/ESPECIALIDADE/GRAVIDADE]]
    ''' 
    try:
        for i in range(len(pacientes)):
            
            patient= pacientes[i]
            nome=patient[0].split('#')
            nome=' '.join(nome)
            
            consultorio.inserirPaciente(nome,patient[1],patient[2],patient[3])
            
    except ClinicException as CE:
        raise ServerException(2,'The clinic sayed: ',CE)
    

def removePatient(cpf):
    '''O MÉTODO REMOVE UM PACIENTE DO CONSULTORIO 
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [REMOVE] [CPF]
    ''' 
    
    try:
        consultorio.removerPaciente(cpf)
    
    except ClinicException as CE:
        raise ServerException(2,'The clinic sayed: ',CE)
    
#== == == == Variáveis
MethodsServerDict={
    'INFORM':1, #Retorna informações sobre o consultório  
    
    'DISPATCH':2, #Adiciona um novo paciente ao consultório
    'DISPATCHALL':3, #Adiciona todos os pacientes 
    'REMOVEPATIENT':4, #Remove um paciente do consultorio
    
    'HIREMEDIC':5, #Adiciona um novo Medico ao consultório
    'FIREMEDIC':6, #Remove um Medico do consultório
    
    'NEWSPECIALITY':7, #Adiciona uma nova Especialidade ao consultório
}

#== == == Objetos
consultorio= Consultorio() # objeto do consultório
consultorio.inserirEspecilidade('Clinica Geral')
consultorio.inserirEspecilidade('Pediatria')
consultorio.inserirEspecilidade('Oftalmologia')
consultorio.inserirEspecilidade('Psiquiatria')
consultorio.inserirEspecilidade('Cirurgia Geral')
consultorio.inserirEspecilidade('Otorrinolaringologia')
consultorio.inserirEspecilidade('Endocrinologia')

consultorio.inserirMedico("Francis Bacon","Pediatria")
consultorio.inserirMedico("Alfandegario Nobrega","Psiquiatria")
consultorio.inserirMedico("Antony Nunes","Pediatria")
consultorio.inserirMedico("Luiz Chaves","Pediatria")
consultorio.inserirMedico("Jair Messias Bolsonaro","Psiquiatria")
consultorio.inserirMedico("Luís Inácio Lula","Endocrinologia")
consultorio.inserirMedico("Gustavo Wagner","Otorrinolaringologia")

#== == == Socket Parte
HOST = 'localhost' #o Host gerado automaticamente
PORT = 5000 #A porta que será usada
serverConection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # O socket está sendo criado
serverConection.bind((HOST, PORT)) #Ele está ouvindo no HOST e PORT pré-definidos


while True:
    msg, cliente = serverConection.recvfrom(1024)
    msg=msg.decode()
    print('=='*30)
    print ('Message from:', cliente)
    print('he sayed: ', msg)
    print('=='*30)
    print(ExecMessage(msg,cliente))#envia para o método que irá tratar a mensagem enviada pelo cliente
serverConection.close()