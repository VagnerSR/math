import math


def standard_deviation(data):
    if len(data) == 0:
        return None

    n = len(data)

    mean_data = sum(data) / n

    std = math.sqrt(sum((x - mean_data) ** 2 for x in data) / (n - 1))

    return std