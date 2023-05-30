## BACKTRACKING LINE SEARCH ##

from .first_wolfe_condition import first_wolfe_condition


def backtracking_line_search(f, gf, x, d, alpha, beta):
    """
       Wyszukiwanie liniowe z cofaniem

       Parametry:
       - f: funkcja celu
       - gf: gradient funkcij celu
       - x: aktualne położenie
       - d: kierunek poszukiwania
       - alpha: długość kroku
       - beta: stała w warunku Wolfe (zakres: (0, 1))

       Zwraca:
        - alpha: długość kroku
       """
    while not first_wolfe_condition(f, gf, x, d, alpha, beta):
        alpha = alpha * 0.5
    return alpha
