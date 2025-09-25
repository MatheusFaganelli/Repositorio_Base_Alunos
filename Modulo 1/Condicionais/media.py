#crie um programa que solicite o usuario duas notas, calcule a média, e informe se o aluno esta aprovado (media maior ou igual a sete), em recuperação media >= a 5 ou reprovado.
nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1 + nota2)/2
if media >= 7:
    print(f"sua media foi {media} e você esta aprovado.")
elif media >= 5:
    print(f"sua media foi{media} e você esta de recuperação.")
else:
    print(f"sua média foi {media} e você esta reprovado.")

























