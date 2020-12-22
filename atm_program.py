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


def manageAccountMenu():
    isShowAccountMenu = True

    while (isShowAccountMenu):
        account_menus = [
            'Exit', 'Balance', 'Add Income', 'Transfer Money', 'Logout'
        ]
        index_account_menu = 0

        print('--------------------')

        for acoount_menu in account_menus:
            print(str(index_account_menu) + '. ' + acoount_menu)
            index_account_menu += 1

        print('--------------------')

        input('Masukkan nomor menu: ')


def loginExistingCard():
    atmId = int(input('Enter your 16 digit card number: '))
    pin = int(input('Enter your 4 digit PIN: '))
    atm = AtmCard()
    if (atmId == atm.checkId() and pin == atm.checkPin()):
        print('Success')
        manageAccountMenu()
    else:
        print('Card or PIN you have entered is wrong')


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
        loginExistingCard()
    elif (main_menu == 0):
        exit()
    else:
        print('Please input 0 - 2')