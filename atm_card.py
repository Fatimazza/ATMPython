class AtmCard:
    def __init__(self,
                 defaultId=4000000000000000,
                 defaultPin=1234,
                 defaultBalance=10000):
        self.defaultId = defaultId
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def checkId(self):
        return self.defaultId

    def checkPin(self):
        return self.defaultPin

    def checkBalance(self):
        return self.defaultBalance
