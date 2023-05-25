# Schreibe eine while-Schleife, die im Sekundentakt einen Text in der Konsole ausgibt.

# Die while-Schleife soll alle Zahlen von 1 bis 100 durchgehen.
# Wenn die Zahl gerade ist, print: „Ich fühle mich gerade“
# Wenn die Zahl durch 3 teilbar ist, print: „Drei ist schön“
# Wenn die Zahl durch 5 teilbar ist, print: „Ich teile alles durch 5“
# In allen übrigen Fällen: „Ich bin besonders“

import time

i=1

while i <= 100 :
    if i%2==0:
        print('Ich fühle mich gerade')
    elif i%3==0:
        print('Drei ist schön')
    elif i%5==0:
        print('Ich teile alles durch 5')
    else:
        print('Ich bin besonders')
    i += 1
    time.sleep(1)