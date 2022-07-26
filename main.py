from cars import Car
from cars import OCar
from cars import TCar

try:                          # dont mind this try and except outside the program, I just dont like to see the warning when I terminate the program
    print("\n== Cars Menu ==")
    print("1. Input data")
    print("2. Display data")
    print("E. Exit")
    choice = input("choice; ")

    one_car = OCar("NoBrand", "NoPlace", 0)
    one_sport_car = False
    two_car = TCar("NoBrand", "NoPlace", 0)
    two_sport_car = False
    invalid = 1                               # count invalid data

    while choice != 'e' and choice != 'E':
        if choice == '1':
            print("\n[ Input data ]")
            print("\n> 1st car")
            brand1 = input("Brand: ")
            if brand1.isdigit():              # validate input - no digit
                print("\n[ Invalid brand - string only  ]\n")
                brand1 = "NoBrand"
                invalid += 1
            else:
                brand1 = brand1.upper()

            place1 = input("Origin place: ")
            if place1.isdigit():
                print("\n[ Invalid place - string only ]\n")
                place1 = "NoPlace"
                invalid += 1
            else:
                place1 = place1.capitalize()

            print("Year was founded: ", end=" ")
            try:
                year1 = int(input())
                if int(year1):               # validate input - no string
                    year1 = year1              # nothing happen here - just placeholder
            except ValueError:
                print("\n[ Invalid year - number only ]")
                invalid += 1

            sport_car_response = input("Is this a sport car (y/n): ").lower()     # make user input to lower case
            if sport_car_response == 'y':
                one_sport_car = True
            elif sport_car_response == 'n':
                one_sport_car = False
            else:
                print("\n[ Invalid response ]")

            print("\n> 2nd car")
            brand2 = input("Brand: ")
            if brand2.isdigit():
                print("\n[ Invalid brand - string only ]\n")
                invalid += 1
            else:
                brand2 = brand2.upper()

            place2 = input("Origin place: ")
            if place2.isdigit():
                print("\n[ Invalid place - string only ]\n")
                invalid += 1
            else:
                place2 = place2.capitalize()

            try:
                print("Year was founded: ", end=" ")
                year2 = int(input())
                if int(year2):
                    year2 = year2          # nothing happen here - just placeholder
            except ValueError:
                print("\n[ Invalid year - number only ]\n")
                invalid += 1

            sport_car_response = input("Is this a sport car (y/n): ").lower()  # make user input to lower case
            if sport_car_response == 'y':
                two_sport_car = True
            elif sport_car_response == 'n':
                two_sport_car = False
            else:
                print("\n[ Invalid response ]")

            invalid -= 1
            if invalid == 0:                        # only if there is nothing wrong then update the value
                one_car = OCar(brand1, place1, year1)
                two_car = TCar(brand2, place2, year2)
                print("\n== Data updated ==\n")
            elif invalid > 0:
                print("\n== Update failed ==\n")

        elif choice == '2':
            print("\n[ Display Data ]")
            if invalid == 0:
                print("\n> 1st Car")
                one_car.the_brand()
                one_car.the_place()
                one_car.the_year()
                if one_sport_car:
                    one_car.sport_car()                # cant use parent class directly to call - ex; Car.sport_car() <- this won't work
                else:
                    one_car.no_sport_car()
                print("\n---------------\n")
                print("> 2nd Car")
                two_car.the_brand()
                two_car.the_place()
                two_car.the_year()
                if two_sport_car:
                    two_car.sport_car()
                else:
                    two_car.no_sport_car()

            else:
                print("\n[ No Data Updated ]")
                print("\n> 1st Car")
                print("No brand")
                print("No origin place")
                print("No year")
                print("\n> 2nd Car")
                print("No brand")
                print("No origin place")
                print("No year")

        else:
            print("\n[ Invalid choice ]")

        print("\n== Cars Menu ==")
        print("1. Input data")
        print("2. Display data")
        print("E. Exit")
        choice = input("choice; ")

    if choice == 'e' or choice == 'E':
        print("\n== Exit Program ==")

except KeyboardInterrupt:
    print("\n\n== Program Stopped ==")

