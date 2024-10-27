import math

def bernoulli_distribution(n, p):
    if not 0 <= p <= 1:
        raise ValueError("Probability p must be between 0 and 1.")
    if n < 0:
        raise ValueError("Number of trials n must be non-negative.")

    expected_value = n * p

    variance = n * p * (1 - p)

    standard_deviation = math.sqrt(variance)
    
    return f"Expected Value: {expected_value}, Variance: {variance}, Standard Deviation: {standard_deviation}"

