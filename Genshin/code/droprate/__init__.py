from random import randint
import json


def json_char(req='no', tier='', rate=0, color=0, star=0):
    with open("characters.json") as arquive_char:
        x = json.load(arquive_char)
    if req not in 'no':
        return print(f"{c[color]}{'★'*star} = {x['Char'][tier][rate]} c{0}")
    else:
        return print('Invalid Person')


def json_rate(tier=0, rating=0, gua=0):
    with open("rate.json", "w") as arquive_rate:
        rate_json = json.load(arquive_rate)
    if tier== 1:
        rate_json['rating']['tier4'] += rating
        rate_json['rating']['tier5'] += rating

    ratechar = json.dumps(rate_json, indent=2)
    arquive_rate.write(ratechar)
    if gua == 1:
        var = rate_json['rating']['guaranteed'][0]
        if var == 0:
            rate_json['rating']['guaranteed'][0] = 1
            return 1
        elif var == 1:
            rate_json['rating']['guaranteed'][0] = 0
            return 0

    if tier == 5:
        return rate_json['rating']['tier5']
    elif tier == 4:
        return rate_json['rating']['tier4']


def drop(pulls=0):
    gacha_pulls = []
    num = 0
    while num != pulls:
        gacha_pulls.append(randint(0, 10))
        json_rate(rating=1)
        num += 1
    return gacha_pulls

def character(dropr):
    with open('rate.json') as char_rate:
        person_rate = json.load(char_rate)
    gacha_pulls = drop(dropr)

    for gacha in gacha_pulls:

        if gacha <= 6 or person_rate['rating']['tier5'][0] >= 80:

            rate = randint(1, 2) #tier5 dest
            if json_rate(gua=1) == 1 and rate == 1:
                json_char('yes', 'Tier5', 5, 3, 5)
                guaranteed = '0'
            else:
                rate = randint(0, 4) # Tier5
                json_char('yes', 'Tier5', rate, 3, 5)
                guaranteed = '1'
        elif gacha <= 51 or person_rate['rating']['tier4'][0] == 10:
            rate = randint(0, 1) #Tier4 Dest
            if rate == 0:
                json_char('yes', 'Tier4G', rate, 5, 4)
            if rate == 1: #Tier4
                rate = randint(0, 37)
                json_char('yes', 'Tier4', rate, 5, 4)
        elif gacha <= 1000: # Tier3
            rate = randint(0, 26)
            json_char('yes', 'Tier3', rate, 4, 3)



c = ['\033[m', # clear
    '\033[31m',# vermelho
    '\033[32m',# verde 
    '\033[33m',# amarelo
    '\033[34m',# azul
    '\033[35m',# roxo
    '\033[36m',# ciano
    '\033[37m' ] #cinza

