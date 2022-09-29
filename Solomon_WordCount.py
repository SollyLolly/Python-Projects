#!/usr/bin/env python
# coding: utf-8

# In[72]:


import nltk
import string
nltk.download('omw-1.4')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import json
from pprint import pprint
def read_text_file(path_of_file):
       f = open(path_of_file, "r")  
       str1 = f.read()
       words=str1.split() 
       w_clean = [''.join(c for c in word if c not in string.punctuation) for word in words] 

       stopWords = set(stopwords.words('english'))
       wordsFiltered = []
     
       for w in w_clean:
        if w not in stopWords:
         wordsFiltered.append(w)
       filter = wordsFiltered
       
       wordnet_lemmatizer = WordNetLemmatizer()
       lemma=[]
       for word in filter:
        if word not in wordnet_lemmatizer.lemmatize(word): 
         lemma.append(word)
       
       freq_occur=dict()
       for word in lemma:
         if word in freq_occur:
            freq_occur[word] += 1
         else:
            freq_occur[word] = 1

       with open("sample.json", "w") as outfile:
        json.dump(freq_occur, outfile) 
    
    

       

       f.close() 
read_text_file("flatland.txt")


# In[ ]:




