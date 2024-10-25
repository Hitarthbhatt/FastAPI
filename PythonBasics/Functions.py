def printMyName(firstName, lastName):
    print(firstName + " " + lastName)

printMyName("John", "Doe")

def multiple(a, b):
    return a * b

val = multiple(2, 3)
print(val)

def printList(myList):
    for i in myList:
        print(i)

printList([1,2,3,4,5])

def getUserDetails(firstName, lastName, age):
    return {"firstName": firstName,
            "lastName": lastName,  
            "age": age
            }
    
print(getUserDetails("John", "Doe", 30))