import os 

def mostrarDicionario(dicionario:dict)->str:
    '''Recebe um dicionário e um array com chaves para poder mostrar na tela as chaves e os seus valores'''
    
    dicionarioChaves=list(dicionario.keys())
    s=''
    for i in dicionarioChaves:
        s+= f'{i :^5}=> {dicionario[i]:^5} \n'
    return s
        
def clearConsole():
    '''Comando para Limpar o terminal'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
