import random
import time

random_nr = random.randint(1,8)

mal = 1

while mal <= 6:
    print(mal, 'Versuch:')
    raten = input('Was is die Nummer?')
    
    if int(raten) == random_nr:
        print('richtig')
        break
    else:
        print('Nein. Noch', 6 - mal, 'mals.')
        mal += 1
        time.sleep(1)