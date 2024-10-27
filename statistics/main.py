from tendencies import tendencies
from discrete_probability import expected_value, variance
import math
from poisson_distribution import poisson_probability, poisson_at_least, poisson_at_most, poisson_more_than, poisson_fewer_than
from binomial_probability import binomial_probability, binomial_at_least, binomial_at_most, binomial_more_than, binomial_fewer_than
from bernoulli_distribution import bernoulli_distribution


x = [0, 2, 5, 10]
y = [2/8,3/8, 2/8, 1/8]

#result = expected_value(x, y)

print(bernoulli_distribution(5, 6/8))

#for key, value in result.items():
#    print(f"{key}: {value}")