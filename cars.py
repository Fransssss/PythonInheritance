class Car:

    def wheel(self):
        print("Cars have 4 wheels in general")

    def legal(self):
        print("Cars are legal to drive in US and Europe")

    def sport_car(self):
        print("This is a sport car")

    def no_sport_car(self):
        print("This is a regular car")


class OCar (Car):
    def __init__(self, brand, place, year):
        self.brand = brand
        self.place = place
        self.year = year

    def the_brand(self):
        print("The brand of this car is " + self.brand)

    def the_place(self):
        print(self.brand + " is originally from " + self.place)

    def the_year(self):
        print("This car was founded in " + str(self.year))


class TCar(Car):
    def __init__(self, brand, place, year):
        self.brand = brand
        self.place = place
        self.year = year

    def the_brand(self):
        print("The brand of this car is " + self.brand)

    def the_place(self):
        print(self.brand + " is originally from " + self.place)

    def the_year(self):
        print("This car was founded in " + str(self.year))
