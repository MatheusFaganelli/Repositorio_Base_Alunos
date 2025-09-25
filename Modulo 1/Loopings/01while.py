letra = "s"
while letra == "s":
#solicitando ao usuario as tres notas
    n1 = float(input("digite a primeira nota: "))
    n2 = float(input("digite a primeira nota: "))
    n3 = float(input("digite a primeira nota: "))
    #realizando os calculos da média
    soma = n1 + n2 + n3
    media = soma / 3
    print(f"a média do aluno é : {round(media,2)}")
    if media >= 7:
        print("aprovado")
    elif media > 3:
        print("recuperação")
    else:
        print("reprovado")

letra = input("deseja continuar? (s\n): ")
               