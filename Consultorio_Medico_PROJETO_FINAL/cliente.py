from classes.SalaRecepcao import SalaRecepcao, ReceptionException
import socket
import os 

def MostrarDicionario(dicionario:dict,dictionaryKeys):
    '''Recebe um dicionário e um array com chaves para poder mostrar na tela as chaves e os seus valores'''
    for i in range(len(dictionaryKeys)):
        print(f'\n[{dictionaryKeys[i]:^10}] => {dicionario.get(dictionaryKeys[i]):^10}')

def clearConsole():
    '''Comando para Limpar o terminal'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#== ==Referente a execução das escolhas do usuário

#== Caso o usuário Digite uma escolha indevida
class TerminalException(Exception):
    def __init__(self,code, msg) -> None:
        '''
        0: o usuário digitou algo fora da escolha.
        1: o usuário digitou um comando inexiste ou errado.
        '''
        super().__init__(f'Terminal Exception {code}: {msg}')

#== demonstra as interações que o usuário pode fazer
def ReceptionPage(choice):
    clearConsole()
    try:
        if choice=='1': #'1': 'SHOW THE AWAITING LIST',
            print('Showning ReceptionRoom....')
            print(ReceptionRoom)
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
                ReceptionRoom.ListarPaciente(cpf,name,speciality,gravity)
                return True
        
        elif choice=='3':#'3':'REMOVE A PATIENT OF THE AWAITING LIST'
            print(ReceptionRoom)
            print('Removing a Patient....')
            cpf=input('Insert him CPF=>  ')
            
            print(f'\n CPF: {cpf}\n')
            confirmacao=str.upper(input('Confirm? (Y)  '))
            if confirmacao=='Y':   
                ReceptionRoom.removerPaciente(cpf)
                return True
            
        elif choice=='4':#'4':'REMOVE ALL PATIENT OF THE AWAITING LIST'
            print('Removing All Patient....')
            
            confirmacao=str.upper(input('Confirm? (Y)  '))
            if confirmacao=='Y':   
                ReceptionRoom.removerTodosPacientes()
                return True
            
        elif choice=='5':#'5':'SHOW A PATIENT',
            print(ReceptionRoom)
            print('Showning a Patient....')
            cpf=input('Insert him CPF=>  ')
            
            print(f'\n CPF: {cpf}\n')
            confirmacao=str.upper(input('Confirm? (Y)  '))
            if confirmacao=='Y':   
                print(ReceptionRoom.consultarPaciente(cpf))
                return True
        elif choice=='-': #'-':'..'
            print('Quiting of Recption Menu....')
            return False
        
        else:
            raise TerminalException(0,'What did u say?! ')
        
        #print(f'{separador}\nSucess!')
        
    except TerminalException as ME:
        print(ME)
    except ReceptionException as RE:
        print(RE)
        
    print('option not realized...') #usuário desistiu da operação
    return True

def PrincipalPage()->bool:
    '''Aqui onde ocorre as primeiras ecolhas do usuário.'''
    global cursor,dest,conect
    
    while True:
        choice=input(cursor)
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
                    input(f'\n {separador1} Press Enter {separador2}\n')

        elif choice=='2':#======Terminal entre consultorio e recepção
            clearConsole()
            ConsultoryBash()
            input()

        elif choice=='3':#=======Manual
            choice=''
                
            clearConsole()
            print(separador)
            print(f'{separador1}Consultory Manual{separador2}')
            print(separador)

            MostrarDicionario(ConsultoryManuDict,ConsultoryManuKeys)
            input(cursor)
            clearConsole()
             
        else:
            clearConsole()
            raise TerminalException(0,'What did you say?! ')

def ConsultoryBash():
    cursor='\n$=> '
    while True:    
        try:
            comand=str.upper(input(cursor))
            comand=comand.split()
            
            if comand[0]=='QUIT':
                '''Example> QUIT'''
                return
            
            elif comand[0]=='HOWISME':
                '''Example> WHOISME'''
                print(ReceptionRoom)
            
            elif comand[0]=='MANU':
                '''Example> MANU'''
                MostrarDicionario(ConsultoryManuDict,ConsultoryManuKeys)
            
            elif comand[0]=='INFORM':
                '''Example> 
                INFORM ?[CLINIC], 
                INFORM [PATIENTS], 
                INFORM MEDICS,
                INFORM [SPECIALITYS]
                '''
                ServerConection(' '.join(comand))

            elif comand[0]=='DISPATCH':
                '''Example> DISPATCH [YYY.YYY.YYY-XX]'''
                patient=ReceptionRoom.despacharPaciente(comand[1]) # despachar retornar uma cadeia de caracteres
                comand[1]=patient
                #print(comand)
                ServerConection(' '.join(comand))

            
            elif comand[0]=='DISPATCHALL':
                '''Example> DISPATCHALL'''
                patients=ReceptionRoom.despacharTodosPacientes()
                comand.append(patients) #adiciona no final do comando uma lista contendo todos os pacientes
                print(comand)
                ServerConection(' '.join(comand))# aqui. deve-se enviar todos os pacientes para o consultório
            
            elif comand[0]=='REMOVEPATIENT':
                '''EXAMPLE> REMOVEPATIENT [YYY.YYY.YYY-XX]'''
                comand[1]=ReceptionRoom.translateCPF(comand[1]) # Ele irá transforma um cpf, em uma cadeia de dígitos
                ServerConection(' '.join(comand))
            
            else:
                raise TerminalException(1, f"SORRY, I DON'T RECOGNIZE THIS: {comand}")
        
        except ReceptionException as RE:
            print(RE)
        except TerminalException as TE:
            print(TE)
        except KeyboardInterrupt:
            clearConsole()
            break
        except IndexError:
            print(1, f"SORRY, I DON'T RECOGNIZE THIS: {comand}")

#== == == ==Variáveis
#== == Dicionarío com as escolhas
ConsultoryManuDict={
    'HOWISME': '[HOWISME] |USE TO GET THE INFORMATION OF HOW IS THE RECEPTION ROOM|',
    'MANU': '[MANU] |USE TO GET THE INFORMATION OF THE COMANDS|',
    
    'INFORM':'[INFORM] && [[SPECIALITYS] || [MEDICS] || [PATIENTS] || [CLINIC]=DEFAULT" |USE TO GET INFORMATION OF THE CONSULTORY|',
    
    'DISPATCH':'[DISPATCH] &&[PATIENT.CPF] |USE TO SEND ONE PATIENT OF THE AWAITING LIST TO THE CONSULTORY|',
    'DISPATCHALL':'[DISPATCHALL] |USE TO SEND ALL PATIENTS ON THE AWAITHING LIST TO THE CONSULTORY|',
    'REMOVEPATIENT':'[REMOVEPATIENT] && [PATIENT.CPF] |USE TO REMOVE ONE PATIENT OF THE CLINIC|',
    
    'QUIT': '[QUIT] |USE FOR QUIT OF THE CONSULTORY PROMPT|',
}
ConsultoryManuKeys= list(ConsultoryManuDict.keys())

PrincipalDict={
    '1': 'RECEPTION MENU',
    '2':'CONSULTORY BASH',
    '3':'CONSULTORY BASH MANU',
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

#== == == == inicialização do lado do cliente
#== == ==Classe Sala Recepção
ReceptionRoom=SalaRecepcao()
'''
#Exemplos pronto
'''
ReceptionRoom.ListarPaciente("34823019705","Joaseiro da Costa","Pediatria","L2")
ReceptionRoom.ListarPaciente("56567424223","Pedro Neto SIlveira","Psiquiatria","G")
ReceptionRoom.ListarPaciente("123.413.133-23","Rogerio SIlveira","Pediatria","M2")
ReceptionRoom.ListarPaciente("123.413.133-01","Paulo Florinopolis","Pediatria","G")
ReceptionRoom.ListarPaciente("153.783.108-20","Paulo Cantando","Otorrinolaringologia","G")
ReceptionRoom.ListarPaciente("123.413.138-34","Paulo lanchando","Otorrinolaringologia","L1")
ReceptionRoom.ListarPaciente("123.913.188-53","Paulo bebendo","Pediatria","L1")
ReceptionRoom.ListarPaciente("123.413.138-72","Paula Sorrino","Pediatria","L1")
ReceptionRoom.ListarPaciente("123.413.166-51","Paulo Subindo","Psiquiatria","G")
ReceptionRoom.ListarPaciente("123.415.123-03","Paulo Chorando","Pediatria","G")
ReceptionRoom.ListarPaciente("123.243.133-56","Paula Equinó","Pediatria","L1")

#== == == Varíavel qualquer
separador='=='*30
separador1='=-'*15
separador2='-='*15
cursor='\ntype =>  '


def ServerConection(msg:str):
    #== == == SOCKET
    HOST = 'localhost'
    PORT = 5000
    conect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    
    conect.sendto(msg.encode(),dest)
    response= conect.recvfrom(8092)
    
    if msg.split()[0]=='INFORM':
        arq=open('INFORM.txt','wb')
        tam_arquivo = len(response)
        while True:
            arq.write(response[0])
            tam_arquivo-= len(response)
            if tam_arquivo==0:break      
        arq.close()
                
    else:
        print(f"{'==='*30 :^20}")
        print(response)
        print(f"{'==='*30 :^20}")

flag=True
while flag:
    #-- -- -- ao logar ou sair de um dos menus, o usuário irá para a página Principal
    try:
        print(f'{separador1}Principal Page{separador2}')
        print(separador)
        MostrarDicionario(PrincipalDict,PrincipalDictKeys)
        
        flag=PrincipalPage()

        #-- -- -- Reception Page option
                    
    except TerminalException as ME:
        print(ME) 