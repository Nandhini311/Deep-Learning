import numpy as np

class Perception:
    
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        #init weights
        self.weights = np.zeros(n_features)
        self.bias = 0
    
        y_ = np.array([1 if i > 0 else 0 for i in y])
        
        for _ in range(self.iters):                                          //to find the best fit line 
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights)
                y_predicted = activation_func(linear_output)
                
                update = self.lr*(y_[idx] - y_predicted)
                self.weights += update*x_i
                self.bias += update
                
                
    def predict(self, X):                                                    //to predict the 'y'
        linear_output = np.dot(X,self.weights)+self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted
    
    def __unit_step_func(self, X):
        return np.where(x>=0,1,0)
