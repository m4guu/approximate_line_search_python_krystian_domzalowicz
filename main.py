####################--- METODY OPTYMALIZACJI ---####################
# ------------------------------------------------------------------#
##################--- APPROXIMATE LINE SEARCH ---###################

import numpy as np
import matplotlib.pyplot as plt
from autograd import grad

from functions import booth_function, rosenbrock_function, three_hump_camel_function
from algorithms import approximate_line_search

print("approximate line search")
