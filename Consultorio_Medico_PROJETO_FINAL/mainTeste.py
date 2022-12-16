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

consultorio.inserirMedico("Francis Bacon","Pediatria")
consultorio.inserirMedico("Alfandegario Nobrega","Psiquiatria")
consultorio.inserirMedico("Antony Nunes","Pediatria")
consultorio.inserirPaciente("12345678943","Adesbosdaldo Neto SIlveira","Pediatria","G")
consultorio.inserirPaciente("92839823145","FElipe Texeiraa sad","Pediatria","G")
#consultorio.inserirPaciente("99999999999","DEBochildo CAstnharie","Genecologista","G")
#consultorio.inserirPaciente("99999999999","Rogerio SIlveira","Pediatria","G")
consultorio.inserirPaciente("56567424227","Uagabugasa Costa","Pediatria","G")
consultorio.inserirPaciente("56567424223","Pedro Neto SIlveira","Psiquiatria","G")
consultorio.inserirPaciente("12321313323","Rogerio SIlveira","Pediatria","G")
consultorio.inserirPaciente("12321313353","Paulo Florinopolis","Pediatria","G")
consultorio.inserirPaciente("12321313356","Paula Equinó","Pediatria","G")
consultorio.inserirPaciente("12321349586","Jácinto Pinto","Pediatria","G")

print('Medicos:')
print(consultorio.exibirMedicos())

print('Pacientes:')
print(consultorio.exibirPacientes())

def everyonehasfired():
    demitido=input("Digite o ID do médico que será excluído:\n")
    consultorio.RemoverMedico(demitido)
    print(consultorio.exibirMedicos())

while True:
    print('1-para remocer medico\n2-para remover paciente')

    x=int(input(''))

    if x ==1:
        demitido=input("Digite o ID do médico que será excluído:\n")
        consultorio.RemoverMedico(demitido)
        print(consultorio.exibirMedicos())

    elif x==2:
        morto=input("Digite o CPF que será cancelado:\n")
        #morto='92839823145'
        consultorio.removerPaciente(morto)
        print(consultorio.exibirPacientes())