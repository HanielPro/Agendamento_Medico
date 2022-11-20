import filaEncadeadaNoCabeca

class HospitalException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
        

class Hospital:
    def __init__(self) -> None:
        self.MedicosLista=[]
    
    #Marca a consulta de um paciente com um médico específico
    #Desmarca uma ou várias consultas
    #Dá a vez ao paciente que chegou primeiro a vez da consulta
    