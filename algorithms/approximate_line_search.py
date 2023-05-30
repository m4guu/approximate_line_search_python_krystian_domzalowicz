## APPROXIMATE LINE SEARCH ##

from .first_wolfe_condition import first_wolfe_condition
from .second_wolfe_condition import second_wolfe_condition
from .backtracking_line_search import backtracking_line_search


def approximate_line_search(f, gf, x, d, alpha_init=5, beta=1e-4, sigma=0.01, max_iter=20):
    """
       Approximate line search - przybliżone wyszukiwanie linii.

       Parametry:
       - f: funkcja celu
       - gf: gradient funkcij celu
       - x: aktualne położenie
       - d: kierunek poszukiwania
       - alpha_init: pierwsza długość kroku
       - beta: stała w warunku Wolfe (zakres: (0, 1))
       - sigma: stała w warunku Wolfe
       - max_iter: maxymalna liczba interacji algorytmu

       Zwraca:
       - alpha: optymalną długość kroku
       """

    alpha = alpha_init
    iter_count = 0
    while iter_count < max_iter:
        if not first_wolfe_condition(f, gf, x, d, alpha, beta):
            # warunek wystarczającego spadku nie jest spełniony
            return backtracking_line_search(f, gf, x, d, alpha, beta)

        if not second_wolfe_condition(gf, x, d, alpha, sigma):
            # warunek krzywizny nie jest spełniony
            return backtracking_line_search(f, gf, x, d, alpha, beta)

        iter_count += 1
        alpha += 1.0  # Powiększ długość kroku dla kolejnej iteracji

    return alpha
