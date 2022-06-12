import numpy as np
import random


# generates and return a random array
def randomArray():
    low = int(input("Lowest possible length "))
    high = int(input("Highest possible length "))

    length = random.randint(low, high)
    arr = np.empty(length, dtype=int)
    for i in range(0, length):
        r = random.randint(-100, 100)
        arr[i] = r
    return arr

def fillArray(pNumbers):
    tempList = pNumbers.split (",")
    tempArr = np.empty(len(tempList), dtype=int)
    for i in range(0, len(tempList)):
        tempArr[i] = tempList[i]
    return tempArr



# shuffles and returns an array
def shuffleArray(pArray):
    y = len(pArray) - 1
    for i in range(0, y):
        x = random.randint(i, y)
        pArray[i], pArray[x] = pArray[x], pArray[i]
    return pArray


# checks if the array is sorted ascending and returns True or False
def checkArray(pArray):
    y = len(pArray) - 1
    for i in range(0, y):
        if pArray[i] > pArray[i + 1]:
            return False

    return True

# calculate amount of possible combinations
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# bogo sort
def bogoSort(pArray):
    print("Start" + str(pArray))
    print("Possible combinations: " + str(factorial(len(pArray))))
    while not checkArray(pArray):
        shuffleArray(pArray)
    return pArray




mode = input("[R]andom or [c]ustom array? ")
mode = mode.lower()
if mode == "c" or mode  == "custom":
    numbers = str(input("Enter comma separated integers. e.g. 1,2,3,4,5: "))
    arr = fillArray(numbers)
else:
    arr = randomArray();
    
result = str(bogoSort(arr))


print("End result: " + result)

