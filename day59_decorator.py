# def greet(fx):
#     def mfx():
#         print("good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx


# @greet
# def hello():
#     print("Inside hello function")

# def add(a,b):
#     print(a+b)

# hello()

import datetime
def log_access(func):
    def wrapper(*args, **kwarges):
        print(f"[{datetime.datetime.now()}] Function '{func.__name__}' was called")
        return func(*args, **kwarges)
    return wrapper

@log_access
def view_profile(username):
    print(f"{username} is viewing their profile.")

view_profile("Piyush")
view_profile("Neeraj ")