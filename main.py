####################--- METODY OPTYMALIZACJI ---####################
# ------------------------------------------------------------------#
##################--- APPROXIMATE LINE SEARCH ---###################

import numpy as np
from functions import booth_function, booth_gradient, booth_with_penalty, booth_with_penalty_gradient, penalty_function,constraint , rosenbrock_function, rosenbrock_gradient, rosenbrock_gradient_with_penalty, rosenbrock_function_with_penalty, \
    three_hump_camel_function, three_hump_camel_gradient, camel_with_penalty, camel_with_penalty_gradient
from algorithms import approximate_line_search
from utils import draw_graph, draw_cost_change


def f_min_search(f, gf, x0, tolerance=1e-3, max_iterations=100000):
    x = x0
    iteration = 0
    points = [x]  # Lista przechowująca punkty po każdej iteracji
    d = -gf(x)  # Początkowy kierunek

    while iteration < max_iterations:
        if np.linalg.norm(gf(x)) < tolerance:
            break

        alpha = approximate_line_search(f, gf, x, d)

        x = x + alpha * d
        points.append(x)  # Dodawanie aktualnego punktu do listy punktów

        # Aktualizacja kierunku przy użyciu metody gradientu sprzężonego
        beta = np.dot(gf(x), gf(x)) / np.dot(gf(points[-2]), gf(points[-2]))
        d = -gf(x) + beta * d

        iteration += 1
    return points, iteration


# testy
x0_rosenbrock = np.array([-5, 5])
x0_booth = np.array([-10, 10])
x0_camel = np.array([-5, 10])
#
# points_rosenbrock, iteration_rosenbrock = f_min_search(rosenbrock_function, rosenbrock_gradient, x0_rosenbrock)
# points_booth, iteration_booth = f_min_search(booth_function, booth_gradient, x0_booth)
points_camel, iteration_camel = f_min_search(three_hump_camel_function, three_hump_camel_gradient, x0_camel)

# graficzne przedstawie wartości zmiennych decyzyjnych w trakcie działania algorytmu
# draw_graph(rosenbrock_function, x0_rosenbrock, points_rosenbrock, [-6, 6], [-7, 13])
# draw_graph(booth_function, x0_booth, points_booth, [-12, 6], [-6, 12])
draw_graph(three_hump_camel_function, x0_camel, points_camel, [-6, 6], [-6, 14])
# graficzne przedstawienie zmiany wartości funkcji celu wraz z iteracją algorytmu
# draw_cost_change(rosenbrock_function,  points_rosenbrock)
# draw_cost_change(booth_function,  points_booth)
draw_cost_change(three_hump_camel_function,  points_camel)

# Wypisanie wyników
# print("Funkcja Rosenbrock:")
# print("- Liczba iteracji:", iteration_rosenbrock)
# print("- Znalezione minimum:", points_rosenbrock[-1])
# print("- Wartośc funkcji celu:", rosenbrock_function(points_rosenbrock[-1]))

#
# print("Funkcja Bootha:")
# print("- Liczba iteracji:", iteration_booth)
# print("- Znalezione minimum:", points_booth[-1])
#
# print("Funkcja Camela:")
# print("- Liczba iteracji:", iteration_camel)
# print("- Znalezione minimum:", points_camel[-1])


# testowanie funkcji z ograniczeniami

# points_with_penalty, iteration_with_penalty = f_min_search(booth_with_penalty, booth_with_penalty_gradient, x0_booth)

# points_with_penalty, iteration_with_penalty = f_min_search(camel_with_penalty, camel_with_penalty_gradient, x0_camel)
# draw_graph_with_penalty(three_hump_camel_function, constraint, x0_camel, points_with_penalty, [-6, 6], [-20, 20])

