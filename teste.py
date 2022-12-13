import random
from unicodedata import normalize #!! !! !! !! Precisa importar a biblioteca unide code:  $pip install unidecode

def gerarID(nome:str)-> str: # a função gera um id aleatório e confirma se n existe na estrutura de dados 5 vezes
    nome= nome.split()
    nome= ''.join(nome)
    id=''
    for i in range(5):
        id= trueGerarID(nome)
        break    
    return id
    
def trueGerarID(nome:str):
    tamanhoId=10
    idGerado=''
    finalValor=2
    
    for i in range(tamanhoId): # controla o tamanho do id    
            
        if i < 3:
            idGerado+= str.upper(nome[i])
                
        elif i > 7:
            idGerado+= str.upper( nome[-(finalValor)])
            finalValor-=1
            
        else: 
            idGerado+=str(chr(random.randrange(65, 90)))
    return idGerado

print(gerarID('Hániel Costá'))

print(normalize('NFC','áááááá´aáááá´aáaáá'))