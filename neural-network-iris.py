import random
import math
from csv import reader

#
# Shorthand:
#   "pd_" as a variable prefix means "partial derivative"
#   "d_" as a variable prefix means "derivative"
#   "_wrt_" is shorthand for "with respect to"
#   "w_ho" and "w_ih" are the index of weights from hidden to output layer neurons and input to hidden layer neurons respectively
#
# Comment references:
#
# [1] Wikipedia article on Backpropagation
#   http://en.wikipedia.org/wiki/Backpropagation#Finding_the_derivative_of_the_error
# [2] Neural Networks for Machine Learning course on Coursera by Geoffrey Hinton
#   https://class.coursera.org/neuralnets-2012-001/lecture/39
# [3] The Back Propagation Algorithm
#   https://www4.rgu.ac.uk/files/chapter3%20-%20bp.pdf

class NeuralNetwork:
    LEARNING_RATE = 0.5

    def __init__(self, num_inputs, num_hidden, num_outputs, hidden_layer_weights = None, hidden_layer_bias = None, output_layer_weights = None, output_layer_bias = None):
        self.num_inputs = num_inputs

        self.hidden_layer = NeuronLayer(num_hidden, hidden_layer_bias)
        self.output_layer = NeuronLayer(num_outputs, output_layer_bias)

        self.init_weights_from_inputs_to_hidden_layer_neurons(hidden_layer_weights)
        self.init_weights_from_hidden_layer_neurons_to_output_layer_neurons(output_layer_weights)

    def init_weights_from_inputs_to_hidden_layer_neurons(self, hidden_layer_weights):
        weight_num = 0
        for h in range(len(self.hidden_layer.neurons)):
            for i in range(self.num_inputs):
                if not hidden_layer_weights:
                    self.hidden_layer.neurons[h].weights.append(random.random())
                else:
                    self.hidden_layer.neurons[h].weights.append(hidden_layer_weights[weight_num])
                weight_num += 1

    def init_weights_from_hidden_layer_neurons_to_output_layer_neurons(self, output_layer_weights):
        weight_num = 0
        for o in range(len(self.output_layer.neurons)):
            for h in range(len(self.hidden_layer.neurons)):
                if not output_layer_weights:
                    self.output_layer.neurons[o].weights.append(random.random())
                else:
                    self.output_layer.neurons[o].weights.append(output_layer_weights[weight_num])
                weight_num += 1

    def inspect(self):
        print('------')
        print('* Inputs: {}'.format(self.num_inputs))
        print('------')
        print('Hidden Layer')
        self.hidden_layer.inspect()
        print('------')
        print('* Output Layer')
        self.output_layer.inspect()
        print('------')

    def feed_forward(self, inputs):
        hidden_layer_outputs = self.hidden_layer.feed_forward(inputs)
        return self.output_layer.feed_forward(hidden_layer_outputs)

    # Uses online learning, ie updating the weights after each training case
    def train(self, training_inputs, training_outputs):
        self.feed_forward(training_inputs)

        # 1. Output neuron deltas
        pd_errors_wrt_output_neuron_total_net_input = [0] * len(self.output_layer.neurons)
        for o in range(len(self.output_layer.neurons)):

           
            pd_errors_wrt_output_neuron_total_net_input[o] = self.output_layer.neurons[o].calculate_pd_error_wrt_total_net_input(training_outputs[o])

        # 2. Hidden neuron deltas
        pd_errors_wrt_hidden_neuron_total_net_input = [0] * len(self.hidden_layer.neurons)
        for h in range(len(self.hidden_layer.neurons)):

            # We need to calculate the derivative of the error with respect to the output of each hidden layer neuron
            
            d_error_wrt_hidden_neuron_output = 0
            for o in range(len(self.output_layer.neurons)):
                d_error_wrt_hidden_neuron_output += pd_errors_wrt_output_neuron_total_net_input[o] * self.output_layer.neurons[o].weights[h]

           
            pd_errors_wrt_hidden_neuron_total_net_input[h] = d_error_wrt_hidden_neuron_output * self.hidden_layer.neurons[h].calculate_pd_total_net_input_wrt_input()

        # 3. Update output neuron weights
        for o in range(len(self.output_layer.neurons)):
            for w_ho in range(len(self.output_layer.neurons[o].weights)):

                
                pd_error_wrt_weight = pd_errors_wrt_output_neuron_total_net_input[o] * self.output_layer.neurons[o].calculate_pd_total_net_input_wrt_weight(w_ho)

                
                self.output_layer.neurons[o].weights[w_ho] -= self.LEARNING_RATE * pd_error_wrt_weight

        # 4. Update hidden neuron weights
        for h in range(len(self.hidden_layer.neurons)):
            for w_ih in range(len(self.hidden_layer.neurons[h].weights)):

               
                pd_error_wrt_weight = pd_errors_wrt_hidden_neuron_total_net_input[h] * self.hidden_layer.neurons[h].calculate_pd_total_net_input_wrt_weight(w_ih)

               
                self.hidden_layer.neurons[h].weights[w_ih] -= self.LEARNING_RATE * pd_error_wrt_weight

    def calculate_total_error(self, training_sets):
        total_error = 0
        for t in range(len(training_sets)):
            training_inputs, training_outputs = training_sets[t]
            self.feed_forward(training_inputs)
            for o in range(len(training_outputs)):
                total_error += self.output_layer.neurons[o].calculate_error(training_outputs[o])
        return total_error/4.0

class NeuronLayer:
    def __init__(self, num_neurons, bias):

        # Every neuron in a layer shares the same bias
        self.bias = bias if bias else random.random()

        self.neurons = []
        for i in range(num_neurons):
            self.neurons.append(Neuron(self.bias))

    def inspect(self):
        print('Neurons:', len(self.neurons))
        for n in range(len(self.neurons)):
            print(' Neuron', n)
            for w in range(len(self.neurons[n].weights)):
                print('  Weight:', self.neurons[n].weights[w])
            print('  Bias:', self.bias)

    def feed_forward(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.calculate_output(inputs))
        return outputs

    def get_outputs(self):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.output)
        return outputs

class Neuron:
    def __init__(self, bias):
        self.bias = bias
        self.weights = []

    def calculate_output(self, inputs):
        self.inputs = inputs
        self.output = self.squash(self.calculate_total_net_input())
        return self.output

    def calculate_total_net_input(self):
        total = 0
        for i in range(len(self.inputs)):
            total += self.inputs[i] * self.weights[i]
        return total + self.bias

    # Apply the logistic function to squash the output of the neuron
    # The result is sometimes referred to as 'net' [2] or 'net' [1]
    def squash(self, total_net_input):
        return 1 / (1 + math.exp(-total_net_input))

    # Determine how much the neuron's total input has to change to move closer to the expected output
    #
    # Now that we have the partial derivative of the error with respect to the output  and
    # the derivative of the output with respect to the total net input  we can calculate
    # the partial derivative of the error with respect to the total net input.
    # This value is also known as the delta [1]
    
    #
    def calculate_pd_error_wrt_total_net_input(self, target_output):
        return self.calculate_pd_error_wrt_output(target_output) * self.calculate_pd_total_net_input_wrt_input();

    # The error for each neuron is calculated by the Mean Square Error method:
    def calculate_error(self, target_output):
        return (target_output - self.output) ** 2

    # The partial derivate of the error with respect to actual output then is calculated by:
    # = 2 * 0.5 * (target output - actual output) ^ (2 - 1) * -1
    # = -(target output - actual output)
    #
    # The Wikipedia article on backpropagation [1] simplifies to the following, but most other learning material does not [2]
    # = actual output - target output
    #
    # Alternative, you can use (target - output), but then need to add it during backpropagation [3]
    #
    # Note that the actual output of the output neuron is often written as and target output as so:
    
    def calculate_pd_error_wrt_output(self, target_output):
        return -(target_output - self.output)

    # The total net input into the neuron is squashed using logistic function to calculate the neuron's output:
   
    # Note that where represents the output of the neurons in whatever layer we're looking at and  represents the layer below it
    #
    # The derivative (not partial derivative since there is only one variable) of the output then is:
    
    def calculate_pd_total_net_input_wrt_input(self):
        return self.output * (1 - self.output)

    # The total net input is the weighted sum of all the inputs to the neuron and their respective weights:
  
    #
    # The partial derivative of the total net input with respective to a given weight (with everything else held constant) then is:
   
    def calculate_pd_total_net_input_wrt_weight(self, index):
        return self.inputs[index]

###

# Blog post example:

#nn = NeuralNetwork(2, 2, 2, hidden_layer_weights=[0.15, 0.2, 0.25, 0.3], hidden_layer_bias=0.35, output_layer_weights=[0.4, 0.45, 0.5, 0.55], output_layer_bias=0.6)



#for i in range(20):
#    nn.train([0.05, 0.1], [0.01, 0.99])
#    print(i, round(nn.calculate_total_error([[[0.05, 0.1], [0.01, 0.99]]]), 9))

# XOR example:

#training_sets = [[[0, 0], [0]],[[0, 1], [1]],[[1, 0], [1]],[[1, 1], [0]]]
training_sets = [[[5.1,3.5,1.4,0.2], [1, 0, 0]], [[4.9,3.0,1.4,0.2], [1, 0, 0]], [[4.6,3.1,1.5,0.2], [1, 0, 0]], [[5.0,3.6,1.4,0.2], [1, 0, 0]], [[5.4,3.9,1.7,0.4], [1, 0, 0]], [[4.6,3.4,1.4,0.3], [1, 0, 0]], [[5.0,3.4,1.5,0.2], [1, 0, 0]], [[4.4,2.9,1.4,0.2], [1, 0, 0]], [[4.9,3.1,1.5,0.1], [1, 0, 0]], [[4.8,3.4,1.6,0.2], [1, 0, 0]], [[4.8,3.0,1.4,0.1], [1, 0, 0]], [[4.3,3.0,1.1,0.1], [1, 0, 0]], [[5.8,4.0,1.2,0.2], [1, 0, 0]], [[5.7,4.4,1.5,0.4], [1, 0, 0]], [[5.4,3.9,1.3,0.4], [1, 0, 0]], [[5.1,3.5,1.4,0.3], [1, 0, 0]], [[5.7,3.8,1.7,0.3], [1, 0, 0]], [[5.1,3.8,1.5,0.3], [1, 0, 0]], [[5.4,3.4,1.7,0.2], [1, 0, 0]], [[5.1,3.7,1.5,0.4], [1, 0, 0]], [[4.6,3.6,1.0,0.2], [1, 0, 0]], [[5.1,3.3,1.7,0.5], [1, 0, 0]], [[4.8,3.4,1.9,0.2], [1, 0, 0]], [[5.0,3.0,1.6,0.2], [1, 0, 0]], [[5.0,3.4,1.6,0.4], [1, 0, 0]], [[7.0,3.2,4.7,1.4], [0, 1, 0]], [[6.4,3.2,4.5,1.5], [0, 1, 0]], [[5.5,2.3,4.0,1.3], [0, 1, 0]], [[6.5,2.8,4.6,1.5], [0, 1, 0]], [[5.7,2.8,4.5,1.3], [0, 1, 0]], [[6.3,3.3,4.7,1.6], [0, 1, 0]], [[4.9,2.4,3.3,1.0], [0, 1, 0]], [[6.6,2.9,4.6,1.3], [0, 1, 0]], [[5.2,2.7,3.9,1.4], [0, 1, 0]], [[5.0,2.0,3.5,1.0], [0, 1, 0]], [[6.0,2.2,4.0,1.0], [0, 1, 0]], [[6.1,2.9,4.7,1.4], [0, 1, 0]], [[5.6,2.9,3.6,1.3], [0, 1, 0]], [[6.7,3.1,4.4,1.4], [0, 1, 0]], [[5.8,2.7,4.1,1.0], [0, 1, 0]], [[6.2,2.2,4.5,1.5], [0, 1, 0]], [[5.6,2.5,3.9,1.1], [0, 1, 0]], [[5.9,3.2,4.8,1.8], [0, 1, 0]], [[6.3,2.5,4.9,1.5], [0, 1, 0]], [[6.1,2.8,4.7,1.2], [0, 1, 0]], [[6.4,2.9,4.3,1.3], [0, 1, 0]], [[6.6,3.0,4.4,1.4], [0, 1, 0]], [[6.8,2.8,4.8,1.4], [0, 1, 0]], [[6.7,3.0,5.0,1.7], [0, 1, 0]], [[6.0,2.9,4.5,1.5], [0, 1, 0]], [[6.3,3.3,6.0,2.5], [0, 0, 1]], [[5.8,2.7,5.1,1.9], [0, 0, 1]], [[7.1,3.0,5.9,2.1], [0, 0, 1]], [[6.3,2.9,5.6,1.8], [0, 0, 1]], [[7.6,3.0,6.6,2.1], [0, 0, 1]], [[4.9,2.5,4.5,1.7], [0, 0, 1]], [[7.3,2.9,6.3,1.8], [0, 0, 1]], [[6.7,2.5,5.8,1.8], [0, 0, 1]], [[7.2,3.6,6.1,2.5], [0, 0, 1]], [[6.5,3.2,5.1,2.0], [0, 0, 1]], [[6.4,2.7,5.3,1.9], [0, 0, 1]], [[6.8,3.0,5.5,2.1], [0, 0, 1]], [[5.7,2.5,5.0,2.0], [0, 0, 1]], [[5.8,2.8,5.1,2.4], [0, 0, 1]], [[6.4,3.2,5.3,2.3], [0, 0, 1]], [[6.5,3.0,5.5,1.8], [0, 0, 1]], [[7.7,3.8,6.7,2.2], [0, 0, 1]], [[7.7,2.6,6.9,2.3], [0, 0, 1]], [[6.0,2.2,5.0,1.5], [0, 0, 1]],[[6.9,3.2,5.7,2.3], [0, 0, 1]], [[5.6,2.8,4.9,2.0], [0, 0, 1]],[[7.7,2.8,6.7,2.0], [0, 0, 1]], [[6.3,2.7,4.9,1.8], [0, 0, 1]], [[6.7,3.3,5.7,2.1], [0, 0, 1]], [[6.2,2.8,4.8,1.8], [0, 0, 1]], [[5.2,3.5,1.5,0.2], [1, 0, 0]], [[4.7,3.2,1.6,0.2], [1, 0, 0]], [[4.8,3.1,1.6,0.2], [1, 0, 0]], [[5.4,3.4,1.5,0.4], [1, 0, 0]], [[5.5,4.2,1.4,0.2], [1, 0, 0]], [[4.9,3.1,1.5,0.1], [1, 0, 0]], [[5.0,3.2,1.2,0.2], [1, 0, 0]], [[5.5,3.5,1.3,0.2], [1, 0, 0]], [[4.9,3.1,1.5,0.1], [1, 0, 0]], [[4.4,3.0,1.3,0.2], [1, 0, 0]], [[5.1,3.4,1.5,0.2], [1, 0, 0]], [[5.0,3.5,1.3,0.3], [1, 0, 0]], [[4.5,2.3,1.3,0.3], [1, 0, 0]], [[4.4,3.2,1.3,0.2], [1, 0, 0]], [[5.0,3.5,1.6,0.6], [1, 0, 0]], [[5.7,2.6,3.5,1.0], [0, 1, 0]], [[5.5,2.4,3.8,1.1], [0, 1, 0]], [[5.8,2.7,3.9,1.2], [0, 1, 0]], [[6.0,2.7,5.1,1.6], [0, 1, 0]], [[5.4,3.0,4.5,1.5], [0, 1, 0]], [[6.0,3.4,4.5,1.6], [0, 1, 0]], [[6.7,3.1,4.7,1.5], [0, 1, 0]], [[6.3,2.3,4.4,1.3], [0, 1, 0]], [[5.6,3.0,4.1,1.3], [0, 1, 0]], [[5.5,2.5,4.0,1.3], [0, 1, 0]], [[5.5,2.6,4.4,1.2], [0, 1, 0]], [[6.1,3.0,4.6,1.4], [0, 1, 0]], [[5.8,2.6,4.0,1.2], [0, 1, 0]], [[5.0,2.3,3.3,1.0], [0, 1, 0]], [[5.6,2.7,4.2,1.3], [0, 1, 0]], [[6.1,3.0,4.9,1.8], [0, 0, 1]], [[6.4,2.8,5.6,2.1], [0, 0, 1]], [[7.2,3.0,5.8,1.6], [0, 0, 1]], [[7.4,2.8,6.1,1.9], [0, 0, 1]], [[6.4,2.8,5.6,2.2], [0, 0, 1]], [[6.3,2.8,5.1,1.5], [0, 0, 1]], [[6.1,2.6,5.6,1.4], [0, 0, 1]], [[7.7,3.0,6.1,2.3], [0, 0, 1]], [[6.3,3.4,5.6,2.4], [0, 0, 1]], [[6.4,3.1,5.5,1.8], [0, 0, 1]], [[6.0,3.0,4.8,1.8], [0, 0, 1]], [[6.7,3.1,5.6,2.4], [0, 0, 1]], [[6.9,3.1,5.1,2.3], [0, 0, 1]], [[5.8,2.7,5.1,1.9], [0, 0, 1]], [[6.8,3.2,5.9,2.3], [0, 0, 1]]]

nn = NeuralNetwork(len(training_sets[0][0]), 20 , len(training_sets[0][1]))
 
 
nn.inspect()

global noEpochsIris
global meanErrorIris
#global noEpochsIrisVal
#global meanErrorIrisVal

noEpochsIris = open("NumberOfEpochsIris.txt", "w")
meanErrorIris = open("MeanSquaredErrorIris.txt", "w")
#noEpochsIrisVal = open("NumberOfEpochsIrisVal.txt", "w")
#meanErrorIrisVal = open("MeanSquaredErrorIrisVal.txt", "w")

epochs = 0
#valError = []
#trainError = []
 
for i in range(15000):
	training_inputs, training_outputs = random.choice(training_sets)
	nn.train(training_inputs, training_outputs)
	#trainError.append(nn.calculate_total_error(training_sets))
	#print(i, nn.calculate_total_error(training_sets))
	#epochs = epochs + 1
	#valError.append(nn.calculate_total_error(validation_sets))
	noEpochsIris.write(str(i) + "\r\n")
	meanErrorIris.write(str(nn.calculate_total_error(training_sets)) + "\r\n")
	#noEpochsIrisVal.write(str(epochs) + "\r\n")
	#meanErrorIrisVal.write(str(nn.calculate_total_error(validation_sets)) + "\r\n")
	#if epochs > 1 and abs(valError[epochs - 1] - valError[epochs - 2]) > 5:
	#	if abs(valError[epochs-1] - trainError[epochs-1]) > abs(valError[epochs-2] - trainError[epochs-2]):
	#		break

#print ('No of epochs preventing overfitting: ',epochs)



noEpochsIris.close()
meanErrorIris.close()
#noEpochsIrisVal.close()
#meanErrorIrisVal.close()

testing_sets = [[[5.1,3.8,1.9,0.4], [1, 0, 0]], [[4.8,3.0,1.4,0.3], [1, 0, 0]], [[5.1,3.8,1.6,0.2], [1, 0, 0]], [[5.3,3.7,1.5,0.2], [1, 0, 0]], [[5.0,3.3,1.4,0.2], [1, 0, 0]], [[4.7,3.2,1.3,0.2], [1, 0, 0]], [[5.4,3.7,1.5,0.2], [1, 0, 0]], [[5.2,3.4,1.4,0.2], [1, 0, 0]], [[4.6,3.2,1.4,0.2], [1, 0, 0]], [[5.2,4.1,1.5,0.1], [1, 0, 0]], [[5.7,3.0,4.2,1.2], [0, 1, 0]], [[5.7,2.9,4.2,1.3], [0, 1, 0]], [[6.2,2.9,4.3,1.3], [0, 1, 0]], [[5.1,2.5,3.0,1.1], [0, 1, 0]], [[5.7,2.8,4.1,1.3], [0, 1, 0]], [[6.9,3.1,4.9,1.5], [0, 1, 0]], [[5.9,3.0,4.2,1.5], [0, 1, 0]], [[5.6,3.0,4.5,1.5], [0, 1, 0]], [[6.1,2.8,4.0,1.3], [0, 1, 0]], [[5.5,2.4,3.7,1.0], [0, 1, 0]], [[6.7,3.3,5.7,2.5], [0, 0, 1]], [[6.7,3.0,5.2,2.3], [0, 0, 1]], [[6.3,2.5,5.0,1.9], [0, 0, 1]], [[6.2,3.4,5.4,2.3], [0, 0, 1]], [[5.9,3.0,5.1,1.8], [0, 0, 1]], [[6.5,3.0,5.8,2.2], [0, 0, 1]], [[6.9,3.1,5.4,2.1], [0, 0, 1]], [[6.5,3.0,5.2,2.0], [0, 0, 1]], [[7.9,3.8,6.4,2.0], [0, 0, 1]], [[7.2,3.2,6.0,1.8], [0, 0, 1]]]

outputs = []
for j in range(len(testing_sets)):
	outputs.append(nn.feed_forward(testing_sets[j][0]))
	#if outputs[j] >= 0.8:
	#	outputs[j] = 1
	#else:
	#	outputs[j] = 0
	expect = testing_sets[j][1]
	if expect[0] == 1:
		expected = 'Iris setosa'
	elif expect[1] == 1:
		expected = 'Iris Versicolor'
	elif expect[2] == 1:
		expected = 'Iris Virginica'
	else:
		expected = 'null'
		
	print('outputs', outputs[j])
	
	got = outputs[j]
	if round(got[0]) == 1 and round(got[1]) == 0 and round(got[2]) == 0:
		result = 'Iris setosa'
	elif round(got[1]) == 1 and round(got[0]) == 0 and round(got[2]) == 0:
		result = 'Iris Versicolor'
	elif round(got[2]) == 1 and round(got[0]) == 0 and round(got[1]) == 0:
		result = 'Iris Virginica'
	else:
		result = 'null'
	print('Expected = %s, Got = %s' % (expected, result))
nn.inspect()
#print(' expected output',training_sets[0][1])

