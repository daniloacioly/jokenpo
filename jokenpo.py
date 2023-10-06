from random import randint
resposta = "s"
lista = [0, 1, 2]
itens = ('pedra', 'papel', 'tesousa')
maquina = randint(0, 2)
while resposta == 's' or resposta == 'S':
    print('=-=' * 11)
    print("Vamos jogar um jokenpô ?")
    print("Escolha entre uma das opções: \n"
                        "[0] Pedra \n"
                        "[1] Papel \n"
                        "[2] Tesoura")
    jogador = int(input("Qual a sua jogada ?: "))
    while jogador not in lista:
        jogador = int(input("Numero invalido, digite novamente: "))
    print(f'a maquina escolheu {(itens[maquina])}')
    print(f'o jogador escolheu {(itens[jogador])}')
    if maquina == 0: #pedra#
        if jogador == 0:
             print("Foi um Empate")
        elif jogador == 1:
            print("O Jogador venceu")
        elif jogador == 2:
            print('O Jogador perdeu')
        else:
            print('Resposta invalida')
    if maquina == 1: #papel#
        if jogador == 0:
            print('O jogador perdeu')
        elif jogador == 1:
            print('Foi um Empate')
        elif jogador == 2:
            print('O Jogador venceu')
        else:
            print('Resposta invalida')
    if maquina == 2: #tesoura#
        if jogador == 0:
            print('O Jogador venceu')
        elif jogador == 1:
            print('O Jogador perdeu')
        elif jogador == 2:
            print('Foi um Empate')
        else:
            print('Resposta invalida')
    print('=-=' * 11)
    resposta = input("Deseja jogar novamente ? S/N: ")
print("programa encerrado ")
