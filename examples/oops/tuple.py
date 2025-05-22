class Store:
    def __init__(self, name):
        self.name = name
        self.hours = ("9:00 AM", "9:00 PM")  # Tuple: fixed data

    def show_hours(self):
        print(f"{self.name} is open from {self.hours[0]} to {self.hours[1]}")

# Example usage
shop = Store("MegaMart")
shop.show_hours()
