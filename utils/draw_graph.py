import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator


def draw_graph(f, x0, points, xlim, ylim):
    # Tworzenie siatki punktów do wygenerowania konturów
    x = np.linspace(xlim[0], xlim[1], 100)
    y = np.linspace(ylim[0], ylim[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = f([X, Y])

    # Wykres konturów funkcji
    plt.contour(X, Y, Z, levels=50)

    # wykres punktu startowego
    plt.plot(x0[0], x0[1], 'ro', label='Start Point')
    plt.text(x0[0], x0[1], 'Start', ha='right')

    # Wykres iteracji i połączenie punktów
    for i in range(len(points) - 1):
        plt.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]], '.-', color='r', markersize=3)

    # Wykres znalezionego minimum
    result = points[-1]
    plt.plot(result[0], result[1], 'go', label='Minimum')
    plt.text(result[0], result[1], 'Minimum', ha='left')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Funkcja i znaleziony minimum')
    plt.show()