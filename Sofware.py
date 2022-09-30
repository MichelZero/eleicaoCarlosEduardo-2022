# Prova de POO
# Equipe: [
# Maria Clara Lourenço de Lira,
# Maria Karoliny Oliveira da Costa,
# Carlos Eduardo OLiveira Lopes,
# Lucas Nóbrega,
# Lucas Mateus Macedo Amorim,
# Isadora Pereira Maciel
# ]

# Importando Classes e bibliotecas
from time import sleep as congelar
from Canditado import Candidato 
from Voto import Voto
from Eleicao import Eleicao

# Instanciando cada classe
Cdt = Candidato()
Vt = Voto()

# Definindo o banco de dados xD, onde serão armazenados as informações
dicionario_candidatos = dict()
dicionario_votos = dict()

# Criando o software
while True:
    print("""
|-=-=-=-=-=-=-Menu-=-=-=-=-=-=-|
|                              |
| 1 - Cadastrar Candidato      |
| 2 - Votar                    |
| 3 - Ver Candidatos           |
| 4 - Contagem de Votos        |
| 5 - Sair da Urna             |
|                              |
|-=-=-=-=-=-=-=--=-=-=-=-=-=-=-| """)

    opcao = input('\nInforme a opção: ')

    if opcao == '1':
        print("""
|-=-=-=Menu de Candidatos=-=-=-|
|                              |
| 1 - Descrever as informações |
| 2 - Voltar ao menu principal |
|                              |
|-=-=-=-=-=-=-=--=-=-=-=-=-=-=-| """)
        
        opcao = input('\nInforme a opção: ')

        if opcao == '1':
            Cdt.Cadastrar_Candidato(
                str(input("\nInforme o nome do canditado: ")),
                str(input(f"Informe o nome do partido: ")),
                int(input(f"Informe o número: ")) 
                )
            
            if Cdt.num in dicionario_candidatos.keys():
                print('\nJá existe um candidato com este mesmo número!!!')
                continue

            else:
                dicionario_candidatos.update(Cdt.dicionariocandidato)

                print(f'\nDados de {Cdt.nome} cadastrados no banco de dados!')
                print(f'\nVoltando para o menu principal...')

                congelar(2)
        
        elif opcao == '2':
            continue

        else:
            print('\nOpção inválida')
            continue

    elif opcao == '2':
        if len(dicionario_candidatos.keys()) == 0:
            print('\nAinda não temos candidatos cadastrados :(')
            continue

        else:
            
            Vt.Votar(
                str(input(f"\nInforme o seu cpf: ")),
                int(input(f"Informe o número do seu candidato: "))
                )

            if Vt.numCandidato not in dicionario_candidatos.keys():
                print('\nSeu voto foi anulado porque não existe este canditado cadastrado')
                Vt.registrarcadastro(anular=True)

            if Vt.cpf in dicionario_votos.keys():
                print('\nVocê já votou nessa Urna :^')
                continue
            
            else:
                dicionario_votos.update(Vt.dicionariovoto)
                print(f'\nCpf: {Vt.cpf} seu voto foi cadastrado com sucesso!')
    
    elif opcao == '3':
        if len(dicionario_candidatos.keys()) == 0:
            print('\nAinda não temos candidatos cadastrados :(')
            continue
        
        else:
            print('\nLista de candidatos disponíveis\n')
            for numero, dado in dicionario_candidatos.items():
                print(f'| Nome: {dado[0]} | Partido: {dado[1]} | Número: {numero}')

    elif opcao == '4':
        if len(dicionario_votos.keys()) == 0:
            print('\nNingúem votou ainda :(')
            continue
        
        else:
            print()
            Ec = Eleicao(dicionario_votos, dicionario_candidatos)
            Ec.contagemvotos()

    elif opcao == '5':
        print('\nFim da votação, volte sempre :)')
        break

    else:
        print('\nNão existe essa opção no menu :v')
        continue