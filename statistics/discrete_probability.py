def expected_value(values, probabilities):
    if len(values) != len(probabilities):
        raise ValueError("The number of values and probabilities must be the same.")
    
    if not abs(sum(probabilities) - 1.0) < 1e-6:
        raise ValueError("The probabilities must sum to 1.")
    
    expected_val = sum(x * p for x, p in zip(values, probabilities))
    
    return expected_val

def variance(values, probabilities):
    if len(values) != len(probabilities):
        raise ValueError("The number of values and probabilities must be the same.")
    
    if not abs(sum(probabilities) - 1.0) < 1e-6:
        raise ValueError("The probabilities must sum to 1.")
    
    mu_x = expected_value(values, probabilities)

    variance_x = sum((x - mu_x) ** 2 * p for x, p in zip(values, probabilities))
    
    return variance_x