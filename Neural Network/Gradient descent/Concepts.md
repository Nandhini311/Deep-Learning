Set the weight step to zero: \Delta w_i = 0Δw 
i
​	
 =0
For each record in the training data:
Make a forward pass through the network, calculating the output \hat y = f(\sum_i w_i x_i) 
y
^
​	
 =f(∑ 
i
​	
 w 
i
​	
 x 
i
​	
 )
Calculate the error term for the output unit, \delta = (y - \hat y) * f&#x27;(\sum_i w_i x_i)δ=(y− 
y
^
​	
 )∗f 
′
 (∑ 
i
​	
 w 
i
​	
 x 
i
​	
 )
Update the weight step \Delta w_i = \Delta w_i + \delta x_iΔw 
i
​	
 =Δw 
i
​	
 +δx 
i
​	
 
Update the weights w_i = w_i + \eta \Delta w_i / mw 
i
​	
 =w 
i
​	
 +ηΔw 
i
​	
 /m where \etaη is the learning rate and mm is the number of records. Here we're averaging the weight steps to help reduce any large variations in the training data.
Repeat for ee epochs.
