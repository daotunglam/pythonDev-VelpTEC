from re import *
def linkfind(datei):
    re = compile('https?://.+html?', I) #1
    f = open(datei,'r')
    text = f.read()
    f.close()
    return re.findall(text) #2

linkliste = linkfind('LICENSE.txt')
print('Wir finden ein Links in der Python-LICENSE-Datei:')
for link in linkliste:
    print(link)