#Faça  um  Programa  que  peça  as  quatro  notas  de  10  alunos,  calcule  e  armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 

soma = 0
media = []
count = 1
nApro = 0
while count <= 10 :
  print(f'Digite a nota do aluno {count} ')
  for a in range(4):
    notas = int(input(f'Digite a {a+1} nota '))
    soma += notas 
  md = soma/ 4 
  media.append(md)
  count +=1 
for n in media :
  if n >= 7 :
    nApro +=1
print(f'O numero de aprovados foi de {nApro}')
   