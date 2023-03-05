import os
import time
import platform
belladona = 0
nulo = 0
sistema = platform.system()
def limpar():
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux':
        os.system('clear')
while True:
    limpar()
    txt = """
#           x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
#
#           Bem vindo a interface de votos improvisada do Kandora!
#
#           x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
#
#           [1] Chapa Belladona
#
#           [0] Voto Nulo
#
#           x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
#
#           Criado por zLuuuck! (Lucas Toterol, 2°ADM)
   """
    print(txt)
    voto = str(input('Digite seu voto:')).strip()

    if voto == 'acabar':
        print(f'Votos para Belladona: {belladona}')
        print(f'Votos nulos: {nulo}')
        print(f'Total de votos: {belladona + nulo}')
        break
    elif voto == '1':
        belladona += 1
    elif voto == '0':
        nulo += 1
    else:
        while voto not in '10':
            print(' ')
            print('Candidato não existente..')
            voto = str(input('Digite seu voto:')).strip()
            if voto == 'acabar':
                print(f'Votos para Belladona: {belladona}')
                print(f'Votos nulos: {nulo}')
                print(f'Total de votos: {belladona + nulo}')
                break
            elif voto == '1':
                belladona += 1
                break
            elif voto == '0':
                nulo += 1
                break

    print('Voto contabilizado!')
    print('Aguarde . . . ')
    time.sleep(3)
