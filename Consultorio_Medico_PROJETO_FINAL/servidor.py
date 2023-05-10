from classes.Hospital import Hospital, HospitalException

import socket
#import os
#from threading import Thread, Semaphore

class ServerException(Exception):

    def __init__(self, code:int, msg:str) -> None:
        '''
        0: Método não encontrado.
        1: O cliente escreveu o método certo, mas não inseriu os parametros adequado
        2: Ocorreu algum erro dentro do Hospital
        '''
        super().__init__(f'Server Exception {code}: \n', msg)
        
#== == == == Métodos
def translateCPF(cpf:str)->str:
    '''Este método serve para transforma o CPF contendo sinais e transforma em uma cadeia de números'''
        
    if len(cpf)>11: # Se for acima de 11 caractéres, removerá os pontos e hífens. 
        cpf=cpf.replace('-','')
        cpf=cpf.replace('.','')
    elif len(cpf) != 11:
        raise ServerException(1,'-ERR WRONG CPF ENTRY')
    return cpf

def ExecMessage(msg:str,cliente:str): 
    '''
    Ele receberá a mensagem do cliente e execultará  o método transcrito nela. 
    '''
    global serverConection
    try:
        response=''
        msg=msg.upper()
        msgTrunc=msg.split()
        method=MethodsServerDict[msgTrunc[0]]
        
        if method==1:                
                if len(msgTrunc)==1: #só o método inform
                    response=inform('CLINIC')
                else:
                    response=inform(msgTrunc[1])
                    
        elif method==2: #Dispatch [CPF/NAME#SUBNAME/SPECIALITY/GRAVITY]
            patient=msgTrunc[1].split('/')
            response= dispatch(patient)
        
        elif method==3:
            patients=msgTrunc[1:]  
            response=dispatchAll(patients)  
        
        elif method==4:#remover paciente
            response= removePatient(msgTrunc[1]) 
        
        serverConection.sendto(response.encode(),cliente)
        if method ==1:
            response=f'+OK FILE inform{msgTrunc[1]}.txt sent'
        return response
        
    except KeyError as KE:
        raise ServerException(0,'METHOD NOT FOUND')
    
def inform(type:str):
    '''O MÉTODO RETORNA AS INFORMAÇÕES DEPENDENDO DA EXIGÊNCIA DO USUÁRIO
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [METHOD] ?[WHOM]
    '''
    parametersList=['CLINIC','SPECIALITYS','MEDICS','PATIENTS']
    try:
        if type in parametersList:
            arquivo= open(f'inform{type}.txt','w')
        else:
            raise ServerException(2,f'-ERR THIS NOT THE RIGHT COMAND' )
        
        if type=='CLINIC':
            arquivo.write(str(Hospital))
            
        elif type=='SPECIALITYS':
            arquivo.write(str(Hospital.exibirEspecialidades()))
        
        elif type=='MEDICS':
            arquivo.write(str(Hospital.exibirMedicos()))
        
        elif type=='PATIENTS':
            arquivo.write(str(Hospital.exibirPacientes()))

        arquivo.close()
        dados_upload = ''

        arq=open(f'inform{type}.txt','r')
        for data in arq.readlines():
            dados_upload+=data
               
        arquivo.close()
        
        return dados_upload
    
    except HospitalException as HE:
        raise ServerException(2,f'-ERR THE CLINIC SAYED: \n {HE}' )

def dispatch(patient)->str:
    '''O MÉTODO INSERE UM PACIENTE NO Hospital 
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [DISPATCH] [CPF/NOME COMPLETO/ESPECIALIDADE/GRAVIDADE]
    '''
    try:
        nome=patient[1].split('#')
        nome=' '.join(nome)
        
        return Hospital.inserirPaciente(patient[0],nome,patient[2],patient[3])
        
    except HospitalException as HE:
        raise ServerException(2,'The clinic sayed: ',HE)
        
def dispatchAll(pacientes):
    '''O MÉTODO INSERE VÁRIOS PACIENTES NO Hospital 
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [DISPATCHALL] [LISTA[CPF/NOME COMPLETO/ESPECIALIDADE/GRAVIDADE]]
    ''' 
    try:
        for i in range(len(pacientes)):
            
            patient= pacientes[i]
            patient= patient.split('/')
            nome=patient[1].split('#')
            nome=' '.join(nome)
            
            Hospital.inserirPaciente(patient[0],nome,patient[2],patient[3])
        return '+Ok, all dispatched!'
        
    except HospitalException as HE:
        raise ServerException(2,'The clinic sayed: ',HE)

def removePatient(cpf):
    '''O MÉTODO REMOVE UM PACIENTE DO Hospital 
    \nO QUE SE ESPERA RECEBER DA MENSAGEM:
    [REMOVEPATIENT] [CPF]
    '''
    try:
        return Hospital.removerPaciente(cpf)
    
    except HospitalException as HE:
        raise ServerException(2,'The clinic sayed: ',HE)
    
#== == == == Variáveis
MethodsServerDict={
    'INFORM':1, #Retorna informações sobre o consultório  
    
    'DISPATCH':2, #Adiciona um novo paciente ao consultório
    'DISPATCHALL':3, #Adiciona todos os pacientes 
    'REMOVEPATIENT':4, #Remove um paciente do Hospital
    
    'HIREMEDIC':5, #Adiciona um novo Medico ao consultório
    'FIREMEDIC':6, #Remove um Medico do consultório
    
    'NEWSPECIALITY':7, #Adiciona uma nova Especialidade ao consultório
}

#== == == Objetos
Hospital= Hospital() # objeto do consultório
Hospital.inserirEspecilidade('Geral')
Hospital.inserirEspecilidade('Pediatria')
Hospital.inserirEspecilidade('Oftamologia')
Hospital.inserirEspecilidade('Psiquiatria')
Hospital.inserirEspecilidade('Cirurgia')
Hospital.inserirEspecilidade('Otorrinolaringologia')
Hospital.inserirEspecilidade('Endocrinologia')

Hospital.inserirMedico("Francis Bacon","Pediatria")
Hospital.inserirMedico("Alfandegario Nobrega","Psiquiatria")
Hospital.inserirMedico("Antony Nunes","Pediatria")
Hospital.inserirMedico("Luiz Chaves","Pediatria")
Hospital.inserirMedico("JOÃO MACHADO","OFTAMOLOGIA")
Hospital.inserirMedico("Jair Messias Bolsonaro","Psiquiatria")
Hospital.inserirMedico("Luís Inácio Lula","Endocrinologia")
Hospital.inserirMedico("Gustavo Wagner","Otorrinolaringologia")

#== == == Socket Parte
HOST = '0.0.0.0' #o Host gerado automaticamente
PORT = 5000 #A porta que será usada
serverConection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # O socket está sendo criado
serverConection.bind((HOST, PORT)) #Ele está ouvindo no HOST e PORT pré-definidos


while True:
    msg, cliente = serverConection.recvfrom(8092)
    msg=msg.decode()
    print('=='*30)
    print ('Message from:', cliente)
    print('he sayed: ', msg)
    print('=='*30)
    try:
        print(ExecMessage(msg,cliente))#envia para o método que irá tratar a mensagem enviada pelo cliente

    except ServerException as SE:
        serverConection.sendto( str(SE).encode(), cliente)
        
    except KeyboardInterrupt:
        break
     
    except Exception as E:
        serverConection.sendto( f'this error ocurried: \n{E} '.encode(), cliente)
        
serverConection.close()