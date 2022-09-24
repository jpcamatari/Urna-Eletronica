from DAO import *

print("****Urna Eletronica***")
escolha = int(input('Escolha uma opção:\n'
    '1-VOTAR\n'
    '2-ADMIN '))

if escolha == 1:
    Votar.votarVereador(input('Escolha o numero do candidato a Vereador:'))
    Votar.votarPrefeito(input('Escolha o numero do candidato a Prefeito:'))
    print('Voto Contabilizado com Sucesso')

elif escolha == 2:
    cadastro = int(input('Escolha qual quandidado deseja cadastrar:\n'
                        '1- Cadastrar Vereador\n'
                        '2- Cadastrar Prefeito\n'
                        '3- Contagem de Votos Vereador\n'
                        '4- Contagem de Votos Prefeito '))
    if cadastro == 1:
        Admin.cadastrarVereador(input('Nome do Candidato:'), input('Numero do Candidato:'))
    elif cadastro == 2:
        Admin.cadastrarPrefeito(input('Nome do Candidato:'), input('Numero do Candidato:'))
    elif cadastro == 3:
        Admin.mostrarVotosVeri()
    elif cadastro == 4:
        Admin.mostrarVotosPref()
    else:
        print('Opção Invalida')

else:
    print('Opção Invalida')