import numpy as np
import matplotlib.pyplot as plt
from operator import add
from math import sin
from math import cos


def input_data(filename):
    with open(filename, "r") as in_file:
        in_lines = in_file.readlines()
    return in_lines


def parse_data(in_line):
    list_no_return = in_line.strip("\n")
    list_split = list_no_return.split(",")
    list_int = [float(x) for x in list_split]
    return list_int


def plot_together(data_0, data_1, sincos):
    time = np.arange(0, len(data_0), 1)
    plt.plot(data_0, data_1)
    plt.plot(data_0, sincos)
    plt.legend(["Data OG", "Curve Matched"])
    plt.show()


def sin_cos(data_0):
    curvesin = [1 * sin(2 * t) for t in data_0]
    curvecos = [2 * cos(3 * p) for p in data_0]
    sincos = list(map(add, curvesin, curvecos))
    return sincos


if __name__ == "__main__":
    in_data = input_data("curve_to_match.dat")
    data_0 = parse_data(in_data[0])
    data_1 = parse_data(in_data[1])
    curve = sin_cos(data_0)
    plot_together(data_0, data_1, curve)
