import numpy as np
import numpy.linalg
import pandas as pd
from scipy.optimize import least_squares, OptimizeResult
from easy_trilateration.model import *
from numpy import linalg as LA


def solve_history_linear(history: [Trilateration]):
    for item in history:
        solve_linear(item)


def solve_history(history: [Trilateration]):
    guess = Circle(0, 0, 0)
    cond = []
    for item in history:
        guess = solve(item, guess)
        cond.append(item.meta)
    print("Max:" + str(max(cond)))
    print("Min:" + str(min(cond)))


def solve_linear(trilateration: Trilateration) -> Circle:
    result = linear_least_squares(trilateration.sniffers)
    trilateration.result = result
    trilateration.meta = 1
    return result


cond_max = 0


def solve(trilateration: Trilateration, guess: Circle = Circle(0, 0, 0)) -> Circle:
    result, meta = easy_least_squares(trilateration.sniffers, guess)
    j = meta.jac
    jt = meta.jac.transpose()
    cov_matrix = pd.DataFrame((jt.dot(j)) ** -1)
    trilateration.result = result
    eig = LA.eig(cov_matrix)[0]
    meta = abs(max(eig) / min(eig))

    trilateration.meta = meta
    # at least one zero is present or if number exceeds threshold
    # if len(eig[eig != 0]) < 3 or meta > 2:
    #    trilateration.meta = 3
    return result


def rssi_to_distance(rssi, C=35.5510920, N=29.0735592, B=11.8099735):
    return B ** (-1*(rssi + C) / N)


def linear_least_squares(crls: [Circle]) -> Circle:
    x, y = 0, 0
    a = []
    b = []
    for circle in crls:
        a.append([1, -2 * circle.center.x, -2 * circle.center.y])
        b.append([circle.radius ** 2 - circle.center.x ** 2 - circle.center.y ** 2])

    A = np.array(a)

    x = np.array([x ** 2 + y ** 2, x, y])

    np.dot(A, x)

    B = np.array(b)

    x, residuals, rank, s = np.linalg.lstsq(A, B)

    return Circle(x[1], x[2], 0)


def easy_least_squares(crls, guess=Circle(0, 0, 0)) -> tuple[Circle, OptimizeResult]:
    g = (guess.center.x, guess.center.y, guess.radius)
    result = least_squares(equations, g, args=[crls])

    xf, yf, rf = result.x

    return Circle(xf, yf, rf), result


def equations(guess, crls: [Circle]):
    eqs = []
    x, y, r = guess
    for circle in crls:
        eqs.append(((x - circle.center.x) ** 2 + (y - circle.center.y) ** 2 - (circle.radius - r) ** 2))
    return eqs
