import numpy as np

def pessimistic_criterion(matrix):
    return np.min(matrix, axis=1)

def optimistic_criterion(matrix):
    return np.max(matrix, axis=1)

def hurwicz_criterion(matrix, lambda_value):
    min_values = np.min(matrix, axis=1)
    max_values = np.max(matrix, axis=1)
    return lambda_value * min_values + (1 - lambda_value) * max_values

def laplace_criterion(matrix):
    return np.mean(matrix, axis=1)

def hodges_lehmann_criterion(matrix):
    differences = matrix - np.mean(matrix, axis=1)[:, np.newaxis]
    min_differences = np.min(differences, axis=1)
    return np.where(differences == min_differences[:, np.newaxis])

k = 5
# Задана матриця
payment_matrix = np.array([
    [180, 140, k, 245 - 4*k, 232],
    [420, 120 + 10*k, 140, 220, 100],
    [25 + 8*k, 315, 35, 49, 10*(k + 23) - 50],
    [290 - 10*k, k, 9, 100*k - 90, 201]
])

# Кількість стратегій та стовпців у матриці
num_strategies, num_columns = payment_matrix.shape

# Ініціалізація параметра lambda для критерію Гурвіца
lambda_values = [1/(k + 3) if k <= 12 else 4/k for k in range(1, 27)]
lambda_val = 0.1
# Ініціалізація ймовірностей для критерію Байєса-Лапласа
probabilities = [0.1, 0.2, lambda_val, lambda_val + 0.1, 1 - 0.1 - 0.2 - lambda_val - (lambda_val + 0.1)]

# Вирішення задачі для кожного критерію

print(f"\nLambda Value: {lambda_val}\n")
    
print("Pessimistic Criterion:")
print(pessimistic_criterion(payment_matrix))
    
print("\nOptimistic Criterion:")
print(optimistic_criterion(payment_matrix))
    
print("\nHurwicz Criterion:")
print(hurwicz_criterion(payment_matrix, lambda_val))
    
print("\nLaplace Criterion:")
print(laplace_criterion(payment_matrix))
    
print("\nHodges-Lehmann Criterion:")
print(hodges_lehmann_criterion(payment_matrix))
