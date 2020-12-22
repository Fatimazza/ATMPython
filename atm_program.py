from atm_card import AtmCard
from customer import Customer

main_menus = ['Exit', 'Create an Account', 'Log into an Account']
index_main_menu = 0

for main_menu in main_menus:
    print(str(index_main_menu) + '. ' + main_menu)
    index_main_menu += 1

print('--------------------')