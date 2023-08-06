import requests

try:
    response = requests.get('http://www.pudim.com.br')
except:
    print('Site inacessível no momento :(')
else:
    print('Consegui me conectar ao site com sucesso !')

