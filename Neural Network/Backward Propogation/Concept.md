Backward propogation is an extension of gradient descent
#Calculate error term for hidden layer
hidden_error_term = np.dot(output_error_term, weights_hidden_output) * \
                    hidden_layer_output * (1 - hidden_layer_output)

#Calculate change in weights for hidden layer to output layer
delta_w_h_o = learnrate * output_error_term * hidden_layer_output

#Calculate change in weights for input layer to hidden layer
delta_w_i_h = learnrate * hidden_error_term * x[:, None]

concept :
    It is a supervised learning algorithm, for training multi-layer perceptrons.
    The calculated error is propogated back as an input, if its not minimized.
    
How Backward propogation is done
> We first initialized some random value to ‘W’ and propagated forward.
> Then, we noticed that there is some error. To reduce that error, we propagated backwards and increased the value of ‘W’.
> After that, also we noticed that the error has increased. We came to know that, we can’t increase the ‘W’ value.  
> So, we again propagated backwards and we decreased ‘W’ value.
> Now, we noticed that the error has reduced.
