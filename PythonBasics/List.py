num = [1, 2, 3, 4, 5, 6, 7, 1]

print(len(num)) # return total item counts in an list.

print(num.count(2)) # counts number of occurance of item.

num.sort() # Sorts the list.
print(num)

num.remove(1)
print(num) # remove item from list.

num.pop(2)
print(num) # remove item at given index.

num.insert(2, 1000)
print(num) # insert item at given index.

num.append(9)
print(num) # append item at last pos. in list.

## Slicing

print(num[2: 5]) # [start: end] index
print(num[2: ]) # [start: end] index

print(num[2: 8: 2]) # [start: end: steps]
print(num[2: :2]) # [start: end: steps] index

print(num[8: 2: -1]) # [start: end: steps]

