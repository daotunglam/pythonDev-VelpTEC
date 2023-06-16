def process_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    # Umwandlung in Kleinbuchstaben
    text = text.lower()
    
    # Erstellung einer Liste mit allen Worten
    word_list = text.split()
    
    # Initialisierung eines leeren Dictionaries für jedes Wort
    word_dict_list = []
    
    # Zählen der Anzahl von 'e' pro Wort und Speichern in den Dictionaries
    for word in word_list:
        e_count = word.count('e')
        word_dict = {'word': word, 'e_count': e_count}
        word_dict_list.append(word_dict)
    
    # Bestimmung des Wortes mit der höchsten Anzahl von 'e'
    word_dict_list.sort(key=lambda x: x['e_count'], reverse=True)
    most_e_word = word_dict_list[0]['word']
    
    # Kodierung des Texts in UTF-8
    encoded_text = text.encode('utf-8')
    
    return encoded_text, word_dict_list


text_file = 'Kapital13/sometext.txt'  # Dateiname des Textdokuments
encoded_text, word_list = process_text(text_file)

# Ausgabe des encodierten Texts und der Wortliste
print(encoded_text)
print(word_list)
