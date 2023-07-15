# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:51:58 2023

@author: bertr
"""

import enchant
import itertools

# Open English dictionary via PyEnchant
english_dict = enchant.Dict("en_US")

def generate_words(letters, length, required_letter):
    # Generar todas las combinaciones posibles de letras con la longitud especificada
    # Generate all possible combinations of letters with the specified length
    combinations = itertools.product(letters, repeat=length)
    # Convertir las combinaciones en 
    # Convert the combinations to 
    words = [''.join(combo) for combo in combinations]
    # Filtrar las palabras que no son válidas en inglés y no contienen la letra requerida
    # Filter the words that are valid and do not contain the required letter
    valid_words = filter(lambda word: english_dict.check(word) and required_letter in word, words)
    return valid_words

#use

letters = ["m","a","x","i","b","o","l"]
length = 7
required_letter ='m' 
words = generate_words(letters, length, required_letter)
print(list(words))
