inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# output of current layer
layer_output = []

# for each neuron in the layer
for n_weights, n_biases in zip(weights, biases):
	# zeroes out output for given neuron
	output = 0
	# loop through each input and weight for the neuron
	for n_input, weight in zip(inputs, n_weights):
		#multiply input by associated weight and add to neurons output value
		output += n_input*weight
	output += n_biases
	layer_output.append(output) 

print(layer_output)
#this is a fully connected neuron. every neuron is connected to every input