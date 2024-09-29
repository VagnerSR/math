def weighted_mean(data, weights):
    if len(data) != len(weights):
        raise ValueError("The two arrays must have the same length.")
    
    n = len(data)
    
    weighted_sum = sum(data[i] * weights[i] for i in range(n))
    
    return weighted_sum / sum(weights)