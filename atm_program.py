from atm_card import AtmCard
from customer import Customer

import random

while (True):

    main_menus = ['Exit', 'Create an Account', 'Log into an Account']
    index_main_menu = 0

    for main_menu in main_menus:
        print(str(index_main_menu) + '. ' + main_menu)
        index_main_menu += 1

    print('--------------------')

    main_menu = int(input('Masukkan nomer menu: '))

    if (main_menu == 1):
        print('Your card has been created')
    elif (main_menu == 2):
        print('Ok')
    else:
        exit()
