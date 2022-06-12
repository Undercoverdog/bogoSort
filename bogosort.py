import numpy as np
import random


# generates and return a random array
def randomArray():
    length = random.randint(1, 105)
    arr = np.empty(length, dtype=int)
    for i in range(0, length):
        r = random.randint(-100, 100)
        arr[i] = r
    return arr

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

# bogo sort
def bogoSort(pArray):
    print("Start" + str(pArray))
    while not checkArray(pArray):
        shuffleArray(pArray)
    return pArray


print("End result" + str(bogoSort(randomArray())))
