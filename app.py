import psycopg2
from psycopg2 import sql

class Shop:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        # Connect to the PostgreSQL database
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Create the products table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                               id SERIAL PRIMARY KEY,
                               name TEXT NOT NULL,
                               price REAL NOT NULL)''')
        self.connection.commit()

    def add_product(self, name, price):
        # Insert a new product into the database
        self.cursor.execute('''INSERT INTO products (name, price) VALUES (%s, %s)''', (name, price))
        self.connection.commit()

    def remove_product(self, product_id):
        # Remove a product from the database by ID
        self.cursor.execute('''DELETE FROM products WHERE id = %s''', (product_id,))
        self.connection.commit()

    def list_products(self):
        # List all products from the database
        self.cursor.execute('''SELECT * FROM products''')
        return self.cursor.fetchall()

    def close(self):
        # Close the database connection
        self.connection.close()

if __name__ == "__main__":
    # Connect to the PostgreSQL database
    shop = Shop(db_name="shopdb", db_user="postgres", db_password="password", db_host="db", db_port="5432")
    
    while True:
        print("\n1. Add Product")
        print("2. Remove Product")
        print("3. List Products")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            shop.add_product(name, price)
        elif choice == "2":
            product_id = int(input("Enter product ID to remove: "))
            shop.remove_product(product_id)
        elif choice == "3":
            products = shop.list_products()
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
        elif choice == "4":
            shop.close()
            break
