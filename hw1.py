# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 01:12:55 2017

@author: Ryan
"""

lines = []
for line in open('building_global_community.txt'):
    line = line.strip()
    lines.append(line)
import nltk
nltk.download("stopwords")    
    

from nltk.corpus import stopwords
from collections import Counter

word_all = []
for line in lines: 
    wordcut = line.split(" ")
    v1word = [word.lower() for word in wordcut if word.isalpha()]
    stopword_e = set(stopwords.words('english'))
    v2word = [word for word in v1word if word not in stopword_e]
    word_all = word_all + v2word
    
wordCounter = Counter(word_all)

import csv
with open('wordcount.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in wordCounter.most_common():
        writer.writerow({'word': word, 'count': count})
        