# Gas class
class Laptops:  # class
    # State
    def __init__(self, type1, type2, type3, type4 , type5):
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3   # Fields
        self.type4 = type4
        self.type5 = type5

        # Behaviour:

    def type_lap(self):   # Methods
        print("Types of Laptops".ljust(40, '.'), ':', self.type1, self.type2,
              self.type3, self.type4, self.type5)


type = Laptops("Lenovo ", "Dell ", "Acer ", "Hp ", "Realme " )
# object
type.type_lap()
