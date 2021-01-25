Here's the general algorithm for updating the weights with gradient descent:

1.Set the weight step to zero
2.For each record in the training data:
  Make a forward pass through the network, calculating the output 
3. Calculate the error term for the output unit = y-output
4. Update the weight step 
     error_term = error * output * 1-output
5. Update the weights .
   #for each sample 
   del_weights += error_term * x
   #update the weights
   wieghts += learning rate* del_weights / n_records
   Here we're averaging the weight steps to help reduce any large variations in the training data.
6.Repeat for ee epochs.


weights are changed for every sample, if correctly classified lines moves father away, if 
incorrectly classified, comes closer
