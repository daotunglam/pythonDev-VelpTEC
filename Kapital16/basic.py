from tkinter import *

def button_action():
    entry_text = textfeld1.get()
    if (entry_text == ''):
        welcome_label.config(text = 'Du musst etwas eingeben.')
    else:
        entry_text = 'Welcome ' + entry_text + '!'
        welcome_label.config(text = entry_text)

fenster = Tk()
fenster.title('Textanalyse')

def wortzahl():
    entry_text = textfeld1.get('1.0', 'end')
    text = str(entry_text)
    worte = text.split()
    wortzahl = len(worte)
    result = 'Anzahl der Worte: ' + str(wortzahl)
    wortlabel.config(text = result)

my_label = Label(fenster, text = 'Gib einen Text ein')

welcome_label = Label(fenster)

textfeld1 = Text(master=fenster, width=39, height=4, wrap='word')
wortzahl_button = Button(fenster, text='Anzahl der Worte', command=wortzahl)

my_label.grid(row=0, column=0)
textfeld1.grid(row=0, column=1)
wortzahl_button.grid(row=1, column=0, pady=30, padx=30)
welcome_label.grid(row=1, column=1, padx=30, pady=30)

wortlabel = Label(fenster, text='Die Anzahl der Worte ist: ')
wortlabel.grid(row=1, column=1, padx=30, pady=30)
mainloop()