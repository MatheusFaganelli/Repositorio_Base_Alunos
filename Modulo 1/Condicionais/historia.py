#o aventureiro e a floresta 
print("bem vindo aventureiro  floresta encantada")
nome_jogador = input("qual é seu nome aventureiro? ")
print(f"\n ola {nome_jogador}você se encontra na borda da floresta encantada")
print("2 caminhos se apresentam: um a esquerda escuro e misterioso, e outro a direita, iluminado pelo sol")
primeira_escolha = input("qual caminho você escolhe?(esquerda/direita)").lower()
if primeira_escolha == "esquerda":
    print("você escolheu o caminho escuro e miserioso")
    print("voce encontra um lago brilhante. a àgua parece convidativa")
    escolha_lago = input("voce bebe a agua ou procura por uma trilha ao redor?(beber/trilha)").lower()
    if escolha_lago == "beber":
        print("A agua do lago te revigora você se sente mais forte")
# simule um aumento de "saude" oi um novo item
    elif escolha_lago == "trilha":
        print("você encontra uma trilha escondida que o leva a uma caverna.")
elif primeira_escolha == "direita":
    print("você escolhe o caminho iluminado pelo sol")
    print("você chega a uma claeira onde fadas dançam no ar")
    escolha_fadas = input("você tenta conversar com as fadas ou se esconde?(conversar/esconder)").lower()
    if escolha_fadas == "esconder":
        print("as fadas sorriem para voce e lhe oferencem um presente magico")
    elif escolha_fadas == "esconder":
        print("você se esconde e as fadas passam sem perceber sua presença")
    else:
        print("você se distrai e as fadas desaparecem. que pena!")
else:
    print("essa não é uma escolha valida. você fica parado e a floresta te engole")
print(f"\nfim da aventura para {nome_jogador},obrigado por jogar")













