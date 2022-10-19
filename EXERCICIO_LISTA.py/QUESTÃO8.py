#Faça  um  Programa  que  peça  a  idade  e  a  altura  de  5  pessoas,  armazene  cada informação na sua respectiva lista. Imprima a idade e a altura na ordem inversa a ordem lida. 

idade = []
altura = []
cont = 1 
for s in range(5):
  idade.append(int(input('Digite a sua idade :')))
  altura.append(input('Digite a sua altura:'))
idade.sort(reverse=True)   
altura.sort(reverse=True)
print(idade)
print(altura)   
  