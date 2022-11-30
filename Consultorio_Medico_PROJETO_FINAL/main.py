from Medico import *
from Paciente import *
from Especialidade import *
from Consultorio import *

consultorio=Consultorio()
consultorio.inserirEspecilidade('Clinica Geral')
consultorio.inserirEspecilidade('Pediatria')
consultorio.inserirEspecilidade('Oftalmologia')
consultorio.inserirEspecilidade('Psiquiatria')
consultorio.inserirEspecilidade('Cirurgia Geral')

consultorio.inserirMedico("Francis Bacon","Pediatria",90)
consultorio.inserirMedico("Alfandegario Nobrega","Psiquiatria",40)
consultorio.inserirMedico("Antony Nunes","Pediatria",60)
consultorio.inserirPaciente("12345678943","Adesbosdaldo Neto SIlveira","Pediatria","Grave")
consultorio.inserirPaciente("92839823145","FElipe Texeiraa sad","Pediatria","Grave")
consultorio.inserirPaciente("99999999999","DEBochildo CAstnharie","Genecologista","Grave")
consultorio.inserirPaciente("94759372850","Uagabugasa Costa","Pediatria","Grave")
consultorio.inserirPaciente("56567424223","Pedro Neto SIlveira","Psiquiatria","Grave")
consultorio.inserirPaciente("12321313323","Rogerio SIlveira","Pediatria","Grave")
consultorio.inserirPaciente("99999999999","Rogerio SIlveira","Pediatria","Grave")
consultorio.inserirPaciente("12321313353","Paulo Florinopolis","Pediatria","Grave")
print('Medicos:')
consultorio.ExibirMedicos()
print('Pacientes:')
consultorio.ExibirPacientes()
def everyonehasfired():
    demitido=input("Digite o ID do médico que será excluído:\n")
    consultorio.RemoverMedico(demitido)
    consultorio.ExibirMedicos()
while True:
    print('1-para remocer medico\n2-para remover paciente')
    x=int(input(''))
    if x ==1:
        demitido=input("Digite o ID do médico que será excluído:\n")
        consultorio.RemoverMedico(demitido)
        consultorio.ExibirMedicos()
    elif x==2:
        morto=input("Digite o CPF que será cancelado:\n")
        consultorio.RemoverPaciente(morto)
        consultorio.ExibirPacientes()