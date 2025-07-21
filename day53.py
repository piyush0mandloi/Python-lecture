l=[1,2,3,4,5]
l2=map(lambda x:x*x, l)
print(l2)
print(list(l2))


def square(x):
    return x*x
def cube(x):
    return x**3
nums=[2,3,4]
functions = [square, cube]
result = [ list(map(f,nums)) for f in functions]
print(result)

# 3
names=["Piyuh", "Neeraj", "Ayush"]
greetings = list(map(lambda name: "Hello "+name, names))
print(greetings)

# 4
list1=[1,2,3]
list2=[4,5,6]
sums = list(map(lambda x,y:x+y,list1,list2))
print(sums)


# Filter
def is_even(x):
    return x%2==0
nums=[1,2,3,4,5,6,7,8,9]
evens = list(filter(is_even, nums))
odd= list(filter(lambda x: x%2!=0, nums))
print(evens)
print(odd)


def is_longer_than_3(string):
    return len(string)>5
words=["Piyush", "Neeraj", "Ayush", "Ankit"]
long_words = list(filter(is_longer_than_3, words))
long_words2 = list(filter(lambda x: len(x)>5, words))
print(long_words)
print(long_words2)

# Reduce
from functools import reduce

# List of numbers
numbers = [5, 3, 8, 2, 10]

# Reduce to maximum
from functools import reduce

result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24
