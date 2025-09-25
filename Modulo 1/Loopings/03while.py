#C5rie um programa que calcule o fatorial de um numero
n=int (input("Digite um numero para saber o fartorial"))
resultado = 1 # 5! = 5.4.3.2.1
f = 1


while f<= n:
    resultado *= f
    f += 1
    print(f"o fatorial do {n} é : , {resultado}")