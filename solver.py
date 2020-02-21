import pprint


class Solver():


    def __init__(self, grid):
        self.grid = grid

    def __repr__(self):
        pprint.PrettyPrinter(self.grid)

    def solve(self):

        for x in range(1, 10):
            for y in range(1, 10):
                if self.grid[x][y] != "" or self.grid[x][y] != None:
                    return jdkfl

    def validate_board(self):

        # Validate columns
        for column in range(1, 10):
            unique_nums = []
            for row in range(1, 10):
                if unique_nums.count(self.grid[row][column]) > 1:
                    return False
                else:
                    unique_nums.append(self.grid[row][column])

        # Validate Rows
        for row in range(1, 10):
            unique_nums = []
            for column in range(1, 10):
                if unique_nums.count(self.grid[row][column]) > 1:
                    return False
                else:
                    unique_nums.append(self.grid[row][column])

        # Validate Grids
        for starting_cell_column in range(1, 10, 3):
            for starting_cell_row in range(1, 10, 3):
                unique_nums = []
                for column in range(starting_cell_column, starting_cell_column + 3):
                    for row in range(starting_cell_row, starting_cell_row + 3):
                        if unique_nums.count(self.grid[row][column]) > 1:
                            return False
                        else:
                            unique_nums.append(self.grid[row][column])
        return True
