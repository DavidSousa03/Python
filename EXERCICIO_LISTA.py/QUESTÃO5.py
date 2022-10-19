#Faça  um  Programa  que  leia  20  números  inteiros  e  armazene-os  numa  lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima os três vetores

inter = [] 
par = []
impar = []
for d in range(20):
  inter.append(int(input('Digite os numeros inteiros: ')))
for x in inter:
  if x % 2==0: 
    par.append(x)
  else:
    impar.append(x)   
print(f'Numeros inteiros {inter}')
print(f'Numeros pares {par}')
print(f'Numeros impares  {impar}')
