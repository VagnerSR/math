import math


def grouped_mean(data, freq):
    if len(data) != len(freq):
        raise ValueError("The two arrays must have the same length.")
    
    n = len(data)
    
    weighted_sum = sum(data[i] * freq[i] for i in range(n))
    
    return weighted_sum / sum(freq)

def grouped_standard_deviation(data, freq):
    if len(data) != len(freq):
        raise ValueError("The two arrays must have the same length.")
    
    N = sum(freq)
    mean = sum(midpoint * freq for midpoint, freq in zip(data, freq)) / N
    
    variance = sum(freq * (midpoint - mean) ** 2 for midpoint, freq in zip(data, freq)) / N
    
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation