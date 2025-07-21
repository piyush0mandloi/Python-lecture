class Calculator:
    @classmethod
    def add(cls, a, b):
        return a+b
    
    @classmethod
    def subtract(cls, a,b):
        return a-b
    
    @classmethod
    def multiply(cls, a,b):
        return a*b
    
    @classmethod
    def divide(cls, a,b):
        return a/b if b!=0 else "Cannot divide by zero"
    

print("Basic Calculator")
a = float(input("Enter Number: "))
b = float(input("Enter another Number: "))
op = input("Choose opeartion (+,-,*,/): ")

if op == '+':
    print("Result: ", Calculator.add(a,b))
elif op == '-':
        print("Result: ", Calculator.subtract(a,b))
elif op == '*':
         print("Result: ", Calculator.multiply(a,b))
elif op == '/':
    print("Result: ", Calculator.divide(a,b))
else:
      print("Invalid Oparator")