# Prova de POO
# Equipe: [
# Maria Clara Lourenço de Lira,
# Maria Karoliny Oliveira da Costa,
# Carlos Eduardo OLiveira Lopes,
# Lucas Nóbrega,
# Lucas Mateus Macedo Amorim,
# Isadora Pereira Maciel
# ]

class Eleicao:
    def __init__(self, dictvotos : dict, dictcandidatos):
        self.votos = dictvotos
        self.candidatos = dictcandidatos
        self.anulados = 0
        self.nums = list()
        self.resultadodigitalvotacao = dict()
    
    def contagemvotos(self):
        # Filtrando apenas os números dos candidatos
        for dado in self.votos.values():
            
            if type(dado) != list:
                self.anulados += 1
            
            else:
                self.nums.append(dado[0])
        
        # Eliminando as repetições dos números
        self.numsetado = set(self.candidatos.keys())

        # Agora sim fazendo a contagem dos votos
        for valor in self.numsetado:
            self.resultadodigitalvotacao[valor] = self.nums.count(valor)
        
        # Imprimindo os resultados
        for numero, votos in self.resultadodigitalvotacao.items():
            print(f'{self.candidatos[numero][0]} -- {votos} Votos')
        
        # Imprimindo os votos nulos, se houver
        print(f'Votos Nulos -- {self.anulados} Votos')