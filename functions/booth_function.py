##- FUNKCJA BOOTHA -##
##- MINIMUM = (x1 = 1 ; x2 = 3) -##

def booth_function(x):
    return (x[0] + 2*x[1] - 7) ** 2 + (2*x[0] + x[1]-5) ** 2
