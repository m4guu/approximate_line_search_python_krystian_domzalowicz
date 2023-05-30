##- FUNKCJA BOOTHA -##
##- MINIMUM = (x1 = 1 ; x2 = 3) -##
import numpy as np

def booth_function(x):
    return (x[0] + 2*x[1] - 7) ** 2 + (2*x[0] + x[1]-5) ** 2


def booth_gradient(x):
    return np.array([-34 + 10*x[0]+8*x[1], -38 + 8*x[0]+10*x[1]], dtype=np.float64)
