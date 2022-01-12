from os.path import dirname, realpath, isfile
from random import randint
from datetime import datetime
from time import sleep
import json


class JsonManager:

    def __init__(self):  # Função construtiva para criar um arquivo caso ele não exista
        self.path = dirname(realpath(__file__)) + '/'

    def create_log(self, file):
        data = []
        path_data_json = self.path + file
        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                f.write('Log Gerado')
            print('Gerando aquivo de Log')
            return True
        else:
            print('aquivo log ja existe')
            return False

    def create_json(self, file):

        data = {}
        path_data_json = self.path + file

        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                json.dump(data, f, indent=2)
            print('criando arquivo json')
            return True
        else:
            log('arquivo json ja existe', 'a')
            return False

    def create_player(self, player):  # Função para criar um player
        if querry_player(player):
            log('Player encontrado', 'a')
            return True
        else:
            print(f'Player nao encontrado, criando um player novo...')
            data = {"pit": 0, "tier4": 0, "tier5": False}
            data_j = open_json('rate')
            new_data = data_j['player']
            new_data[player] = data.copy()
            new_data2 = {'player': new_data}
            try:
                close_json('rate', new_data2, 'w')
                return False
            except:
                log('Erro na criacao de player', 'a')
                return False


def querry_player(player):  # Função que localiza player no json
    rate_json = open_json('rate')
    pos = 0
    for querry in rate_json['player']:
        log(f'posicao {pos} = {querry}', 'a')
        if player == querry:
            return True
        pos += 1
    return False


def open_txt(arquive_name):  # abre o log
    try:
        with open(f'data/{arquive_name}', 'r') as f:
            return True
    except:
        print('erro ao abrir arquivo txt')


def log(data_write, par='a'):  # escreve ou sobrescreve o log
    try:
        data = datetime.now()
        with open(f'data/arquive-log.txt', par) as f:
            f.write(f'\n {data} // {data_write}')
    except:
        print('erro ao fechar arquivo txt')


def open_json(arquive_name):  # abre o arquivo
    try:
        with open(f"data/{arquive_name}.json", 'r') as arquive:
            return json.load(arquive)
    except:
        return log('Erro encontrado na leitura do arquivo json', 'a')


def close_json(arquive_name, new_itens, par):  # fecha o arquivo
    try:
        with open(f"data/{arquive_name}.json", par) as arquive:
            json.dump(new_itens, arquive, indent=2)
    except:
        return log('Erro encontrado ao fechar o arquivo json', 'a')


def drop(n1=0, n2=0):
    return randint(n1, n2)


def pit_handler(player, option='add'):
    rajs = open_json('rate')
    if option == 'add':
        rajs['player'][player]['pit'] += 1
    elif option == 'add4':
        rajs['player'][player]['tier4'] += 1

    elif option == 'rt5':
        rajs['player'][player]['pit'] = 0
    elif option == 'rt5g':
        rajs['player'][player]['tier5'] = False

    elif option == 'ad5g':
        rajs['player'][player]['tier5'] = True

    elif option == 'rt4':
        rajs['player'][player]['tier4'] = 0
    close_json('rate', rajs,  'w')


def drop_rate(player, pull):
    print('Sorteando premio...')
    for i in range(0, pull):
        rate = drop(0, 1000)
        char = ''
        chjs = open_json('characters')
        rajs = open_json('rate')
        log(rajs['player'][player]['pit'], 'a')
        num = rajs['player'][player]['pit']
        log([type(num), num])
        pit_handler(player, 'add')
        if num == 89 or rate <= 6:  # Drop 5 stars
            rate = drop(1, 2)
            pit_handler(player, 'rt5')

            # dropa o personagem tier 5 do banner

            if rajs['player'][player]['tier5'] or rate == 1:
                char = chjs['Char']['Tier5'][0]
                pit_handler(player, 'rt5g')
                log('tier 5 garantido')

            else:  # dropa o personagem não garantido do banner
                rate = drop(1, 5)
                char = chjs['Char']['Tier5'][rate]
                pit_handler(player, 'ad5g')
            show_drop(char, 5)

        elif rajs['player'][player]['tier4'] == 9 or rate <= 51:  # Drop 4 stars
            rate = drop(0, 3)
            pit_handler(player, 'rt4')
            if rate <= 2:
                char = chjs['Char']['Tier4G'][rate]
                log('tier 4 garantido')
                show_drop(char, 4)

            else:
                rate = drop(0, 44)
                char = chjs['Char']['Tier4'][rate]
                log('tier 4')
                show_drop(char, 4)

        else:  # Drop 3 stars
            log('tier 3')
            rate = drop(0, 25)
            pit_handler(player, 'add4')
            char = chjs['Char']['Tier3'][rate]
            show_drop(char, 3)
        sleep(0.5)


c = [
    '\033[m',     # clear 0 cryo
    '\033[31m',  # vermelho 1 pyro
    '\033[32m',  # verde 2 anemo
    '\033[33m',  # amarelo 3 geo
    '\033[34m',  # azul 4 hydro
    '\033[35m',  # roxo 5 eletro
    '\033[36m',  # ciano 6
    '\033[37m'   # cinza 7 weapon

]


def show_drop(drop, tier, color=0):
    if tier == 3:
        print(f" {c[4]}★★★ {drop} {c[0]}")
    if tier == 4:
        print(f" {c[5]}★★★★{c[color]} {drop} {c[0]}")
    if tier == 5:
        print(f" {c[3]}★★★★★{c[color]} {drop} {c[0]}")


if __name__ == '__main__':
    rate = generate_log = JsonManager()
    rate.create_json('data/rate.json')
    generate_log.create_log('data/arquive-log.txt')
