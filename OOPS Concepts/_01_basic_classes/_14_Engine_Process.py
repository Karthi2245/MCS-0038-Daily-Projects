# Engine_Process class:
class Engine_process:  # class
    # State
    def __init__(self, process1, process2, process3, process4 , process5):
        self.process1 = process1
        self.process2 = process2
        self.process3 = process3   # Fields
        self.process4 = process4
        self.process5 = process5

        # Behaviour:

    def process(self):   # Methods
        print("Engine process".ljust(40, '.'), ':', self.process1,
              self.process2,self.process3, self.process4, self.process5)


pr = Engine_process("Suction", "Compression ", "Combustion ", "Power-stroke ",
                    "Exhaustion ")
# object
pr.process()