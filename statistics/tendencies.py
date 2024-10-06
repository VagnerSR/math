from variance_and_std import variance, standard_deviation
from collections import Counter

def tendencies(data, sample=True):
    if len(data) == 0:
        return None
    
    n = len(data)
    
    # Mean (Average)
    mean = sum(data) / n

    # Variance and Standard Deviation (handles both sample and population)
    v = variance(data, sample)
    std = standard_deviation(data, sample)
    
    # Median
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    # Mode
    counts = Counter(sorted_data)
    max_freq = max(counts.values())
    
    if max_freq == 1:
        mode = "No mode" 
    else:
        mode = [val for val, freq in counts.items() if freq == max_freq]
        if len(mode) == 1:
            mode = mode[0]

    # Range
    data_range = max(data) - min(data)
    
    # Interquartile Range (IQR) and Outliers
    q1 = sorted_data[n // 4]
    q3 = sorted_data[3 * n // 4]
    iqr = q3 - q1
    
    # Outlier detection: Values outside the range [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'range': data_range,
        'IQR': iqr,
        'outliers': outliers,
        'variance': v,
        'standard_deviation': std
    }