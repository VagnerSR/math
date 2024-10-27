import math

def binomial_probability(n, k, p):
    nCk = math.comb(n, k)

    probability = nCk * (p ** k) * ((1 - p) ** (n - k))

    return probability

def binomial_at_least(n, k, p):
    probability_sum = sum(binomial_probability(n, i, p) for i in range(k, n + 1))

    return probability_sum

def binomial_at_most(n, k, p):
    probability_sum = sum(binomial_probability(n, i, p) for i in range(k + 1))

    return probability_sum

def binomial_more_than(n, k, p):
    probability_sum = sum(binomial_probability(n, i, p) for i in range(k + 1, n + 1))

    return probability_sum

def binomial_fewer_than(n, k, p):
    probability_sum = sum(binomial_probability(n, i, p) for i in range(k))
    
    return probability_sum
