##- THREE HUMP CAMEL FUNCTION -##
##- MINIMUM = (x1 = 0 ; x2 = 0) -##

def three_hump_camel_function(x):
    return 2 * x[0]**2 - 1.05*x[0]**4 + (x[0]**6)/6 + x[0]*x[1] + x[1]**2
