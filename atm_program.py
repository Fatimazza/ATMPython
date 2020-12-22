from atm_card import AtmCard
from customer import Customer

import random


def createCard():
    atmId = 4000000000000000 + random.randint(1000, 9999)
    pin = random.randint(1000, 9999)
    atm = AtmCard(atmId, pin)
    print('Your card has been created')
    print('Your card number :' + str(atm.checkId()))
    print('Your card pin: ' + str(atm.checkPin()))


while (True):

    main_menus = ['Exit', 'Create an Account', 'Log into an Account']
    index_main_menu = 0

    print('--------------------')

    for main_menu in main_menus:
        print(str(index_main_menu) + '. ' + main_menu)
        index_main_menu += 1

    print('--------------------')

    main_menu = int(input('Masukkan nomer menu: '))

    if (main_menu == 1):
        createCard()
    elif (main_menu == 2):
        print('Ok')
    else:
        exit()