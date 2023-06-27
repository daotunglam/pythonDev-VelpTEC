einser = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,

        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
}

nullers = {'thousand': 1000, 'million': 1000000, 'billion': 1000000000}

def word2num(s):
    words = s.lower().split(' ')
    num = 0
    nuller = 0
    for w in words:
        if w in einser:
            nuller += einser[w]
        elif w == 'hundred':
            nuller *= 100
        elif w in nullers:
            num = num + nuller * nullers[w]
            nuller = 0
        else:
            print('{} is not a number'.format(w))
    num = num + nuller
    return num

print(word2num("one hundred billion seventy thousand eight hundred thirty four"))