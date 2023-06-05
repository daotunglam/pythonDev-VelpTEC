import string
punctuation = string.punctuation

def textAnalysis(text):
    text = ''.join(char for char in text if char not in punctuation)
    words = text.split()
    wordLengths = [len(word) for word in words]

    average = sum(wordLengths) / len(wordLengths)

    lettersAndAmount = []
    for letter in text:
        lettersAndAmount.append((letter, text.count(letter)))
    lettersAndAmount = set(lettersAndAmount)

    print(average, lettersAndAmount)

textAnalysis(input('Text eingeben: '))