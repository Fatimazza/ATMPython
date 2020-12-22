from atm_card import AtmCard


class Customer:
    def __init__(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.custPin

    def checkBalance(self):
        return self.custBalance

    def debet(self, nominal):
        debet = self.custBalance - nominal
        # current custBalance hasn't updated
        return debet

    def credit(self, nominal):
        credit = self.custBalance + nominal
        # current custBalance hasn't updated
        return credit