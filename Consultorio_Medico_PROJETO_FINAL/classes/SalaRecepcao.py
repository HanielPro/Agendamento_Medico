from EstruturasDeDados.Lista.ListaEncadeada import *
from Paciente import Paciente
#from Consultorio import Consultorio,ClinicException,consultorio1

class SalaRecepcao():
    
    def __init__(self):
        self.__listaAguardo= Lista()
        #self.__consultorio= consultorio
    
    def __str__(self) -> str:
        return str(self.__listaAguardo)
    
    #== == Esta função insere o paciente na lista de aguardo da Sala de Recepção
    def ListarPaciente(self,cpf:str, nome:str, especialidadeDesejada:str, gravidade:str)-> None:
        newPaciente=Paciente(cpf,nome,especialidadeDesejada,gravidade)
        posicao=self.__checarPosicaoPorGravidade(newPaciente,1) # a posição é gerada a partir de uma busca na lista pela menor prioridade
        
        self.__listaAguardo.inserir(cpf,newPaciente,posicao) 
    
    #== == Este método deverá retornar a posição da lista de aguardo o paciente deverá ser inserido. O índice é gerado a partir da gravidade do tal.
    #-- -- Na dúvida, cheque o dicionário de gravidades do cliente
    
    def __checarPosicaoPorGravidade(self,paciente:Paciente,posicaoAtual:int) -> int:
        '''
        Melhor Caso é quando a lista vazia ou a primeira posição é a certa: O(1)
        Maior parte dos caso quando a resposta está no meio da lista: O(N)
        Pior caso é quando a resposta está no final da lista: O(N)
        '''
        if self.__listaAguardo.tamanho()< posicaoAtual : # Caso a lista esteja vazia, ou caso tenha chegado no final desta.
            return posicaoAtual
        
        pacienteAlocado= self.__listaAguardo.elemento(posicaoAtual)
        if paciente > pacienteAlocado :# Checa se o paciente tem mais prioridade que o que já está na lista 
            return posicaoAtual
        
        return self.__checarPosicaoPorGravidade(paciente, posicaoAtual + 1) # caso a prioridade do paciente seja igual ou menor que o tal, ele irá tentar inserir depois deste.

    #== == Esta função remove permanentemente o paciente da lista de aguardo da Sala de Recepção    
    def removerPaciente(self,cpf:str)->str:
        '''Remove um único paciente da lista de aguardo'''
        self.__listaAguardo.remover(self.__listaAguardo.busca(cpf))
        return '+OK PATIENT REMOVED'
    
    
    #== == Esta função remove permanentemente o paciente da lista de aguardo da Sala de Recepção    
    def consultarPaciente(self,cpf:str)->str:
        '''Obtem a informação de um paciente através de seu cpf'''
        posicao=self.__listaAguardo.busca(cpf)
        
        paciente=self.__listaAguardo.elemento(posicao)
    
        return str(paciente)
    
    #== == Esta função remove permanentemente Todos os pacientes da lista de aguardo da Sala de Recepção
    def removerTodosPacientes(self):
        ''' Remove todos os pacientes da lista de aguardo'''
        self.__listaAguardo.esvazia()
    
    #== == Esta função envia um paciente da lista de aguardo da Sala de Recepção para o consultório
    
    def despacharPaciente(self,cpf:str)->str:
        '''Envia um único paciente da lista de aguardo para o consultório'''
        
            #self.__consultorio.inserirPaciente(pacienteDespacho) #seria interessante enviar o objeto diretamente para o consultório ao invés de enviar os atributos.
            #self.__consultorio.inserirPaciente(pacienteDespacho.cpf,pacienteDespacho.nome, pacienteDespacho.especialidadeDesejada, pacienteDespacho.stringuificarGravidade())
        
        pacienteDespacho=self.__listaAguardo.remover(self.__listaAguardo.busca(cpf))
        
        nome=pacienteDespacho.nome.split()
        nome='#'.join(nome)
        return f'{pacienteDespacho.cpf}/{nome}/{pacienteDespacho.especialidadeDesejada}/{pacienteDespacho.stringuificarGravidade()}'
            
        '''
        except ClinicException as CE:
            return f'-ERR: OCURRIED THIS ERROR: {CE}'
        '''
    
    #== == Esta função envia todos os pacientes da lista de aguardo da Sala de Recepção para o consultório
    def despacharTodosPacientes(self)->str:
        '''Retorna uma lista contendo todos os pacientes da lista de aguardo'''

        todosPacienteParaDespachar=[]
        while not(self.__listaAguardo.estaVazia()):
            
            pacienteParaDespachar=self.__listaAguardo.elemento(1)
            
            pacienteParaDespachar=self.despacharPaciente(pacienteParaDespachar.cpf)
            
            todosPacienteParaDespachar.append(pacienteParaDespachar)
        
        return ' '.join(todosPacienteParaDespachar)

    
    # !! !! !! !! Esses métodos estão dentro da Sala de espera mas não deveriam está aqui.
    def consultarConsutorio(self):
        return str(self.__consultorio)

    
if __name__=='__main__':

    sala1=SalaRecepcao()
    sala1.ListarPaciente("34823019705","Joaseiro da Costa","Pediatria","L2")
    sala1.ListarPaciente("56567424223","Pedro Neto SIlveira","Psiquiatria","G")
    sala1.ListarPaciente("12321313323","Rogerio SIlveira","Pediatria","M2")
    sala1.ListarPaciente("12321313301","Paulo Florinopolis","Pediatria","G")
    sala1.ListarPaciente("12321313820","Paulo Cantando","Pediatria","G")
    sala1.ListarPaciente("12321313834","Paulo lanchando","Pediatria","L1")
    sala1.ListarPaciente("12321313853","Paulo bebendo","Pediatria","L1")
    sala1.ListarPaciente("12321313872","Paula Sorrino","Pediatria","L1")
    sala1.ListarPaciente("12321313651","Paulo Subindo","Psiquiatria","G")
    sala1.ListarPaciente("12321313303","Paulo Chorando","Pediatria","G")
    sala1.ListarPaciente("12321313356","Paula Equinó","Pediatria","L1")
    
    print(sala1)
    input()
    '''   
    sala1.removerPaciente('56567424223')
    print(sala1)
    input('removido o paciente 56567424223....')
    
    sala1.despacharPaciente('12321313356')
    print(sala1)
    input('despachado o paciente 12321313356....')

    sala1.removerTodosPacientes()
    print(sala1)
    input('removido todos pacientes....')
    '''
    print(sala1.despacharPaciente('12321313356'))
    print(sala1.despacharTodosPacientes())
    print(sala1)
    input('Mostrando as informações do consultório')

    #-- -- Testando o consultorio