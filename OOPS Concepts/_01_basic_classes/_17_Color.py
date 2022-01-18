# Color class
class Color:  # class
    # State
    def __init__(self, type1, type2, type3, type4 , type5):
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3   # Fields
        self.type4 = type4
        self.type5 = type5

        # Behaviour:

    def type_color(self):   # Methods
        print("Types of Colors".ljust(40, '.'), ':', self.type1, self.type2,
              self.type3, self.type4, self.type5)


type = Color("Blue", "Green ", "Black ", "Purple ", "Pink " )
# object
type.type_color()
