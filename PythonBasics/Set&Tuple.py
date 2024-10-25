
##  Set Methods.
print("Set Methods")
mySet = {1, 2, 3, 4, 5, 6, 7, 1, 2}

print(mySet) # set does not allow duplicate value.
mySet.add(10) # add item to set.

mySet.discard(3) # remove item from set. 

mySet.update([8, 9]) # update set.
print(mySet)

mySet.clear() # clear set. 
print(mySet)

##  Tuple Methods.
print("\nTuple Methods")
myTuple = (1, 2, 3, 4)
print(myTuple[0]) # access tuple item.
print(myTuple[0: 2]) # slicing tuple.
print(myTuple.index(4)) # return index of item.

