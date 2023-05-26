text = input('Text eingeben: ')
def frequencyAnalysis(text):
    letters = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    
    return list(letters.items())

listLetters = frequencyAnalysis(text)

def maxFrequencLetter(listLetters):
    maxFrequencLetter = ''
    maxFrequency = 0
    for letter, frequency in listLetters:
        if frequency > maxFrequency:
            maxFrequency = frequency
            maxFrequencLetter = letter
    return (maxFrequencLetter, maxFrequency)

print(maxFrequencLetter(listLetters))