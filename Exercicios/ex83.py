expressao = input('Digite a expressão: ')

validacao = 'Expressão validada'
lista = []
for c in expressao:
  if c == '(' or c ==')':
    lista.append(c)

if lista[0] == ')' or lista[len(lista)-1] == '(' or lista.count('(') != lista.count(')'):
  validacao = 'Expressão não validada'

print(validacao)