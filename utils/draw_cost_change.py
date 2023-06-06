import matplotlib.pyplot as plt
import numpy as np

def draw_cost_change(f, x0, points):
    iterations = len(points)
    costs = [f(x) for x in points]

    plt.figure(figsize=(10, 6))
    plt.plot(range(iterations), costs, '-o')
    plt.xlabel('Iteracja')
    plt.ylabel('Wartość funkcji celu')
    plt.title('Zmiana wartości funkcji celu wraz z iteracją')
    plt.xticks(range(iterations))
    plt.grid(True)
    plt.show()