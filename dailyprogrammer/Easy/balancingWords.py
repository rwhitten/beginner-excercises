#https://www.reddit.com/r/dailyprogrammer/comments/3c9a9h/20150706_challenge_222_easy_balancing_words/

from string import ascii_uppercase

alphabet = dict.fromkeys(ascii_uppercase)

# Assign values to letters
counter = 1
for c in ascii_uppercase:
    alphabet[c] = counter
    counter += 1

def balance(entry):
    # Weight on either side
    left, right = 0, 0

    for idx,val in enumerate(entry):
        # Calculate leftweight
        for subidx,subval in enumerate(reversed(entry[0:idx])):
            left = (left + ((subidx + 1) * alphabet[subval]))

        # Calculate rightweight
        for subidx,subval in enumerate(entry[idx+1:]):
            right = (right + (subidx +1) * alphabet[subval])

        # Check if balanced
        if left == right:
            print(entry[:idx], val, entry[idx+1:], '-', left)
            break
        
        # Check if impossible to balance
        elif right < left:
            print(entry, 'DOES NOT BALANCE')
            break

        # Reset weights
        left, right = 0, 0


balance('CONSUBSTANTIATION')
balance('WRONGHEADED')
balance('UNINTELLIGIBILITY')
balance('SUPERGLUE')