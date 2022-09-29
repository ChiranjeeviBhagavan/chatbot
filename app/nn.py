#creating a new class for our neural network

import torch.nn as nn

class NeuralNetModel(nn.Module):
  #This will be a feed forward neural network with two hidden layer
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetModel, self).__init__()
        #creating the firstlinear layer. This gets the input size and then the connected hiddenlayer
        self.linearlayer1 = nn.Linear(input_size, hidden_size)
        #applying batch normalization
        self.bn1= nn.BatchNorm1d(hidden_size)
        #creating the 1st hidden layer with input size as hiddensize and output size as the hidden size
        self.linearlayer2 = nn.Linear(hidden_size, hidden_size)
        self.bn2= nn.BatchNorm1d(hidden_size)
        #creating the 2nd hidden layer with input size as hiddensize and output size as the num classes
        self.linearlayer3 = nn.Linear(hidden_size, num_classes)
        #using relu activation function
        self.relu = nn.ReLU()
    #implementing the forward pass
    def forward(self, x):
      #apply our first linear layer which gets x as input and then gives out the output
        output = self.linearlayer1(x)
        #activation function
        output = self.relu(output)
      #apply our first linear layer which gets output as input and then gives out the next output
        output = self.linearlayer2(output)
        #activation function
        output = self.relu(output)
        output = self.linearlayer3(output)
        return output