# Mobile class
class Mobile:  # class
    # State
    def __init__(self, mname1, mname2, mname3, mname4 , mname5):
        self.mname1 = mname1
        self.mname2 = mname2
        self.mname3 = mname3    # Fields
        self.mname4 = mname4
        self.mname5 = mname5

        # Behaviour:

    def get_mob_model(self):   # Methods
        print("Mobile Models".ljust(40, '.'), ':',self.mname1, self.mname2,
              self.mname3, self.mname4, self.mname5)


mob = Mobile("Moto", "Lenovo", "Iphone", "oppo", "Samsung" )
# object
mob.get_mob_model()