import datetime

class Voto:
    def Votar(self, cpf, numCandidato):
        self.cpf = cpf
        self.numCandidato = numCandidato
        self.horarioVoto = datetime.datetime.now()
        self.registrarcadastro()

    def registrarcadastro(self, anular = False):
            if anular == False:
                self.dicionariovoto = {self.cpf : [self.numCandidato, self.horarioVoto.strftime('%H:%M:%S, %d/%m/%y')]}
            
            else:
                self.dicionariovoto = {self.cpf : self.horarioVoto.strftime('%H:%M:%S, %d/%m/%y')}
            
            return self.dicionariovoto