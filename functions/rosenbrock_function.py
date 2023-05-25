##- FUNKCJA ROSENBROCKA -##
##- MINIMUM = (x1 = 1 ; x2 = 2) -##

def rosenbrock_function(x1, x2):
    return (1 - x1) ** 2 + 100 * (x2 - x1 ** 2) ** 2
