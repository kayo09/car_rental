import datetime
from modules import customer_module
#rental time and bill function 

class Rentals(customer_module.Customer):
    car_rented=[]
    _cars=["honda","porsche","ford","tesla"]
    name=_cars
    # current_time=datetime.datetime.now()

    def __init__(self):
       pass 
        #self.car_rented=[]
        # self._cars=["honda","porsche","ford","tesla"]

    def get_available_cars(self):
        print("Available cars: ",self._cars)
        return self._cars
    
    def get_rented_cars(self):
        return self.car_rented
    
    def rent_car(self,car,customer):
      
        weeks=input("weeks: ")or int("0")
        days=input("days: ")or int("0")
        hours=input("hours: " )or int("0")
        print(customer.name,":",datetime.datetime.now())
        rental_duration=datetime.datetime.now()+datetime.timedelta(hours=int(hours)+(int(days)*24)+(int(weeks)*168))
        if(len(self._cars)>=1):
            customer._cars.remove(car)
            customer.car_rented.append(car)
            print("Car rented successfully until ", rental_duration)
        else: 
            raise Exception("Out of cars :(")

        return customer.car_rented 

    def return_car(self,car,customer):
        if(car in customer.car_rented):
            customer._cars.append(car)
            customer.car_rented.remove(car)
        else:
            raise Exception("Car not rented")
        return "Car returned successfully"
