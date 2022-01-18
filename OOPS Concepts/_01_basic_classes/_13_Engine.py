# Engine class
class Engine:  # class
    # State
    def __init__(self, part1, part2, part3, part4 , part5):
        self.part1 = part1
        self.part2 = part2
        self.part3 = part3  # Fields
        self.part4 = part4
        self.part5 = part5

        # Behaviour:

    def get_part(self):   # Methods
        print("Parts in Engine".ljust(40, '.'), ':', self.part1, self.part2,
              self.part3, self.part4, self.part5)


parts = Engine("Clutchbox", " Gear box ", "Cylinder ", "Cam", "valve " )
# object
parts.get_part()
