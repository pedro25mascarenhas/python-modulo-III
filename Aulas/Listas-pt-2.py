teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])


galera = [['João', 19],['Maria', 40],['Joaquim', 13],['Creuza', 200]]

for pessoa in galera:
  print(pessoa[1])

