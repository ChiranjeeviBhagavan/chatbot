from random import random

import torch
from torch import device

from QATrain import tokenize, BagOfWords
from dataset import readIntent
from nn import NeuralNetModel


def predictChattyAnswer():
    # loading the data we saved before
    FILE = "./DATA.pth"
    data = torch.load(FILE)

    # defining values
    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_the_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    # lets print the model now.
    model = NeuralNetModel(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()


    bot_name = "FinBot"
    #for taking the input
    name=input("Enter Your Name: ")
    print("FinBot:Hey, Let's chat! (type 'quit' to exit)Also when you start bargaining give digits")
    while True:
      #once the person types his name, then from the next chat onwards the name will be shown
        sent=input(name+':')
        if sent == "quit":
            break
        #since im going to offer bargaining offer for only one product and its rated price is 30 Rs.
        #However the person will tell only numbers ranging from 1 to 30
        sent = tokenize(sent)
        X = BagOfWords(sent, all_the_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in readIntent(): ##intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        else:
            print(f"{bot_name}: I do not understand...")


#predictChattyAnswer()
