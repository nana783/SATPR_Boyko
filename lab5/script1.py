def find_maximin(matrix):
    # Finding maximin (lower game price) for player A
    maximin = max([min(row) for row in matrix])
    return maximin

def find_minimax(matrix):
    # Finding minimax (upper game price) for player B
    minimax = min([max(row) for row in zip(*matrix)])
    return minimax



# Game matrix
game_matrix = [
    [4, -4, -5, 6],
    [-3, -4, -9, -2],
    [6, 7, -8, -9],
    [7, 3, -9, 5]
]

# Finding maximin, minimax
maximin_value = find_maximin(game_matrix)
minimax_value = find_minimax(game_matrix)


# Displaying the results
print(f"Maximin (lower game price) for player A: {maximin_value}")
print(f"Minimax (upper game price) for player B: {minimax_value}")

