#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if not sentence:
        return 0, None
    else:
        FirstCharacter = sentence[0]
        return length, FirstCharacter
