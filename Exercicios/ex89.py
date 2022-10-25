# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = list()
qnt_alunos = int(input('Digite a quantidade de alunos: '))
temp = list()
for c in range(qnt_alunos):
  aluno = input('Digite o nome do Aluno: ')
  notas = list(map(float, input('Digite as notas do aluno separadas por espaço: ').split()))
  media = (notas[0] + notas[1])/2
  temp.append(aluno)
  temp.append(notas[:])
  temp.append(media)
  lista_alunos.append(temp[:])

print(lista_alunos)