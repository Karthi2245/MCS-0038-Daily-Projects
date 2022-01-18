# Municipaloffice class
class Municipaloffice:  # class
    # State
    def __init__(self, dept1, dept2, dep3, dep4 , dep5):
        self.dep1 = dept1
        self.dep2 = dept2
        self.dep3 = dep3    # Fields
        self.dep4 = dep4
        self.dep5 = dep5

        # Behaviour:

    def get_dept(self):   # Methods
        print("Various Departments in Municipality".ljust(40, '.'), ':',
              self.dep1, self.dep2, self.dep3, self.dep4, self.dep5)


mun_off = Municipaloffice("h-tax ", "i-tax ", "w-tax ", "vid-issue ",
                          "corporation " )
# object
mun_off.get_dept()