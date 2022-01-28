inputs = [1.0, 2.0, 3.0, 2.5] #made up inputs for the beginning. data passed into the model to get desired outpus
weights = [0.2, 0.8, -0.5, 1.0] #weights corresponding to each input that are typically set randomly and change throughout the training of the network
bias = 2.0 #one bias per neuron, similarly, the bias changes as the network is traiend

output = (inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias) #the output is the sum of the produtc of all the inputs and weights, added to the bias

print(output)