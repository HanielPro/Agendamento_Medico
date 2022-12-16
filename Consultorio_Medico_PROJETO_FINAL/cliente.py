from SalaRecepcao import SalaRecepcao
import socket
from  time import sleep
import os 
#from Menus import *

def MostrarDicionario(dicionario:dict,dictionaryKeys:list[str]):
    for i in range(len(dictionaryKeys)):
        print(f'\n[{dictionaryKeys[i]:^5}] => {dicionario.get(dictionaryKeys[i]):^5} ')


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#== ==Referente a execução das escolhas do usuário

class MenuException(Exception):
    def __init__(self,code, msg) -> None:
        '''0: o usuário digitou algo fora da escolha.'''
        super().__init__(f'Menu Exception {code}: ', msg)

def ReceptionPage(choice):
    clearConsole()
    
    if choice=='1': #'1': 'SHOW THE AWAITING LIST',
        print('Showning Reception....')
        print(Reception)
        return True
                    
    elif choice=='2':#'2':'ADD A PATIENT INTO THE AWAITING LIST',
        print('Adding a new Patient....')

        cpf=input('Insert him CPF=>  ')
        name=str.upper(input('Insert him name=>  ') )
        speciality=str.upper(input('Insert him ndesired speciality=>  ') )
        gravity=str.upper(input('Insert him gravity=>  ') )
        
        print(f'\n CPF: {cpf} \n Name: {name}\nDesired specialty: {speciality} \n Gravity: {gravity}\n')
        
        confirmacao=str.upper(input('Confirm? (Y)  '))
        if confirmacao=='Y':
            Reception.ListarPaciente(cpf,name,speciality,gravity)
            return True
        
    
    elif choice=='3':#'3':'REMOVE A PATIENT OF THE AWAITING LIST'
        print(Reception)
        print('Removing a Patient....')
        cpf=input('Insert him CPF=>  ')
        
        print(f'\n CPF: {cpf}\n')
        confirmacao=str.upper(input('Confirm? (Y)  '))
        if confirmacao=='Y':   
            Reception.removerPaciente(cpf)
            return True
        
    elif choice=='4':#'4':'REMOVE ALL PATIENT OF THE AWAITING LIST'
        print('Removing All Patient....')
        
        confirmacao=str.upper(input('Confirm? (Y)  '))
        if confirmacao=='Y':   
            Reception.removerTodosPacientes(cpf)
            return True
        
    elif choice=='5':#'5':'SHOW A PATIENT',
        print(Reception)
        print('Showning a Patient....')
        cpf=input('Insert him CPF=>  ')
        
        print(f'\n CPF: {cpf}\n')
        confirmacao=str.upper(input('Confirm? (Y)  '))
        if confirmacao=='Y':   
            print(Reception.consultarPaciente(cpf))
            return True
        
    elif choice=='-': #'-':'..'
        print('Quiting of Recption Menu....')
        return False
    
    else:
        raise MenuException(0,'What did u say?! ')
    
    print('option not realized...') #usuário desistiu da operação
    return True

                

def PrincipalPage(choice)->bool:

    global cursor
    
    principalFlag=True
    while principalFlag:
        if choice=='-':
            clearConsole()
            print('Bye! Thank you for to use our code :)')
            return False
        
        elif choice=='1':
            choice=''
            receptionFlag=True
            while receptionFlag:
                
                clearConsole()
                print(separador)
                print(f'{separador1}Reception Page{separador2}')
                print(separador)
                
                MostrarDicionario(ReceptionDict,ReceptionDictKeys)
                receptionFlag=ReceptionPage(input(cursor))
                if receptionFlag==True:
                    input('Sucess!')

        elif choice=='2':#======= para implementar
            choice=''
            receptionFlag=True
            while receptionFlag:
                
                clearConsole()
                print(separador)
                print(f'{separador1}Consultory Manual{separador2}')
                print(separador)
    
                MostrarDicionario(ConsultoryManuDict,ConsultoryManuKeys)
                receptionFlag=ReceptionPage(input(cursor))
                if receptionFlag==True:
                    input('Sucess!')
        elif choice=='3':
            choice=''
            receptionFlag=True
            while receptionFlag:
                
                clearConsole()
                print(separador)
                print(f'{separador1}Consultory Bash Manual{separador2}')
                print(separador)
    
                MostrarDicionario(ConsultoryManuDict,ConsultoryManuKeys)
                receptionFlag=ReceptionPage(input(cursor))
                if receptionFlag==True:
                    input('Sucess!')
        
        else:
            raise MenuException(0,'What did you say')
                

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

#== == == Varíavel qualquer
separador='=='*30
separador1='=-'*15
separador2='-='*15
cursor='\ntype =>  '

flag=True
while flag:
    #-- -- -- ao logar ou sair de um dos menus, o usuário irá para a página Principal
    try:
        print(f'{separador1}Principal Page{separador2}')
        print(separador)
        MostrarDicionario(PrincipalDict,PrincipalDictKeys)
        
        flag=PrincipalPage(PrincipalPage(input(cursor)))
        
        #-- -- -- Reception Page option
                    
    except MenuException as ME:
        print(ME)