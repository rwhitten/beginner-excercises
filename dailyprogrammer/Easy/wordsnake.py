#https://www.reddit.com/r/dailyprogrammer/comments/3bi5na/20150629_challenge_221_easy_word_snake/
#I took the easy way out with this snake. It only prints right and down.

#words = "SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE"
#words = "CAN NINCOMPOOP PANTS SCRIMSHAW WASTELAND DIRK KOMBAT TEMP PLUNGE ESTER REGRET TOMBOY"
    words = ("NICKEL LEDERHOSEN NARCOTRAFFICANTE EAT TO OATS SOUP PAST TELEMARKETER RUST THINGAMAJIG GROSS SALTPETER REISSUE ELEPHANTITIS").split()

    #lay down base word
    print(words[0])

    #direction last word was written. 0 = right; 1 = down
    direction = 0
    #whitespace needed
    padding = len(words[0]) - 1

    for word in words[1:]:
        #go down
        if direction == 0:
            for char in word[1:-1]:
                print(' ' * padding + char)
            direction = 1
        #go right
        elif direction == 1:
            print(' ' * padding + word)
            padding = padding + len(word) - 1
            direction = 0;
