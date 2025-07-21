x,y=2,3
print(f"product of two numbers as {x} and {y} : {(lambda x,y:x*y)(2,3)}")

print((lambda x:x*x*x)(3))

print((lambda x,y,z:(x+y)/z)(2,4,10))

# passing function to another function
cube=lambda x:x*x*x
def sum2cube(x,val):
    return x+val

print(sum2cube(3,cube(3)))