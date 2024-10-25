import math
import random

## importing module with alias 'f' to shorten the name.
import math as m
import Functions as f 

print("\ncalling multiple function from Functions.py")
val = f.multiple(2, 3)
print(val)

print("\nusing math module")
print(m.sqrt(16))

print("\nusing random module")
print(random.randint(1,10))

print("\nusing random module to get random item from list")
listItems = ["apple", "banana", "cherry"]
print(random.choice(listItems))