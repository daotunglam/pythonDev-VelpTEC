numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def durch2or3(nr):
    return nr%2==0 or nr%3==0

listNrs=filter(durch2or3, numbers )
print(list(listNrs))