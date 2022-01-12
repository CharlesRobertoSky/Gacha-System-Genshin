from _init_ import *
from time import sleep
log('Log gerado', 'w')
rate = pl_cr = JsonManager()
rate.create_json('data/rate.json')
player = opc = ''

sleep(2)
if player == '':
    player = str(input('Digite seu nickname: '))

if player == '':
    player = 'anonimo'

if pl_cr.create_player(player):

    print(f'Bem vindo de novo {player}, tenha uma boa sorte!')
else:
    print(f'Bem vindo {player}, tenha uma boa sorte!')
while opc != 'sair':

    opc = 0
    print('=-'*20)
    print(f'{"Escolha uma opção: ":^40}')
    print(f'{"[ 1 Pull]    [10 Pull]":^40}')
    print('=-'*20)
    opc = str(input())
    print('')
    if opc == 'sair':
        break
    elif opc == '1':
        pull = 1

    elif opc == '10':
        pull = 10

    drop_rate(player, pull)
    print('')
print('Fim do programa...')
