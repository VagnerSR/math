from covariance import covariance
from standard_deviation import standard_deviation
from correlation_coefficient import correlation_coefficient
from weighted_mean import weighted_mean
from grouped_data import grouped_mean, grouped_standard_deviation


x = [3.55, 4.01, 3.05, 5.35, 4.22, 6.12, 7.45, 5.95, 6.35, 6.98]
y = [51, 54, 50, 60, 52, 61, 63, 59, 68, 74]

#print(covariance(x, y))
#print(standard_deviation(x))
print(correlation_coefficient(x, y))
#print(weighted_mean(x, y))
#print(grouped_mean(x, y), grouped_standard_deviation(x, y))

#print(sum(x) / len(x), len(x))