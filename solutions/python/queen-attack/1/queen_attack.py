"""Module to implement Queen position and attack detection on a chessboard."""
def verify_position(row, column):
    # Validate row and column separately to provide specific error messages.
    # The board is 8x8, with valid indices from 0 to 7.
    if row < 0:
        raise ValueError("row not positive")
    elif row > 7:
        raise ValueError("row not on board")
    if column < 0:
        raise ValueError("column not positive")
    elif column > 7:
        raise ValueError("column not on board")

class Queen:
    def __init__(self, row, column):
        verify_position(row, column)
        # Double underscore triggers name mangling, preventing direct external access
        # to the raw row/column values.
        self.__row = row
        self.__column = column

    @property
    def position(self):
        # Expose position as a read-only tuple (row, column).
        return (self.__row, self.__column)

    def can_attack(self, another_queen):
        # Two queens on the same square is an invalid board state.
        if self.position == another_queen.position:
            raise ValueError("Invalid queen position: both queens in the same square")
        same_row = self.position[0] == another_queen.position[0]
        same_column = self.position[1] == another_queen.position[1]
        # On a diagonal, the absolute difference between rows equals
        # the absolute difference between columns.
        same_diagonal = abs(self.position[0] - another_queen.position[0]) == abs(self.position[1] - another_queen.position[1])
        return same_row or same_column or same_diagonal