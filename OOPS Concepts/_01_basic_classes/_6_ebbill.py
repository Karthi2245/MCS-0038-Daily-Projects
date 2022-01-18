# Electriccity  class
class Electricity:  # class
    # State
    def __init__(self, bill1, bill2, bill3, bill4, bill5):
        self.bill1 = bill1
        self.bill2 = bill2
        self.bill3 = bill3    # Fields
        self.bill4 = bill4
        self.bill5 = bill5

        # Behaviour:

    def get_eb_bill(self):   # Methods
        print("Eb Bill For Hosues".ljust(40, '.'), ':',self.bill1, self.bill2,
              self.bill3, self.bill4, self.bill5)


eb_bill = Electricity("house-1:180", "house-2:150", "house-3:950",
                      "house-4:360", "house-5:200" )
# object
eb_bill.get_eb_bill()