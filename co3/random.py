import random

random.seed(10)
print(random.random())
print(random.getstate())
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
print(random.uniform(20, 60))
print(random.triangular(20, 60, 30))
