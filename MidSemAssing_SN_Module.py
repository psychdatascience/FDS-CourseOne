def mean(data):
    return sum(data) / len(data)

def variance(data):
    m = mean(data)
    return sum((xi - m) ** 2 for xi in data) / len(data)

def std_dev(data):
    return variance(data) ** 0.5

def std_error(data):
    return std_dev(data) / (len(data) ** 0.5)

def z_score(observation, data):
    return (observation - mean(data)) / std_dev(data)
