class CSStudent:
    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, roll):
        # Instance Variable
        self.roll = roll

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

a = CSStudent(101)
a.setAddress("Noida, UP")
print(a.getAddress())  