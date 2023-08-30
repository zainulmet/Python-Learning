class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product):
        self.items.append(product)
    
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

# List of available products
products = [
    Product("Item 1", 10.99),
    Product("Item 2", 5.99),
    Product("Item 3", 7.49)
]

# Create a shopping cart
cart = ShoppingCart()

print("Welcome to the Online Shopping Simulation!")
print("Available Products:")
for idx, product in enumerate(products, start=1):
    print(f"{idx}. {product.name} - ${product.price:.2f}")

while True:
    choice = input("Enter the number of the product to add to cart (0 to checkout): ")
    
    if choice == '0':
        break
    
    try:
        choice_idx = int(choice) - 1
        selected_product = products[choice_idx]
        cart.add_item(selected_product)
        print(f"{selected_product.name} added to cart.")
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid product number.")

total_price = cart.calculate_total()
print(f"Total price of items in cart: ${total_price:.2f}")
