import math

def variance(data, sample=True):
    
    if len(data) == 0:
        return None

    n = len(data)
    mean_data = sum(data) / n

    if sample:
        v = sum((x - mean_data) ** 2 for x in data) / (n - 1)
    else:
        v = sum((x - mean_data) ** 2 for x in data) / n

    return v

def standard_deviation(data, sample=True):
    
    if len(data) == 0:
        return None

    std = math.sqrt(variance(data, sample))
    return std