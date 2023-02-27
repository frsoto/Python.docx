
# from __future__ import annotations
#
# def letter_frequency(sentence: str) -> dict[str, int]:
#     frequencies: dict[str, int] = {}
#     for letter in sentence:
#         frequency = frequencies.setdefault(letter, 0)
#         #devuelve el valor de la key si esta, si no esta crea la entrada con leeter con y 0 y ademas devuelve 0
#         frequencies[letter] = frequency + 1
#     return frequencies
#
# print(letter_frequency("Hola Mundo"))


#################################################################################
# from collections import defaultdict
# def letter_frequency_2(sentence: str) :
#     frequencies: defaultdict[str, int] = defaultdict(int)
#     for letter in sentence:
#         frequencies[letter] += 1
#     return frequencies
#
# print(letter_frequency_2("Hola Mundo"))



#################################################################################
from __future__ import annotations
import string

CHARACTERS = list(string.ascii_letters) + [" "]

def letter_frequency(sentence: str) -> list[tuple[str, int]]:
    frequencies = [(c, 0) for c in CHARACTERS]

    for letter in sentence:
        index = CHARACTERS.index(letter) #sino encuentra la letra
        frequencies[index] = (letter, frequencies[index][1] + 1)

    non_zero = [ (letter, count) for letter, count in frequencies if count > 0 ]
    return non_zero


print(letter_frequency("Hola Mundo"))
