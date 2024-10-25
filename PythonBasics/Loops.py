myList = [1,2,3,4,5,6,7,8,9,10]

for i in myList:
    print(i)

for i in range(10,15):
    print(i)

while i < 5:
    if i == 3:
        continue
    print(i)
    i += 1

while i < 5:
    if i == 3:
        continue
    print(i)
    i += 1
else:
    print("Loop ended")
