import numpy as np

def softmax(x):
    expX = np.exp(x)   #exp applied to every element of the vector
    sumX = np.sum(expX) #denominator
    result = []
    
    for i in expX:
        result.append(i/sumX)
        
    return result


#drive code
X = [2,1,0]
ans = softmax(X)
print(ans)


'''Works on a vector. Takes a vector of k real values and returns a vector of k values to sum = 1 (probabilities)'''
