#As tuplas são imutáveis - ( )
#Listas podem mudar - [ ]

#Adicionar elementos no final da lista:

lanche = ['bolo','suco','melancia','sanduiche']
for c in lanche:
    print(c)
print('------------')

lanche.append('cookie')
for c in lanche:
    print(c)
print('-------------')

#adicionar item em algum lugar específico (sem substituir)
lanche.insert(0,'hamburguer')
for c in lanche:
    print(c)
print('-------------')
#eliminar itens
'''del lanche(3) #elimina numa posição específica
lanche.pop() #elimina o ultimo elemento direto
lanche.remove('melancia') #elimina pelo nome'''

#declarando uma lista partindo de uma progressão
valores = list(range(4,11,2))
print(valores)

#colocando em ordem crescente/decrescente
valores.sort()
valores.sort(reverse=True)
print(valores)

#contar os valores
print(len(valores))

for c, v in enumerate(valores): 
    print(c, v)

#ligação entre uma lista e outra
a = valores

#cópia de lista
a = valores[:]

