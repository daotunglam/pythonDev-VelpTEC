alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

liste = [(letter, alphabet.index(letter)) for letter in alphabet]

print(liste)
print(dict(liste))