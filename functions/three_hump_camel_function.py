##- THREE HUMP CAMEL FUNCTION -##
##- MINIMUM = (x1 = 0 ; x2 = 0) -##
import numpy as np


def three_hump_camel_function(x):
    return 2 * x[0]**2 - 1.05*x[0]**4 + (x[0]**6)/6 + x[0]*x[1] + x[1]**2


def three_hump_camel_gradient(x):
    return np.array([4*x[0] - 4.2*x[0]**3 +x[0]**5+x[1], x[0]+2*x[1]])


def penalty_function(x):
    constraint_value = 2*x[0] + 3*x[1] - 2
    if np.any(constraint_value >= 0):
        return 0
    else:
        return constraint_value


def camel_with_penalty(x, r=100):
    return three_hump_camel_function(x) + r * penalty_function(x)


def camel_with_penalty_gradient(x, r=100):
    return three_hump_camel_gradient(x) + r * np.array([2, 3], dtype=np.float64)
