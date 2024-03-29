import numpy as np

def calculate_hypothesis(X, theta, i):
    """
        :param X            : 2D array of our dataset
        :param theta        : 1D array of the trainable parameters
        :param i            : scalar, index of current training sample's row
    """
    #########################################
    # Write your code here
    # You must calculate the hypothesis for the i-th sample of X, given X, theta and i.
    x = X[i]
    hypothesis = theta[0]*x[0] + theta[1]*x[1] + theta[2]*pow(x[1], 2) + theta[3]*pow(x[1], 3) + theta[4]*pow(x[1], 4) + theta[5]*pow(x[1], 5)
    ########################################/

    return hypothesis
