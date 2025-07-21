class CarRental:
    def __init__(self):
        self.cars = {'Sedan':500, 'SUV':800, 'Hatchback':300}
    
    def display_cars(self):
        print("Available Cars:")
        for car, price in self.cars.items():
            print(f"{car} - rs{price}/day")
    
    def rent_car(self, car_name, days):
        if car_name in self.cars:
            total = self.cars[car_name] * days
            print(f"You have rented a {car_name} for {days} days. Total: rs{total}")
        else:
            print("Sorry, car not available.")

rental = CarRental()
rental.display_cars()
car = input("Which car do you want to rent? ")
days = int(input("For how many days? "))
rental.rent_car(car, days)