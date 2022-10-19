#Faça um Programa que armazena em uma lista 5 números inteiros, mostre a soma, a multiplicação e os números

num = []
soma = 0
multi = 0
m = 0 
for a in range(5):
  num.append(int(input("Digite 5 numeros: ")))
  m += a
for e in num:
  soma += e
  multi = soma * m  
  
print(num)
print(f'A soma é = {soma}')
print(multi)
