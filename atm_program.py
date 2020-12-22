from atm_card import AtmCard
from customer import Customer

customer1 = Customer(2222)
print(customer1.checkPin())
print(customer1.checkBalance())
print(customer1.credit(600))
print(customer1.checkBalance())
print(customer1.debet(500))
print(customer1.checkBalance())