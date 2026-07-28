"""Module to implement Conway's Game of Life cellular automaton."""

def cell_life(cells, current_x, current_y):
    # All 8 neighbor directions: horizontal, vertical, and diagonal.
    other_cells = [[0, 1], [1, 0], [-1, 0], [0, -1],
                   [-1, -1], [1, 1], [1, -1], [-1, 1]]
    live_cells = 0
    # Keep row and column bounds separate to support non-square matrices.
    max_x = len(cells) - 1
    max_y = len(cells[current_x]) - 1
    for coords in other_cells:
        new_x = current_x + coords[0]
        new_y = current_y + coords[1]
        # Skip neighbors that fall outside the grid boundaries.
        if new_x >= 0 and new_y >= 0 and new_x <= max_x and new_y <= max_y:
            if cells[new_x][new_y] == 1:
                live_cells += 1
    # Apply Conway's rules:
    # Live cell survives with 2 or 3 neighbors; dies otherwise.
    # Dead cell becomes alive with exactly 3 neighbors.
    life_or_death = 0
    if cells[current_x][current_y] == 1:
        if live_cells in [2, 3]:
            life_or_death = 1
    elif live_cells == 3:
        life_or_death = 1
    return life_or_death

def duplicate_matrix(matrix):
    # Create a deep copy of the matrix so tick() can write the next
    # generation without modifying the original while iterating over it.
    new_matrix = []
    for row in matrix:
        new_row = []
        for cell in row:
            new_row.append(cell)
        new_matrix.append(new_row)
    return new_matrix

def tick(matrix):
    # Work on a copy so cell_life() always reads the current generation,
    # not a partially updated one.
    new_matrix = duplicate_matrix(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            new_matrix[x][y] = cell_life(matrix, x, y)
    return new_matrix