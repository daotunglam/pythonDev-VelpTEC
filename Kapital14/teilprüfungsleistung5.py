import time

damals1 = time.mktime((1979, 10, 15, 23, 55, 0, 0, 0, 0))
damals2 = time.mktime((2022, 1, 20, 0, 0, 0, 0, 0, 0))

diff = damals2 - damals1
diffTage = diff/60/60/24

print("Es sind: ", int(diffTage / 365), "Jahre und ", int(diffTage % 365), " Tage vergangen.")