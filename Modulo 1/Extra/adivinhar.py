#crie um jogo de adivinhação

import random

def jogar_adivinhacao():
    print("***************")
    print("bem vindo ao jogo da adivinhação")
    print("***************")

    numero_secreto = random.randint(1, 100) 
    pontos = 1000

    print("qual o nivel de dificuldade?")
    print(" (1) facil (2) medio (3) dificil.")

    while True:
        try:
            nivel = int(input("defina o nivel:"))
            if nivel in [1, 2, 3]:
                break
            else:
                print("escolha um nivel valido: (1) (2) (3). ")
        except ValueError:
            print("por favor digite um numero valido ")
    if nivel ==1:
        total_tentativas =20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"tentativa {rodada} de {total_tentativas}")

        while True:
            try:
                chute = int(input("digite um numero entre 1 e 100"))
                if 1 <= chute <= 100:
                    break
                else:
                    print("numero fora do intervalo digite um numero entra 1 e 100")
            except ValueError:
                print("entrada invalida! digite um numero inteiro.")
        print(f"voce digitou: {chute}")
            
        if chute == numero_secreto:
            print(f"parabens você acertoe fez {pontos} pontos.")
            break
        else:
            if chute > numero_secreto:
                print("voce errou! o numero que voce chutou é maior que o numero secreto")
            else:
                print("voce errou o numero que voce chuitou é menor")

                pontos_perdidos = abs(numero_secreto - chute)
                pontos = max(0, pontos - pontos_perdidos)

    print(f"o numero secreto era {numero_secreto} fim do jogo")

if __name__ == "__main__":
    jogar_adivinhacao()

















