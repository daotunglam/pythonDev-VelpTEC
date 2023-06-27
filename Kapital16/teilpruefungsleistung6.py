from tkinter import *

fenster = Tk()
fenster.title('Teilprüfungsleistung 6')

label1 = Label(fenster, text='Hello darkness',
width=10, height=10, bg='black', fg='white', padx=5, pady=5)
label1.grid(row=0, column=0, padx=10)

label2 = Label(fenster, text='My old friend',
width=10, height=10, bg='blue', fg='red', padx=5, pady=5)
label2.grid(row=0, column=1, padx=10)

label3 = Label(fenster, text='I am so dark',
width=10, height=10, bg='white', fg='green', padx=5, pady=5)
label3.grid(row=1, column=0, padx=10)

label4 = Label(fenster, text='It has no end',
width=10, height=10, bg='green', fg='white', padx=5, pady=5)
label4.grid(row=1, column=1, padx=10)

label5 = Label(fenster, text='Bitte einen Text eingeben', padx=5, pady=5)
label5.grid(row=2, column=0, columnspan=2, sticky='n')

textfeld = Text(master=fenster, width=20, height=1, wrap='word')
textfeld.grid(row=3, column=0, columnspan=2, sticky='n', padx=10, pady=10)

mainloop()
