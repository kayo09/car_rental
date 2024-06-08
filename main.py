from modules import car_rental_module 
from modules import customer_module

customers=[]


def customer_init():
 
    name=input("Please enter your name")
    rental=car_rental_module.Rentals()
    rental.name=name
    # customer=customer_module.Customer(name)
    # customers.append(customer_module.Customer(customer))
    print("HELLO "+name)
    print("Welcome to the car rental system")
    print("Please choose from the following options")
    print("1. Rent a car")
    print("2. Return a car")
    print("3. Exit")
    available_cars=rental.get_available_cars()
    choice=int(input())
    car=input("please enter the car name")



    if choice==1:
        if(car in available_cars):
            rental.rent_car(car,rental)
        else: 
            print("Car is not available")
            customer_init()
    elif choice==2:
        print(available_cars)
        if(car in rental.car_rented):
            rental.return_car(car,rental)
            print("Car has been returned, Thank You")
        else:
            print("Car is not rented")
            customer_init()
    elif choice==3:
        print("Thank you for using the car rental system")
    else:
        print("Invalid choice")
        print(available_cars)
        customer_init()
    
    return rental

while(True):
    customers.append(customer_init())
    
