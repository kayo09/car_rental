import sqlite3

def create_tables():
    conn = sqlite3.connect('car_rental.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY, name TEXT, available BOOLEAN)''')
    c.execute('''CREATE TABLE IF NOT EXISTS rentals (id INTEGER PRIMARY KEY, customer_name TEXT, car_name TEXT, return_date TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
