# Ve class
class Vehicle:  # class
    # State
    def __init__(self, car1, car2, car3, car4 , car5):
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3    # Fields
        self.car4 = car4
        self.car5 = car5

        # Behaviour:

    def get_vehicle(self):   # Methods
        print("Vehicles".ljust(40, '.'), ':', self.car1, self.car2,
              self.car3, self.car4, self.car5)


vehicles = Vehicle("BMW", "Suzuki", "Thar", "Toyota", "Jaguar")


# object
vehicles.get_vehicle()