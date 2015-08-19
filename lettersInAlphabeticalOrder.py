alphabet = 'abcdefghijklmnopqrstuvwxyz'

def walk(word, alphabet):
    placeholder = 0
    for c in word:
        if (c in alphabet[placeholder:]):
            placeholder = alphabet.index(c)
        elif (c not in alphabet[placeholder:]):
            return False
    return True

def check(word):
    if (walk(word, alphabet[::-1])):     # Check reverse
        print(word, 'REVERSE ORDER')
    elif (walk(word, alphabet)):         # Check forward
        print(word, 'IN ORDER')
    else:
        print(word, 'NOT IN ORDER')


input = ['billowy', 'biopsy', 'chinos', 'defaced', 'chintz', 'sponged',
          'bijoux', 'abhors', 'fiddle', 'begins', 'chimps', 'wronged']

for x in input:
   check(x)