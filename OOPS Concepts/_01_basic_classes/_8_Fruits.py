# Fruits class
class Fruits:  # class
    # State
    def __init__(self, fruit1, fruit2, fruit3, fruit4 , fruit5):
        self.fruit1 = fruit1
        self.fruit2 = fruit2
        self.fruit3 = fruit3    # Fields
        self.fruit4 = fruit4
        self.fruit5 = fruit5

        # Behaviour:

    def fruit_types(self):   # Methods
        print("Fruits".ljust(40, '.'), ':', self.fruit1, self.fruit2,
              self.fruit3, self.fruit4, self.fruit5)


fruit = Fruits("strawberry ", "orange ", "banana ", "Mango ", "Apple " )
# object
fruit.fruit_types()