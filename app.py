from flask import Flask, request, jsonify 
from modules import car_rental_module,customer_module
import threading 
import sqlite3

app=Flask(__name__)

def get_available_cars():
    conn=sqlite3.connect('car_rental.db')
    c=conn.cursor()
    c.execute("SELECT name FROM cars WHERE available=1")
    available_cars=[row[0] for row in c.fetchall()]
    conn.close()
    return available_cars

def rent_car_db(car, customer_name):
    conn = sqlite3.connect('car_rental.db')
    c = conn.cursor()
    c.execute("UPDATE cars SET available=0 WHERE name=?", (car,))
    c.execute("INSERT INTO rentals (customer_name, car_name) VALUES (?, ?)", (customer_name, car))
    conn.commit()
    conn.close()

def return_car_db(car, customer_name):
    conn = sqlite3.connect('car_rental.db')
    c = conn.cursor()
    c.execute("UPDATE cars SET available=1 WHERE name=?", (car,))
    c.execute("DELETE FROM rentals WHERE customer_name=? AND car_name=?", (customer_name, car))
    conn.commit()
    conn.close()

@app.route('/rent', methods=['POST'])
"""curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "car": "honda"}' http://127.0.0.1:5000/rent"""
def rent_car():
    data = request.json
    name = data.get('name')
    car = data.get('car')
    available_cars = get_available_cars()
    if car in available_cars:
        rent_car_db(car, name)
        return jsonify({"message": "Car rented successfully!"}), 200
    else:
        return jsonify({"message": "Car is not available"}), 400

@app.route('/return', methods=['POST'])
def return_car():
    data = request.json
    name = data.get('name')
    car = data.get('car')
    rented_cars = get_rented_cars_db(name)
    if car in rented_cars:
        return_car_db(car, name)
        return jsonify({"message": "Car returned successfully!"}), 200
    else:
        return jsonify({"message": "Car is not rented"}), 400

def get_rented_cars_db(customer_name):
    conn = sqlite3.connect('car_rental.db')
    c = conn.cursor()
    c.execute("SELECT car_name FROM rentals WHERE customer_name=?", (customer_name,))
    rented_cars = [row[0] for row in c.fetchall()]
    conn.close()
    return rented_cars

def sanitize_input(user_input):
    import re
    return re.sub(r'[^\w\s]', '', user_input)

def customer_init():
    name = sanitize_input(input("Please enter your name"))
    rental = car_rental_module.Rentals()
    rental.name = name
    print("HELLO " + name)
    print("Welcome to the car rental system")
    print("Please choose from the following options")
    print("1. Rent a car")
    print("2. Return a car")
    print("3. Exit")
    available_cars = get_available_cars()
    choice = int(input())
    car = sanitize_input(input("Please enter the car name"))

    if choice == 1:
        if car in available_cars:
            rent_car_db(car, name)
            print("Car rented successfully!")
        else:
            print("Car is not available")
            customer_init()
    elif choice == 2:
        rented_cars = get_rented_cars_db(name)
        if car in rented_cars:
            return_car_db(car, name)
            print("Car has been returned, Thank You")
        else:
            print("Car is not rented")
            customer_init()
    elif choice == 3:
        print("Thank you for using the car rental system")
    else:
        print("Invalid choice")
        customer_init()

    return rental

def run_customer_init():
    customer_init()

if __name__ == '__main__':
    threading.Thread(target=run_customer_init).start()
    app.run(debug=True)
