import numpy as np

#Y - array that says 0/1, 1- for yes and 0 - for no
#P - array that contains the probability of an event happening.
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y*np.log(P) + (1-Y)*np.log(1-P))
