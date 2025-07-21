names=["Piyush","Neeraj","Ayush"]
ages=[21,20,21]
paired = list(zip(names,ages))
print(paired)

l=[20,30,40]
l2=[1,5,8]
product = [x*y for x,y in zip(l,l2)]
print(product)