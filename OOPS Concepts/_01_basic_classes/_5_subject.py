# subject class
class Subject:  # class
    # State
    def __init__(self, sub1, sub2, sub3, sub4 , sub5):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3   # Fields
        self.sub4 = sub4
        self.sub5 = sub5

        # Behaviour:

    def get_sub(self):   # Methods
        print("Books are".ljust(40, '.'), ':',self.sub1, self.sub2,
              self.sub3, self.sub4, self.sub5)


sub = Subject("Tamil", "English", "Maths", "Science", "Social")
# object
sub.get_sub()

