# Multiplex:
class Multiplex:  # class
    # State
    def __init__(self, screen1, screen2, screen3, screen4 , screen5):
        self.movie1 = screen1
        self.movie2 = screen2
        self.movie3 = screen3    # Fields
        self.movie4 = screen4
        self.movie5 = screen5

        # Behaviour:

    def get_movies(self):   # Methods
        print("The Movies rely on Multiplex".ljust(40, '.'), ':',self.movie1,
              self.movie2,self.movie3, self.movie4, self.movie5)


movies = Multiplex("Vadivasal", "Annatha", "Beast", "Mersal", "Doctor" )


# object
movies.get_movies()