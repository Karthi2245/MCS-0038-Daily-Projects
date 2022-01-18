# Gender class
class Gender:  # class
    # State
    def __init__(self, type1, type2, type3):
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3   # Fields

        # Behaviour:

    def type_gender(self):   # Methods
        print("Types of Gender".ljust(40, '.'), ':', self.type1, self.type2,
              self.type3)


type = Gender("Male", "Female ", "Transgender ")
# object
type.type_gender()
