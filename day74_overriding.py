# Imagine you have a general payment class, and then different payment methods override the same method.

# Parent Class
class Payment:
    def pay(self, amount):
        print(f"Paying {amount} using generic method")


# Child Classes (Overriding the pay() method)
class UPI(Payment):
    def pay(self, amount):
        print(f"Paying {amount} via UPI (Google Pay / PhonePe)")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

p1 = UPI()
p1.pay(500)

p2 = CreditCard()
p2.pay(1200)

# -------------------------------------------------------------------------

# ⭐ Example — Logging Before and After Payment

# Suppose you have a base payment class that does a basic payment.
# Now the child wants to extend the behavior, not completely replace it.

class Payment:
    def pay(self, amount):
        print(f"Processing payment of {amount}...")

# ✅ Child Class (Overriding + calling parent using super())
class UPI(Payment):
    def pay(self, amount):
        print("Starting UPI transaction...")
        
        # Call parent method
        super().pay(amount)
        
        print("UPI payment successful!")


p = UPI()
p.pay(800)
