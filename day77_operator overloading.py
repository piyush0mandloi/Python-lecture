class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 1)

p3 = p1 + p2
print(p3)

# ⭐ More operators you can overload
# Operator	        Method
# +	                __add__
# -	                __sub__
# *	                __mul__
# /	                __truediv__
# ==                __eq__
# <	                __lt__
# >	                __gt__
# []                __getitem__