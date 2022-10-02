# Prova de POO
# Equipe: [
# Maria Clara Lourenço de Lira,
# Maria Karoliny Oliveira da Costa,
# Carlos Eduardo OLiveira Lopes,
# Lucas Nóbrega,
# Lucas Mateus Macedo Amorim,
# Isadora Pereira Maciel
# ]

class Candidato:
    def Cadastrar_Candidato(self, nome : str, partido : str, NumCandidato : int):    
        self.nome = nome
        self.partido = partido
        self.num = NumCandidato

        self.dicionariocandidato = {self.num : [self.nome, self.partido]}