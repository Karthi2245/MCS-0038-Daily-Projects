# Geometry box class
class Geometry_Box:  # class
    # State
    def __init__(self, item1, item2, item3, item4 , item5):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3   # Fields
        self.item4 = item4
        self.item5 = item5

        # Behaviour:

    def get_item(self):   # Methods
        print("Items in the geometry box".ljust(40, '.'), ':', self.item1,
              self.item2,self.item3, self.item4, self.item5)


items = Geometry_Box("Pen ", "Pencil ", "Rubber ", "Scale ", "Sharpner " )
# object
items.get_item()
