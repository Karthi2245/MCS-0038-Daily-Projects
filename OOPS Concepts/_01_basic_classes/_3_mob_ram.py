# Mobile class
class Mob_ram:  # class
    # State
    def __init__(self, rmem1, rmem2, rmem3, rmem4 , rmem5):
        self.rmem1 = rmem1
        self.rmem2 = rmem2
        self.rmem3 = rmem3    # Fields
        self.rmem4 = rmem4
        self.rmem5 = rmem5

        # Behaviour:

    def get_mob_ram(self):   # Methods
        print("Various ram".ljust(40, '.'), ':',self.rmem1, self.rmem2,
              self.rmem3, self.rmem4, self.rmem5)


ram = Mob_ram("1gb", "2gb", "3gb", "4gb", "8gb" )
# object
ram.get_mob_ram()