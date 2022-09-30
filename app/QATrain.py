import numpy as np
import random
import json
import torch
import torch.nn as nn
#importing nltk and necessary downloads
import nltk
from dataset import generateJson, readIntent

# nltk.download('punkt')
# nltk.download('all')
#Im using porter stemmer here
from nltk.stem.porter import PorterStemmer
from torch.utils.data import Dataset, DataLoader


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


#
# #for collecting all the words, lets create an empty list
# all_the_words = []
# #for collecting all the tags
# tags = []
# #the below pair list which will be  made filled with both patterns and their tags
# pair = []
# # loop through each sentence in our intents patterns
# intents = readIntent()
#
# for intent in intents['intents']:
#     tag = intent['tag']
#     # adding this to tag list
#     tags.append(tag)
#     for pattern in intent['patterns']:
#         # tokenizing each word in the sentence
#         w = tokenize(pattern)
#         # addding to our words list(since w is an array we need to use extend for adding the elements)
#         all_the_words.extend(w)
#         # add to pair
#         pair.append((w, tag))
#
# # stem and lower each word. So, first excluding punctuation marks
# ignore_words = ['?', '.', '!',',']
# all_the_words = [stem(w) for w in all_the_words if w not in ignore_words]
# # remove duplicates and sort
# all_the_words = sorted(set(all_the_words))
# tags = sorted(set(tags))
#
# print(len(pair), "patterns")
# print(len(tags), "tags:", tags)
# print(len(all_the_words), "unique stemmed words:", all_the_words)
#
#
# # create training data
# X_train = []
# y_train = []
# #using a tuple to run through the pair
# for (pattern_sentence, tag) in pair:
#     # X-->is the bag of words for each pattern_sentence
#     bag = BagOfWords(pattern_sentence, all_the_words)
#     X_train.append(bag)
#     # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot.so defining label
#     label = tags.index(tag)
#     y_train.append(label)
#
# #array
# X_train = np.array(X_train)
# y_train = np.array(y_train)
#
# # Hyper-parameters are--->
# num_epochs = 1000
# batch_size = 8
# learning_rate = 0.001
# #len(X_train[0]) means the length of 1st bag of words because they all have the same size.
# #if we want we can just print and check. But its clear here.
# input_size = len(X_train[0])
# hidden_size = 8
# output_size = len(tags)
# #lets print the values
# print("inputsize=",input_size)
# print("outputsize=",output_size)