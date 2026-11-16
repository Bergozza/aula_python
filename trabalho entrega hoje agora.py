import random

import random

opcoes = ["pedra", "papel", "tesoura"]
jogadas = 3

while jogadas > 0:
    jogadas -= 1
    jogador = input("\nEscolha pedra, papel ou tesoura: ")
    
    if jogador not in opcoes:
        print("Opção inválida!")
        continue

    pc = random.choice(opcoes)
    print("Você")

    if jogador == pc:
        print("Empate!")
    elif (jogador == "pedra" and pc == "tesoura") or \
         (jogador == "papel" and pc == "pedra") or \
         (jogador == "tesoura" and pc == "papel"):
        print("Você ganhou!")
    else:
        print("PC ganhou!")

    if jogadas == 0:
        jogardnv = str(input("Jogar de novo?" "(s/n)"))
        if  jogardnv == "s":
            jogadas = 3
            