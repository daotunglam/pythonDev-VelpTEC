class TextAnalysis():
    def __init__(self, text):
        self.text = text # warum brauchen wir das?
        self.words = self.text.split()

    def most_commen_letter(self):
        letterAmounts = [self.text.count(letter) for letter in self.text if letter != ' ']
        return max(letterAmounts)

    def avarageWordLength(self):
        wordLengths = [len(word) for word in self.words]
        return sum(wordLengths) / len(wordLengths)
    
    def wortsAmount(self):
        return len(self.words)

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
a = TextAnalysis(text)
print(a.most_commen_letter())
print(a.avarageWordLength())
print(a.wortsAmount())