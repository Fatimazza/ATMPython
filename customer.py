from atm_card import AtmCard


class Customer(AtmCard):
    def __init__(self,
                 custId=4000000000000000,
                 custPin=1234,
                 custBalance=10000):
        super().__init__(custId, custPin, custBalance)

    def debet(self, nominal):
        self.custBalance -= nominal
        return self.custBalance

    def credit(self, nominal):
        self.custBalance += nominal
        return self.custBalance