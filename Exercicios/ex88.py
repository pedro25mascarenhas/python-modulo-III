# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep


palpites_mega = list()
temp = list()
qnt_jogos = int(input('Quantos jogos serão gerados? '))

for j in range(qnt_jogos):
  while True:
    randomico = randint(1, 60)
    if randomico not in temp:
      temp.append(randomico)
    if len(temp) == 6:
      break
  temp.sort()
  palpites_mega.append(temp[:])
  temp.clear()

for j in range(len(palpites_mega)):
  sleep(1)
  print(f'Jogo {j+1}: {palpites_mega[j]}')