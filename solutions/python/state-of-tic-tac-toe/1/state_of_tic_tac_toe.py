"""Module to implement the state detection of a tic-tac-toe game."""


class BoardStats:
    # Collects every statistic needed to classify a board:
    # symbol counts, winners and the progress of the line being checked.
    def __init__(self):
        self.x_count = 0
        self.o_count = 0
        self.empty_count = 0
        self.x_wins = False
        self.o_wins = False
        self.reset_current_line()

    def is_valid_turn_count(self):
        # X starts, so X can have the same number of moves as O or exactly one more.
        return self.x_count == self.o_count or self.x_count == self.o_count + 1

    def x_played_twice(self):
        return self.x_count - self.o_count > 1

    def get_validation_error(self):
        # Returns the error message for an impossible board, or an empty string if valid.
        # Order matters: turn order errors are checked before win-related errors.
        message = ""
        if self.x_played_twice():
            message = "Wrong turn order: X went twice"
        elif not self.is_valid_turn_count():
            message = "Wrong turn order: O started"
        elif ((self.x_wins and self.o_wins)
            or (self.x_wins and self.x_count == self.o_count)
            or (self.o_wins and self.x_count > self.o_count)):
            # Both players won, or the game continued after a win:
            # if X won, X must have made the last move (x_count > o_count);
            # if O won, O must have made the last move (x_count == o_count).
            message = "Impossible board: game should have ended after the game was won"
        return message

    def update_x(self, line=False):
        # line=True counts X inside the combination being checked,
        # line=False counts X on the whole board.
        if line:
            self.x_in_line += 1
        else:
            self.x_count += 1

    def update_o(self, line=False):
        if line:
            self.o_in_line += 1
        else:
            self.o_count += 1

    def update_empty(self):
        self.empty_count += 1

    def reset_current_line(self):
        self.x_in_line = 0
        self.o_in_line = 0

    def check_line_winner(self):
        # A combination with three identical symbols is a win.
        # The line counters are reset to be ready for the next combination.
        if self.x_in_line == 3:
            self.x_wins = True
        elif self.o_in_line == 3:
            self.o_wins = True
        self.reset_current_line()

    def game_status(self):
        # Assumes the board has already been validated.
        result = "ongoing"
        if self.x_wins or self.o_wins:
            result = "win"
        elif self.empty_count == 0:
            result = "draw"
        return result


def create_winning_combinations():
    # Build all 8 winning lines as tuples of (row, column) coordinates:
    # 3 rows, 3 columns and 2 diagonals.
    winning_combinations = []
    main_diagonal = []
    anti_diagonal = []
    for x in range(3):
        row = []
        column = []
        for y in range(3):
            row.append((x, y))
            # Swapping the coordinates turns a row into a column.
            column.append((y, x))
        main_diagonal.append((x, x))
        anti_diagonal.append((x, 2 - x))
        winning_combinations.append(tuple(row))
        winning_combinations.append(tuple(column))
    winning_combinations.append(tuple(main_diagonal))
    winning_combinations.append(tuple(anti_diagonal))
    return tuple(winning_combinations)


# Computed once at import time, since the combinations never change.
WINNING_COMBINATIONS = create_winning_combinations()


def gamestate(board):
    stats = BoardStats()

    # First pass: count X, O and empty cells on the whole board.
    for row in board:
        for cell in row:
            count_cell(stats, cell)

    # Second pass: check each winning line for three identical symbols.
    for combination in WINNING_COMBINATIONS:
        for row, col in combination:
            cell = board[row][col]
            count_cell(stats, cell, True)
        stats.check_line_winner()

    # Reject impossible boards before classifying the game.
    error_message = stats.get_validation_error()
    if error_message:
        raise ValueError(error_message)

    return stats.game_status()


def count_cell(stats, cell, line=False):
    # Dispatch the cell to the right counter.
    # Empty cells are only counted on the whole board, not inside a line.
    match cell:
        case "X":
            stats.update_x(line)
        case "O":
            stats.update_o(line)
        case " ":
            if not line:
                stats.update_empty()