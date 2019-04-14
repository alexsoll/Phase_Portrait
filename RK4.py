from matplotlib import pyplot as plt
import random
from mpmath import *


def cauchy(dx, dy, x10, x20, Range, num_part):
    X = [x10]
    Y = [x20]

    h = Range / num_part

    num_system = '14'

    for i in range(0, int(num_part)):
        k11 = dx((i - 1) * h, X[-1], Y[-1], num_system)
        k12 = dy((i - 1) * h, X[-1], Y[-1], num_system)
        k21 = dx((i - 1) * h + h / 2, X[-1] + h / 2 * k11, Y[-1] + h / 2 * k12, num_system)
        k22 = dy((i - 1) * h + h / 2, X[-1] + h / 2 * k11, Y[-1] + h / 2 * k12, num_system)
        k31 = dx((i - 1) * h + h / 2, X[-1] + h / 2 * k21, Y[-1] + h / 2 * k22, num_system)
        k32 = dy((i - 1) * h + h / 2, X[-1] + h / 2 * k21, Y[-1] + h / 2 * k22, num_system)
        k41 = dx((i - 1) * h + h, X[-1] + h * k31, Y[-1] + h * k32, num_system)
        k42 = dy((i - 1) * h + h, X[-1] + h * k31, Y[-1] + h * k32, num_system)

        X.append(X[-1] + h / 6 * (k11 + 2 * k21 + 2 * k31 + k41))
        Y.append(Y[-1] + h / 6 * (k12 + 2 * k22 + 2 * k32 + k42))

    return X, Y


def dx(t, x1, x2, f):
    d = {'1': x1 + x2,
         '2': -x1 - 5 * x2,
         '3': 3 * x1 - x2,
         '4': x1 - x2,
         '5': -x1 + 8 * x2,
         '6': x1 + 3 * x2,
         '7': (0.1 - 0.05 * x2) * x1,
         '8': x2,
         '9': x2,
         '10': x1 - x1 * x2,
         '11': x1 * 4 - x1 * x1 - x1 * x2,
         '12': x2,
         '13': x2,
         '14': -x1 * (1 + x1 * x1) - 2 * x2,
         '15': x2,
         '16': x1 - x1 * x2 / (1 + 0.9 * x1),
         '17': x1 - x1 * x1 - 5 * x1 * x2
         }
    return d[f]


def dy(t, x1, x2, f):
    d = {'1': -2 * x1 + 3 * x2,
         '2': x1 + x2,
         '3': 4 * x1 - x2,
         '4': x2 - 4 * x1,
         '5': x1 + x2,
         '6': 2 * x1,
         '7': (-0.2 + 0.09 * x1) * x2,
         '8': (- 9.8 / 0.1) * sin(x1),
         '9': (- 9.8 / 0.1) * sin(x1) - sqrt((2 * 9.8) / 0.1),
         '10': -x2 + x1 * x1,
         '11': x2 * x1 - (x2 + x2),
         '12': -2 * x2 + x1 + 3 * (x1 * x1 * x1),
         '13': -2 * x2 - 3 * x1,
         '14': x1 + x2,
         '15': -x1 - x2 * x2 * x2,
         '16': -x2 + x1 * x2 / (1 + 0.9 * x1),
         '17': 3 * x2 - x2 * x2 - 3 * x1 * x2
         }
    return d[f]


def showPhase():
    num_partitions = 1000
    v = []
    _range = 15
    plt.xlabel('X')
    plt.ylabel('Y')

    for i in range(50):
        v.append([random.randint(-10, 10), random.randint(-10, 10)])
        plt.annotate("(" + str(v[-1][0]) + "," + str(v[-1][1]) + ")", xy=(v[-1][0], v[-1][1]), fontsize=5)
        v[i][0], v[i][1] = cauchy(dx, dy, v[i][0], v[i][1], _range, num_partitions)
        plt.plot(v[i][0], v[i][1], color="blue", lw="1")

    plt.xlim(-40, 40)
    plt.ylim(-40, 40)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.show()


def main():
    showPhase()


main()
