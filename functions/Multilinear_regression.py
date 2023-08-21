#%%
import numpy as np
import pandas as pd

def multilinear_regression(x, y, initial, alpha, iters) -> np.array:
    """This function train a multiple dimension linear model using gradient descent as its optimizer. 

    Args:
        x (np.array[np.array[float]]): The independent variables. Each row of variables must be an
        element of the array
        y (np.array[float]): An array with the dependant variable. 

    Returns:
        np.array: The weights of the best fit. 
    """
    #For code simplicity, we'll add a 1-column for the constant factor
    x = np.array([np.insert(i, 0, 1) for i in x])

    #get the dimension
    dim = len(x[0])
    
    n = len(x)

    #define the hipothesis function
    h = lambda x, t: np.dot(x, t)

    t = initial
    for _ in range(iters):
        #computing dT
        t_delta = [1] * dim
        for i in range(dim):
            t_delta[i] = (1/n) * sum([(h(x[j], t) - y[j]) * x[j][i] for j in range(n)])
        
        t_delta = np.array(t_delta)
        #updating T
        t = (t - alpha*t_delta)
    
    return t

def predict_regresion(t, x):
    x = np.array([np.insert(i, 0, 1) for i in x])
    return np.dot(x, t)

