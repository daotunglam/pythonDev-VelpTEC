import random
numbersList = [random.randint(0, 1000) for _ in range(10)]
print(numbersList)
def insertion_sort():
    for i, nr in enumerate(numbersList):
        if nr > numbersList[i+1]:
            numbersList[i+1] = nr
            print(numbersList)
    
insertion_sort()