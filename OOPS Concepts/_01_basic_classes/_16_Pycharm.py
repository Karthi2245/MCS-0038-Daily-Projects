# Pycharm class
class Pycharm:  # class
    # State
    def __init__(self, option1, option2, option3, option4 , option5):
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3   # Fields
        self.option4 = option4
        self.option5 = option5

        # Behaviour:

    def opt_in_pycharm(self):   # Methods
        print("Options available in pycharm".ljust(40, '.'), ':', self.option1,
              self.option2, self.option3, self.option4, self.option5)


py = Pycharm("File ", "Edit ", "View ", " Navigate ", " code ")
# object
py.opt_in_pycharm()
