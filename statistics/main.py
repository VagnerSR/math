from tendencies import tendencies



x = [1, 2, 3, 4,5]
y = [0.136, 0.159, 0.248, 0.202, 0.255]

result = tendencies(x, sample=True)
for key, value in result.items():
    print(f"{key}: {value}")