from atm_card import AtmCard

import random
from datetime import datetime

atmUser = AtmCard()

# Note:
# When user not create account, login using:
# 4000 0000 0000 0000 and PIN: 1234
# When user create account, login using:
# 16 digit generated card and 4 digit generated PIN


def createCard():
    atmId = 4000000000000000 + random.randint(1000, 9999)
    pin = random.randint(1000, 9999)
    atmUser.setId(atmId)
    atmUser.setPin(pin)
    print('Your card has been created')
    print('Your card number :' + str(atmUser.checkId()))
    print('Your card pin: ' + str(atmUser.checkPin()))


def printReceipt():
    print('--------------------')
    recordNo = random.randint(100000, 1000000)
    currentDate = datetime.now()
    currentBalance = atmUser.defaultBalance
    print('Record No: ' + str(recordNo))
    print('Date: ' + str(currentDate))
    print('Balance: ' + str(currentBalance))


def manageAccountMenu():
    isShowAccountMenu = True

    while (isShowAccountMenu):
        account_menus = ['Logout', 'Balance', 'Add Income', 'Transfer Money']
        index_account_menu = 0

        print('--------------------')

        for acoount_menu in account_menus:
            print(str(index_account_menu) + '. ' + acoount_menu)
            index_account_menu += 1

        print('--------------------')

        accountMenu = int(input('Masukkan nomor menu: '))

        if (accountMenu == 0):
            printReceipt()
            break
        elif (accountMenu == 1):
            print('Your balance: ' + str(atmUser.checkBalance()))
        elif (accountMenu == 2):
            income = int(input('Add your income: '))
            atmUser.credit(income)
            print('Add income success')
            print('Your balance: ' + str(atmUser.checkBalance()))
        elif (accountMenu == 3):
            transfer = int(input('Add nominal to transfer: '))
            atmUser.debet(transfer)
            print('Transfer success')
            print('Your balance: ' + str(atmUser.checkBalance()))
        else:
            print('Please input 0 - 4')


def loginExistingCard():
    atmId = int(input('Enter your 16 digit card number: '))
    pin = int(input('Enter your 4 digit PIN: '))
    if (atmId == atmUser.checkId() and pin == atmUser.checkPin()):
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