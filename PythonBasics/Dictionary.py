myDict = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

print(myDict.get("name"))

print("\nAdding new key-value pair")
myDict["married"] = True
print(myDict)

print("\nLooping through dictionary")
for x in myDict:
    print(x)

print("\nLooping through dictionary with values")
for x, y in myDict.items(): # x is the key, y is the value
    print(x, y)

print("\nNew Dictionary with copy")
myDict2 = myDict.copy() # copies the dictionary
myDict2.pop("married") # removes the key-value pair
print(myDict2)

print("\npopping items")
myDict.pop("age") # removes the key-value pair
print(myDict)

print("\ndeleting items")
del myDict["married"] # removes the key-value pair
print(myDict)

print("\nclearing dictionary")
myDict.clear() # removes all key-value pairs
print(myDict)

print("\ndeleting dictionary")
del myDict

