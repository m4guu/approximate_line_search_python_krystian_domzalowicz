##- FUNKCJA ROSENBROCKA -##
##- MINIMUM = (x1 = 1 ; x2 = 1) -##
import numpy as np


def rosenbrock_function(x):
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2


def rosenbrock_gradient(x):
    return np.array([2 * (200*x[0]**3 - 200 * x[0] * x[1] + x[0] - 1), 200 * (x[1] - x[0] ** 2)], dtype=np.float64)
