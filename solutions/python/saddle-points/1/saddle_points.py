"""Module to implement saddle points detection in a matrix."""


def saddle_points(matrix):
    results = []

    # An empty matrix has no saddle points.
    if not matrix:
        return results

    if irregular_matrix(matrix):
        raise ValueError("irregular matrix")

    # Check every cell: it is a saddle point if it is the tallest
    # in its row and the smallest in its column.
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            current_tree_height = matrix[row][column]
            is_tallest_tree = is_tallest_tree_in_row(matrix, current_tree_height, row, column)
            is_smallest_tree = is_smallest_tree_in_column(matrix, current_tree_height, column)
            if is_tallest_tree and is_smallest_tree:
                # Positions in the output are 1-based.
                results.append({"row": row + 1, "column": column + 1})
    return results


def irregular_matrix(matrix):
    # A matrix is irregular if any row has a different length from the first one.
    for row in range(len(matrix)):
        if len(matrix[row]) != len(matrix[0]):
            return True
    return False


def is_tallest_tree_in_row(matrix, tree_height, row_index, column_index):
    # Compare the tree against every other tree in its row.
    # Equal heights are allowed, only a strictly taller tree disqualifies it.
    for column in range(len(matrix[row_index])):
        if column != column_index:
            if tree_height < matrix[row_index][column]:
                return False
    return True


def is_smallest_tree_in_column(matrix, tree_height, column_index):
    # Compare the tree against every tree in its column.
    # The tree itself is included, but it can never be strictly smaller than itself.
    for row in range(len(matrix)):
        if tree_height > matrix[row][column_index]:
            return False
    return True