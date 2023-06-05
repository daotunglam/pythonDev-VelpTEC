import random
import string

alphabet = string.ascii_lowercase

def stringGeneration(length):
    generated_str = ''
    for _ in range(length):
        index = random.choice(alphabet)
        generated_str += index
    return generated_str

print(stringGeneration(4) + str(random.randint(50, 100)) + stringGeneration(3) + str(random.randint(100, 1000)))

