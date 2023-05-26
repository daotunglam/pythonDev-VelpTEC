text = input('Text eingeben: ')

def textAnalyse(text):
    # Entfernen der Interpunktionszeichen
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    words = [word.strip(punctuations) for word in words]

    # Text in einzelne Worte aufspalten
    words = text.split()  

    word_lengths = [len(word) for word in words]  # Liste mit Zeichenzahlen der Worte erstellen
    min_length = min(word_lengths)  # Minimum der Zeichenzahlen bestimmen
    max_length = max(word_lengths)  # Maximum der Zeichenzahlen bestimmen
    total_length = sum(word_lengths)  # Gesamtzeichenanzahl bestimmen

    return word_lengths, max_length, min_length, total_length

lengths, maximum, minimum, total = textAnalyse(text)
print("Zeichenzahlen der Worte:", lengths)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Gesamtzeichenzahl:", total)
