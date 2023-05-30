## SECOND WOLFE CONDITION ##
import numpy as np


def second_wolfe_condition(gf, x, d, alpha, sigma):
    """
    Drugi warunek Wolfe - warunek krzywizny.

    Parametry:
    - gf: gradient funkcij celu
    - x: aktualne położenie
    - d: kierunek poszukiwania
    - alpha: długość kroku
    - sigma: stała w warunku Wolfe

    Zwraca:
    - True, jeśli warunek jest spełniony
    - False, w przeciwnym przypadku
    """
    grad_current = gf(x)           # Gradient funkcji w aktualnym położeniu
    grad_next = gf(x + alpha * d)  # Gradient funkcji w nowym położeniu

    # Warunek krzywizny
    return np.dot(grad_next, d) >= sigma * np.dot(grad_current, d)
