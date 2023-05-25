import time


def countdown(n):
    time.sleep(1)
    if n == 0:
        print("GO!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
