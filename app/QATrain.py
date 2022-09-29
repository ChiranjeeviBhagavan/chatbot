import numpy as np
import random
import json
import torch
import torch.nn as nn
#importing nltk and necessary downloads
import nltk

from app.dataset import writeTOJsonFile, readIntent

nltk.download('punkt')
#Im using porter stemmer here
from nltk.stem.porter import PorterStemmer
from torch.utils.data import Dataset, DataLoader
nltk.download('all')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def BagOfWords(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    Bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            Bag[idx] = 1
    return Bag



#for collecting all the words, lets create an empty list
all_the_words = []
#for collecting all the tags
tags = []
#the below pair list which will be  made filled with both patterns and their tags
pair = []
# loop through each sentence in our intents patterns
intents = readIntent()

for intent in intents['intents']:
    tag = intent['tag']
    # adding this to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenizing each word in the sentence
        w = tokenize(pattern)
        # addding to our words list(since w is an array we need to use extend for adding the elements)
        all_the_words.extend(w)
        # add to pair
        pair.append((w, tag))

# stem and lower each word. So, first excluding punctuation marks
ignore_words = ['?', '.', '!',',']
all_the_words = [stem(w) for w in all_the_words if w not in ignore_words]
# remove duplicates and sort
all_the_words = sorted(set(all_the_words))
tags = sorted(set(tags))

print(len(pair), "patterns")
print(len(tags), "tags:", tags)
print(len(all_the_words), "unique stemmed words:", all_the_words)