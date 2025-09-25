from random import randrange
from click import clear

def exibir_tabuleiro(tabuleiro):
    clear()
    print("+-----"*3, "+", sep="") #vai limpar a tela e imprimi a bordas superior do tabuleiro
    for linha in range(3):
        print("|          "* 3, "|", sep="")
        #imprimi a primeira linha vazia de cada limnha do tabuleiro
        for coluna in range(3):
            print("|     "+str(tabuleiro[linha][coluna])+"    ",end="")
        print("|")
        print("|       "* 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def entrada_jogador(tabuleiro):
    valido = False
    while not valido:
        movimento = input("digite seu movimento:  ")
        valido = len(movimento) == 1 and movimento >= '1' and movimento <= "9"
        if not valido:
            print("movimento ruim - repita sua entrada!")
            continue
            movimento = int(movimento) - 1  #converte para indice de 0 a 8
            linha = movimento // 3
            coluna = movimento % 3
            conteudo = tabuleiro[linha][coluna] # verifica o conteudo do campo selecionado
            valido = conteudo not in ["O", "X"]
            if not valido:
                print("campo ja ocupado - repita sua entrada!")
                continue
            tabuleiro[linha][coluna] not in ["O", "X"]

def lista_campos_livres(tabuleiro):
    livres = [] # lista inicialmente vazia
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ["O", "X"]:
                livres.append((linha, coluna))
    return livres

def verifica_vitoria(tabuleiro, sinal):
    if sinal == "X":
        vencedor = 'computador'
    elif sinal == "O":
        vencedor = 'jogador'
    else:
        vencedor = None

        diag1 = diag2 = True # variaveis para verificar as diagonais
        for i in range(3):
            # verifica a linha i
            if tabuleiro[i][0] == sinal and tabuleiro[i][1] == sinal and tabuleiro[i][2] == sinal:
                return vencedor
            # verifica a coluna i
            if tabuleiro[0][i] == sinal and tabuleiro[1][i] == sinal and tabuleiro[2][i] == sinal:
                return vencedor
             # verifica a diagonal principal
            if tabuleiro[i][i] != sinal:
                diag1 = False
            #verifica a diagonal inversa
            if tabuleiro[1][2 - i] != sinal:
                diag2 = False
    if diag1 or diag2:
        return vencedor
    return None

def jogada_computador(tabuleiro):
    livres = lista_campos_livres(tabuleiro)
    quantidade = len(livres)
    if quantidade > 0:
        escolha = randrange(quantidade)
        linha, coluna = livres[escolha]
        tabuleiro[linha][coluna] = "X"
# cria o tabuleiro inicial com números de 1 a 9

tabuleiro = [[3 * j + i + 1 for i in range (3)] for j in range (3)]
tabuleiro[1][1] = "X" #define um "X" no centro
livres = lista_campos_livres(tabuleiro)
vez_jogador = True # indica que é a vez do jogador
vencedor = None#variavel para armazenar o vencedor

while len(livres) and vencedor is None:
    exibir_tabuleiro(tabuleiro)
    if vez_jogador:
        entrada_jogador(tabuleiro)
        vencedor = verifica_vitoria(tabuleiro, 'O')
    else:
        jogada_computador(tabuleiro)
        vencedor = verificar_vitoria(tabuleiro, "X")
    vez_jogador = not vez_jogador
    livres = lista_campos_livres(tabuleiro)

exibir_tabuleiro(tabuleiro)
if vencedor == 'jogador':
    print("você ganhou!")
elif vencedor == "computador":
    print("eu venci")
else:
    print("empate")