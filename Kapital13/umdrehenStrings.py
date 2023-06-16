def umdrehenStrings(string):
    listChars = list(string)
    listChars.reverse()
    reversed_string = ''.join(listChars)
    return reversed_string

print(umdrehenStrings('12345'))