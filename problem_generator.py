import numpy as np

def generate_addition_problems(num_problems, lower_bound=1, upper_bound=10):
    problems = []
    for _ in range(num_problems):
        a = np.random.randint(lower_bound, upper_bound + 1)
        b = np.random.randint(lower_bound, upper_bound + 1)
        question = [a, b]
        answer = a + b
        problems.append((question, answer, '+'))
    return problems

def generate_multiplication_problems(num_problems, lower_bound=1, upper_bound=10):
    problems = []
    for _ in range(num_problems):
        a = np.random.randint(lower_bound, upper_bound + 1)
        b = np.random.randint(lower_bound, upper_bound + 1)
        question = [a, b]
        answer = a * b
        problems.append((question, answer, '*'))
    return problems
