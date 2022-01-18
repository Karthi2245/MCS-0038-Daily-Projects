# Gas class
class Myprofile:  # class
    # State
    def __init__(self, fname, gender, degree, blood , address, mob_num ):
        self.fname = fname
        self.gender = gender
        self.degree = degree  # Fields
        self.blood = blood
        self.address = address
        self.mob_num = mob_num


        # Behaviour:

    def get_profile(self):   # Methods

        print("My Profile".ljust(40, '.'), ':', self.fname, self.gender,
              self.degree, self.blood,self.address,  self.mob_num)


profile = Myprofile("Karthikeyan ", "Male ", "BE Mech ", "B+ve ",
           "Theni", "9786910190" )
# object
profile.get_profile()
