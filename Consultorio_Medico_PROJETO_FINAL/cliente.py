from SalaRecepcao import SalaRecepcao
import socket
from  time import sleep
import os 


def MostrarDicionario(dicionario:dict,dictionaryKeys:list[str]):
    for i in range(len(dictionaryKeys)):
        print(f'\n[{dictionaryKeys[i]:^5}] => {dicionario.get(dictionaryKeys[i]):^5} ')


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


PrincipalDict={
    '1': 'GO TO RECEPTION MENU',
    '2':'GO TO CONSULTORY MENU',
    '3':'CONSULTORY METHOD MANU',
    '-':'..',
}

PrincipalDictKeys= list(PrincipalDict.keys())

ReceptionDict={
    '1': 'SHOW THE AWAITING LIST',
    '2':'ADD A PATIENT INTO THE AWAITING LIST',
    '3':'REMOVE A PATIENT OF THE AWAITING LIST',
    '4':'REMOVE ALL PATIENT OF THE AWAITING LIST',
    '5':'SHOW A PATIENT',
    '-':'..',
}

ReceptionDictKeys= list(ReceptionDict.keys())

ConsultoryManuDict={
    'INFORM':'[INFORM] "SPECIALITY, MEDIC, PATIENT, DEFAULT=CLINIC" |USE TO GET INFORMATION OF THE CONSULTORY|',
    
    'DISPATCH':'[SEND] [PATIENT.CPF] |USE TO SEND ONE PATIENT OF THE AWAITING LIST TO THE CONSULTORY|',
    'DISPATCHALL':'[SENDALL] |USE TO SEND ALL PATIENTS ON THE AWAITHING LIST TO THE CONSULTORY|',
    
    'REMOVE':'[REMOVE] [PATIENT.CPF] |USE TO REMOVE ONE PATIENT OF THE CLINIC|',
    'SENDALL':'[SENDALL] |USE TO SEND ALL PATIENTS ON THE AWAITHING LIST TO THE CONSULTORY|',
    
    'QUIT': '[QUIT] |USE FOR QUIT OF THE CONSULTORY PROMPT|',
    '{-}':'..',
}

ConsultoryManuKeys= list(ConsultoryManuDict.keys())
#== == == == inicialização do lado do cliente

#== == ==Classe Sala Recepção

Reception=SalaRecepcao()

#== == == SOCKET
HOST = 'localhost'
PORT = 5000
conect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

separador='=='*30
separador1='=-'*15
separador2='-='*15

while True:
    #-- -- -- ao logar ou sair de um dos menus, o usuário irá para a página Principal
    try:
        print(f'{separador1}Principal Page{separador2}')
        print(separador)
        MostrarDicionario(PrincipalDict,PrincipalDictKeys)
        
        MenuOption=input('type => ')
        #-- -- Quit option
        if MenuOption=='-':
            clearConsole()
            print('Bye! Thank you for to use our code :)')
            break
        #-- -- -- Reception Page option
        elif MenuOption=='1':
            
            while True:
                clearConsole()
                userChoice=''
                try:
                    print(separador)
                    print(f'{separador1}Reception Page{separador2}')
                    print(separador)
                    MostrarDicionario(ReceptionDict,ReceptionDictKeys)
                    userChoice=input('type => ')

                    if userChoice=='1': #'1': 'SHOW THE AWAITING LIST',
                        print('Showning Reception....')
                        print(Reception)
                    
                    elif userChoice=='2':#'2':'ADD A PATIENT INTO THE AWAITING LIST',
                        print('Adding a new Patient....')
                        
                        cpf=input('Insert him CPF=>  ')
                        name=str.upper(input('Insert him name=>  ') )
                        speciality=str.upper(input('Insert him speciality=>  ') )
                        gravity=str.upper(input('Insert him gravity=>  ') )
                        
                        Reception.ListarPaciente(cpf,name,speciality,gravity)
                        
                    
                    elif userChoice=='3':#'3':'REMOVE A PATIENT OF THE AWAITING LIST'

                        print('Removing a Patient....')
                    
                        cpf=input('Insert him CPF=>  ')
                        Reception.removerPaciente(cpf)
                        
                    elif userChoice=='4':#'4':'REMOVE ALL PATIENT OF THE AWAITING LIST'
                        print('Removing All Patient....')
                        Reception.removerTodosPacientes()
                        
                    elif userChoice=='5':#'5':'SHOW A PATIENT',
                        print('Showning a Patient....')
                        cpf=input('Insert him CPF=>  ')
                        print(Reception.consultarPaciente(cpf))
                        
                    elif MenuOption=='-':#'-':'..'
                        clearConsole()
                        print('Quiting of Recption Menu....')
                        break
                    
                    else:
                        print('What did you say ?!')
                    
                    input('Press Enter for continue.... ')
                    sleep(3)

                except Exception as E:
                    print(E)
                    input('Press Enter for continue.... ')
                    
            sleep(3)
    except Exception:
        pass