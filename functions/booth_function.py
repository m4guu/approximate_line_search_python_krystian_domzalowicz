##- FUNKCJA BOOTHA -##
##- MINIMUM = (x1 = 1 ; x2 = 3) -##
import numpy as np


def booth_function(x):
    return (x[0] + 2*x[1] - 7) ** 2 + (2*x[0] + x[1]-5) ** 2


def booth_gradient(x):
    return np.array([-34 + 10*x[0]+8*x[1], -38 + 8*x[0]+10*x[1]], dtype=np.float64)


# UWAGA! zmieniam w zależności od badanej funkcji celu z ograniczeniami
def constraint(x):
    return (2 - 2*x) / 3


def penalty_function(x):
    return 2*x[0]+3*x[1]-6


def booth_with_penalty(x, r=10):
    return booth_function(x) + r * penalty_function(x)


def booth_with_penalty_gradient(x, r=10):
    dx = 4*r*(2*x[0]+3*x[1]-6) + 4*(2*x[0]+x[1]-5) + 2*(x[0] + 2*x[1] - 7)
    dy = 6*r*(3*x[1]+2*x[0]-6) + 4*(2*x[1]+x[0]-7) + 2*(x[1]+2*x[0]-5)
    return np.array([dx, dy])
