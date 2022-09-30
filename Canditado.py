class Candidato:
    def Cadastrar_Candidato(self, nome : str, partido : str, NumCandidato : int):    
        self.nome = nome
        self.partido = partido
        self.num = NumCandidato

        self.dicionariocandidato = {self.num : [self.nome, self.partido]}