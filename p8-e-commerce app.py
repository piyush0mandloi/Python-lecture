class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Product ID: {self.pid}, Name: {self.name}, Price: ${self.price:.2f}"
    
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = Cart()
    
    def __str__(self):
        return f"User: {self.username}"

class Cart:
    def __init__(self):
        self.items = []
    
    def add_to_cart(self, product):
        self.items.append(product)
        print(f"🛒 Added {product.name} to cart.")
    
    def view_cart(self):
        if not self.items:
            print("🛒 Your cart is empty.")
            return
        print("🛒 Your Cart:")
        total = 0
        for item in self.items:
            print(f'- {item.name} ${item.price:.2f}')
            total += item.price
        print(f"Total: ${total:.2f}")
    
    def checkout(self):
        if not self.items:
            print("🛒 Your cart is empty. Cannot checkout.")
            return
        self.view_cart()
        print("🛒 Checkout successful! Thank you for your purchase!")
        self.items.clear()

class ECommerceApp:
    def __init__(self):
        self.users = {}
        self.products = [
            Product(1, "Laptop", 999.99),
            Product(2, "Smartphone", 499.99),
            Product(3, "Headphones", 199.99),
            Product(4, "Smartwatch", 299.99)
        ]
        self.current_user = None
    
    def register(self):
        username = input("👤 Enter username: ")
        if username in self.users:
            print("⚠️ Username already exists.")
            return
        password = input("🔑 Enter password: ")
        self.users[username] = User(username, password)
        print(f"✅ User {username} registered successfully.")
    
    def login(self):
        username = input("👤 Enter username: ")
        password = input("🔑 Enter password: ")
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            print(f"✅ Welcome back, {username}!")
        else:
            print("⚠️ Invalid username or password.")
        
    def logout(self):
        if self.current_user:
            print(f"👋 Goodbye, {self.current_user.username}!")
            self.current_user = None
        else:
            print("⚠️ No user is currently logged in.")
    
    def add_to_cart(self):
        self.show_products()
        pid = int(input("🆔 Enter product ID to add to cart: "))
        product = next((p for p in self.products if p.pid == pid), None)
        if product:
            self.current_user.cart.add_to_cart(product)
        else:
            print("❌ Product not found.")

    def run(self):
        while True:
            print("\n📱 E-Commerce Menu")
            print("1. Register")
            print("2. Login")
            print("3. View Products")
            print("4. Add to Cart")
            print("5. View Cart")
            print("6. Checkout")
            print("7. Logout")
            print("8. Exit")

            choice = input("🔍 Enter your choice: ")
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.show_products()
            elif choice == '4':
                if self.current_user:
                    self.add_to_cart()
                else:
                    print("⚠️ Please login to add products to your cart")
            elif choice == '5':
                if self.current_user:
                    self.current_user.cart.view_cart()
                else:
                    print("⚠️ Please login to view your cart")
            elif choice == '6':
                if self.current_user:
                    self.current_user.cart.checkout()
                else:
                    print("⚠️ Please login to checkout")
            elif choice == '7':
                self.logout()
            elif choice == '8':
                print("👋 Thank you for using the E-Commerce App!")
                break
            else:
                print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    app = ECommerceApp()
    app.run()