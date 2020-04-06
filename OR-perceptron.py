import numpy as np


def fill_random():
  return np.random.uniform(-0.09, 0.1, size=(3,1))


def pcn_forward(weights):
  activations = np.dot(data_input,weights)
  return np.where(activations>0,1,0)


def train(weights):
  activations = pcn_forward(weights)
  eta=0.25
  iterations=10
  for i in range(iterations):
    activations = pcn_forward(weights)
    weights += eta*np.dot(np.transpose(data_input),targets-activations)
    #print("Iteración", i)
    #print(weights),
    #print(activations)


#solamente necesito una neurona
bias = -np.ones((4,1))#bias input
data_input = np.array([[0,0],[0,1],[1,0],[1,1]])
data_input = np.concatenate((bias,data_input),axis=1)
targets = np.array([[0],[1],[1],[1]])
weights = fill_random()
train(weights)
