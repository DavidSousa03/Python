#Faça um Programa que armazena em uma lista 4 notas, mostre as notas e a média na tela. 

notas = []
numero= int(input('Digite quantas notas vc tem ?'))
soma = 0
for x in range(numero):
  notas.append(int(input('Digite a nota: ')))
for i in notas:
  soma = soma + i
media = soma / numero 

print(f'Suas notas são {notas}. E a media é de {media}')
