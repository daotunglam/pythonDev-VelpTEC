number_words = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
    'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
}
number_scales = {
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000
}

def wortZuZahl(words):
    words = words.lower().split()
    words.reverse()
    n = 0
    number_scale = 1

    for w in words:
        if w in number_scales:
            number_scale = number_scales[w]
        elif w == 'hundred':
            number_scale *= 100
        elif w in number_words:
            n += number_words[w] * number_scale
        else: print('{} is not a number'.format(w))
        
    return n
    
words = "one hundred million seventy thousand eight hundred and thirty four"
print(wortZuZahl(words))