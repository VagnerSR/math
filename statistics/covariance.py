def covariance(x, y):
    if len(x) != len(y):
        raise ValueError("The two arrays must have the same length.")
    
    n = len(x)
    
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)
    
    return cov