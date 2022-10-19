#Faça  um  Programa  que  armazena  em  uma  lista  10  caracteres,  e  diga  quantas consoantes foram lidas. Imprima as consoantes. 

conso = []
soma = 0 
for i in range(10):
  conso.append(input(f'Digite o {i+1} caractere ')) 
for x in conso: 
  if x == 'a':   
    continue 
  elif x == 'e':
    continue 
  elif x == 'i':
    continue  
  elif x == 'o':
    continue 
  elif x == 'u':
    continue
  else:
    soma +=1  
print(f'a quantidade de consoantes são: {soma}')
print(f'As consoantes {conso}')  
