#Faça um Programa que  armazena em uma lista 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos da lista. 

inteiros = []
quadrado = []
for i in range(3):
  inteiros.append(int(input('Digite um numero: ')))
for x in inteiros:
  x = x **2 
  quadrado.append(x)  
print(quadrado)  