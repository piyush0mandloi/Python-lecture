class MovieBooking:
    def __init__(self):
        self.movies = {
            'Avengers':{'time':'6 PM', 'seats': 100},
            'How to Train Your Baby':{'time':'9 PM', 'seats': 80},
        }
    
    def show_movies(self):
        for movie, info in self.movies.items():
            print(f"{movie} - {info['time']} - {info['seats']} seats left")
    
    def book_ticket(self, movie_name, num_seats):
        if movie_name in self.movies:
            if self.movies[movie_name]['seats'] >= num_seats:
                self.movies[movie_name]['seats']-=num_seats
                print(f"Successfully booked {num_seats} seat(s) for {movie_name}")
            else:
                print("Not enough seats")
        else:
            "Movie not available"

booking = MovieBooking()
booking.show_movies()
movie = input("Enter movie name to book: ")
seats = int(input("Enter the number of seats to book: "))
booking.book_ticket(movie, seats)