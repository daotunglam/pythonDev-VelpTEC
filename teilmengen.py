import random

numbersList1 = [random.randint(0, 10) for _ in range(5)]
numbersList2 = [random.randint(0, 10) for _ in range(5)]

def mengen(list1, list2):
    list1 = set(list1)
    list2 = set(list2)