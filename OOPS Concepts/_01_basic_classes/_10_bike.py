# Bike class
class Bike:  # class
    # State
    def __init__(self, brand1, brand2, brand3, brand4, brand5):
        self.brand1 = brand1
        self.brand2 = brand2
        self.brand3 = brand3    # Fields
        self.brand4 = brand4
        self.brand5 = brand5

        # Behaviour:

    def bike_types(self):   # Methods
        print("The Bikes are".ljust(40, '.'), ':', self.brand1, self.brand2,
              self.brand3, self.brand4, self.brand5)


bikes = Bike("RoyalEnfeild", "Tvs", "Honda", "Bajaj", "Yamaha" )
# object
bikes.bike_types()