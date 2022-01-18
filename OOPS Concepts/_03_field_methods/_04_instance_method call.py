# Instance method Calling :
class Employee:

    def __init__(self, eid, esal):
        self. eid = eid
        self. esal = esal
    def get_data(self):
        print(self.eid, self.esal)

    def update_hike(self, rating):
        if rating >= 4 and  rating <=5:
            self.hike = self.esal * 30/100
            return self.hike
        elif rating >=3 and rating < 4:
            self.hike = self.esal * 20/100
            return  self.hike
        elif rating >= 2 and rating < 3:
            self.hike = self.esal* 10/100
            return  self.hike
        elif rating >=1 and rating < 2:
            self.hike = self.esal* 5/100
            return self.hike
        else:
            print("Hike is Zero")


karthi = Employee(101, 10000)
karthi.update_hike(3)





















