## FIRST WOLFE CONDITION ##
import numpy as np


def first_wolfe_condition(f, gf, x, d, alpha, beta):
    """
    Pierwszy warunek Wolfe - warunek wystarczającego spadku.

    Parametry:
    - f: funkcja celu
    - gf: gradient funkcij celu
    - x: aktualne położenie
    - d: kierunek poszukiwania
    - alpha: długość kroku
    - beta: stała w warunku Wolfe (zakres: (0, 1))

    Zwraca:
    - True, jeśli warunek jest spełniony
    - False, w przeciwnym przypadku
    """
    f_current = f(x)           # Wartość funkcji w aktualnym położeniu
    f_next = f(x + alpha * d)  # Wartość funkcji w nowym położeniu

    # Warunek wystarczającego spadku
    return f_next <= f_current + beta * alpha * np.dot(gf(x), d)
