from covariance import covariance
from standard_deviation import standard_deviation

def correlation_coefficient(x, y):
    if len(x) != len(y):
        raise ValueError("The two arrays must have the same length.")
    
    n = len(x)

    cov = covariance(x, y)
    std_x = standard_deviation(x)
    std_y = standard_deviation(y)
    
    corr = cov / (std_x * std_y)
    
    return corr

    