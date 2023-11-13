import numpy as np

# Задані матриці критеріїв та альтернатив
criteria_matrix = np.array([
    [1.00, 3.00, 4.00, 2.00, 4.00, 6.00, 7.00],
    [0.33, 1.00, 3.00, 2.00, 4.00, 5.00, 6.00],
    [0.20, 0.33, 1.00, 0.50, 2.00, 3.00, 4.00],
    [0.50, 0.50, 2.00, 1.00, 3.00, 4.00, 5.00],
    [0.25, 0.25, 0.50, 0.33, 1.00, 2.00, 3.00],
    [0.17, 0.20, 0.25, 0.50, 0.33, 1.00, 2.00],
    [0.14, 0.17, 0.25, 0.50, 0.25, 0.33, 1.00]
])

# Задані матриці альтернатив
alternative_matrices = [
    np.array([
        [1.00, 3.00, 5.00],
        [0.33, 1.00, 2.00],
        [0.20, 0.50, 1.00]
    ]),
    np.array([
        [1.00, 3.00, 5.00],
        [0.33, 1.00, 2.00],
        [0.20, 0.50, 1.00]
    ]),
    np.array([
        [1.00, 3.00, 5.00],
        [0.33, 1.00, 2.00],
        [0.20, 0.50, 1.00]
    ]),
    np.array([
        [1.00, 2.00, 4.00],
        [0.50, 1.00, 3.00],
        [0.25, 0.33, 1.00]
    ]),
    np.array([
        [1.00, 2.00, 3.00],
        [0.50, 1.00, 2.00],
        [0.33, 0.50, 1.00]
    ]),
    np.array([
        [1.00, 6.00, 3.00],
        [0.17, 1.00, 0.50],
        [0.33, 2.00, 1.00]
    ]),
    np.array([
        [1.00, 7.00, 4.00],
        [0.14, 1.00, 0.33],
        [0.25, 3.00, 1.00]
    ])
]

# Нормалізація кожного елемента матриці критеріїв
normalized_criteria_matrix = criteria_matrix / np.sum(criteria_matrix, axis=0, keepdims=True)

# Нормалізація кожного елемента в кожній матриці альтернатив
normalized_alternative_matrices = [alternative_matrix / np.sum(alternative_matrix, axis=0, keepdims=True) for alternative_matrix in alternative_matrices]

# Суми елементів кожного стовбця у матриці критеріїв
sums_of_columns_criteria = np.sum(criteria_matrix, axis=0)

# Середні значення для кожного критерію
average_values_criteria = np.mean(normalized_criteria_matrix, axis=1)

# Виведемо результати для критеріїв
print("Нормалізована матриця критеріїв:")
print(normalized_criteria_matrix)
print("\nСуми елементів кожного стовбця у матриці критеріїв:")
print(sums_of_columns_criteria)
print("\nСередні значення для кожного критерію:")
print(average_values_criteria)

arrays_list = []

# Виведемо результати для кожної матриці альтернатив
for idx, alternative_matrix in enumerate(normalized_alternative_matrices):
    arrays_list.append(np.mean(alternative_matrix, axis=1))
    # Конвертація списку масивів в матрицю
matrix = np.vstack(arrays_list)
print(matrix)

# Сума добутків кожного стовбця матриці на середнє значення для кожного критерію
sumproduct_per_column = np.sum(matrix * average_values_criteria[:, np.newaxis], axis=0)

# Виведення результатів для суми добутків кожного стовбця та середніх значень для кожного критерію
print("\nРезультат:")
for idx, value in enumerate(sumproduct_per_column):
    print(f"A{idx + 1}: {value}")