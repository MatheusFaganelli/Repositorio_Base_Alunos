#crie um codigo que solicite o preço total da compra e ofereça um desconto de 10% se 
# a compra for maior ou igual a 500 reais
conta = float(input("informe o preço total da sua compra"))
if conta >= 500:
    conta*=0.9
    print(f"vc recebeu um desconto de 10% E o valor a pagar é R${conta} ")
else:
    print("obrigado pela sua compra")



























