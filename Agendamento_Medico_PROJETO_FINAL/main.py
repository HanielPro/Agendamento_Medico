from Medico import Medico
from Paciente import Paciente

cpf=input('Digite o CPF: ')
nome=input('Digite o Nome do paciente: ')
especialista=input('Digite o especialista que o paciente deseja: ')
tempoDaConsulta=int(input('Digite o tempo estimado da consulta: '))

p1=Paciente(cpf,nome,especialista)
print(p1)

nome=input('Digite o Nome do médico: ')
especialidade=input('Digite a especialidade do médico: ')
limite=int(input('Digite o tempo limite da fila de espera: '))
m1=Medico(nome,especialidade)
print(m1)