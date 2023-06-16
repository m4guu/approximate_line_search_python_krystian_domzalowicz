##- FUNKCJA ROSENBROCKA -##
##- MINIMUM = (x1 = 1 ; x2 = 1) -##
import numpy as np


def rosenbrock_function(x):
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2


def rosenbrock_gradient(x):
    return np.array([2 * (200 * x[0] ** 3 - 200 * x[0] * x[1] + x[0] - 1), 200 * (x[1] - x[0] ** 2)], dtype=np.float64)


def penalty_function(x):
    return (2 * x[0] + 3 * x[1] - 6)**2


def rosenbrock_function_with_penalty(x):
    r = 1
    return rosenbrock_function(x) + r * penalty_function(x)


def rosenbrock_gradient_with_penalty(x):
    return np.array([2*(-13+200*x[0]**3+x[0]*(5-200*x[1])+6*x[1]), -36+12*x[0]-200*x[0]**2+218*x[1]], dtype=np.float64)