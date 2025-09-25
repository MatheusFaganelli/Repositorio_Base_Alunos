#apenas 6 erros permitidos
#criar um jogo da forca onde o usuario tena adivinhar uma palavra secreta


import random

def jogar():#função principa

    imprime_mensagem_abertura() #função para menssagem de abertura
    palavra_secreta = carrega_palavra_secreta() #escolhe uma palavra aleatoria de um arquivo.txt
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
   #transforma a palvra em uma lista de "_" uma para cad letra(ocultando a palavra, representados por underline (_ _ _).
   #lista de "_", uma para cada letra(ocultando a palavra)
    print(letras_acertadas) #mostra ao jogador os espaços da 
#palavra, representados
enforcou = False
acertou = False
erros = 0 

while (not enforcou and not acertou):
    
    chute = pede_chute()
    if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
    else:
                erros += 1
    

    enforcou = erros == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
    
    if (acertou):
        print("você ganhou!!")
    else:
         print("você perdeu")
         print("fim de jogo")

def pede_chute():
     chute = input("qual letra? ")
     chute = chute.strip().upper()
     return chute

def imprime_mensagem_abertura():
     print("*********************************")
     print("***bem vindo ao jogo da forca***")
     print("*********************************")

def carrega_palavra_secreta(nome_do_arquivo = r"C:\Users\Aluno_Programador\Desktop\matheus faganelli\jogo\Atividade 29 - palavras_forca.txt"):
    arquivo = open(nome_do_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
     
        arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavras):
     return ["_" for letra in palavras]

#contextualizar o metodo "if(__name__ == "__main__"):" significa que o arquio esta sendo executado diretamente
# não apenas sendo lido para ser utilizado






