class Product:
    def __init__(self, name, price, tags):
        self.name = name
        self.price = price
        self.tags = set(tags)  # Use set to store unique tags

    def display_info(self):
        print(f"{self.name} - Rs.{self.price} | Tags: {', '.join(self.tags)}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []  # List to store multiple products (order matters)

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.name} added to {self.name}'s cart")

    def view_cart(self):
        print(f"\n{self.name}'s Shopping Cart:")
        for item in self.cart:
            item.display_info()


class Store:
    store_hours = ("9:00 AM", "9:00 PM")  # Tuple - fixed store hours

    @staticmethod
    def show_hours():
        print(f"Store Hours: {Store.store_hours[0]} to {Store.store_hours[1]}")

# Create Products
p1 = Product("Laptop", 75000, ["electronics", "computers", "electronics"])
p2 = Product("Shoes", 2500, ["fashion", "footwear"])
p3 = Product("Phone", 30000, ["electronics", "mobile"])

# Create Customer
cust1 = Customer("Alice")

# Interact with the system
cust1.add_to_cart(p1)
cust1.add_to_cart(p2)
cust1.view_cart()

# Show Store Hours
Store.show_hours()