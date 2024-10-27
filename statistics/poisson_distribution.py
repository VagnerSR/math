import math

def poisson_probability(x, lam):  
    if x < 0:
        return 0  
    
    probability = (lam ** x) * math.exp(-lam) / math.factorial(x)

    return probability

def poisson_at_least(x, lam, max_iterations=100):
    probability_sum = 0

    for i in range(x, max_iterations):
        probability_sum += poisson_probability(i, lam)

    return probability_sum

def poisson_at_most(x, lam):
    probability_sum = sum(poisson_probability(i, lam) for i in range(x + 1))

    return probability_sum


def poisson_more_than(x, lam, max_iterations=100):
    probability_sum = 0

    for i in range(x + 1, max_iterations):
        probability_sum += poisson_probability(i, lam)

    return probability_sum

def poisson_fewer_than(x, lam):
    probability_sum = sum(poisson_probability(i, lam) for i in range(x))

    return probability_sum