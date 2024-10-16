#Peça dois números e mostre o resultado da divisão com apenas duas casas decimais

num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

divisao = num1 / num2

print(f'A divisão de {num1} por {num2} é {divisao:.2f}')
