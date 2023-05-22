import random

def random_with_probability(values, probabilities):
    rand = random.random()
    prob_sum = 0
    
    for i, prob in enumerate(probabilities):
        prob_sum += prob
        if rand < prob_sum:
            return values[i]
    
    return None

values = [1, 2, 3, 4, 5]
probabilities = [0.1, 0.3, 0.2, 0.25, 0.15]

result = random_with_probability(values, probabilities)

print("Случайное число с заданной вероятностью:", result)
