letra = "s"
while letra == "s":
    n1 = float(input("Digite um numero"))
    n2 = float(input("Digite a porcentagem que deseja descobrir"))

    porcentagem = (n1*n2)/100
    print(f'A porcentagem é igual a{porcentagem}: ')
    letra = input("Deseja continuar s/n: ")