# -*- coding: utf-8 -*-
"""Solomon_TextCount.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OeOLomdExMP2WIXsJMi6usCmd6GYAmoQ
"""

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""

import string
punctuation_list = list(string.punctuation)
s_lower=s.lower()
words=s_lower.split()
w_clean = [''.join(c for c in word if c not in string.punctuation) for word in words]
unique=[]
for x in w_clean:
    if x not in unique:
        unique.append(x)  
unique=len(unique)     
def word_count(str):
 freq_occur=dict()
 for word in w_clean:
        if word in freq_occur:
            freq_occur[word] += 1
        else:
            freq_occur[word] = 1
 return freq_occur  
print("Word Dictionary: ", word_count(words))
print("Number of distinct words: ", unique)