import numpy as np

class Solution:
    def gameOfLife(self, board) -> None:
        self.gen = np.array(board, dtype=np.int8)
        self.rows = self.gen.shape[0]
        self.columns = self.gen.shape[1]
        for row in range(self.rows):
            for column in range(self.columns):
                board[row][column] = self.generate_cell_state(row, column)
        print(board)

    def generate_cell_state(self, row, column):
        cell = self.gen[row][column]
        state = 0
        if row == 0:
            if column == 0:
                state = self.update_cell_0_0(cell, row, column)
            elif column == (self.gen.shape[1] - 1):
                state = self.update_cell_0_n(cell,row, column)
            else:
                state = self.update_cell_0_i(cell, row, column)
        elif row == (self.gen.shape[0] - 1):
            if column == 0:
                state = self.update_cell_n_0(cell, row, column)
            elif column == (self.gen.shape[1] - 1):
                state = self.update_cell_n_n(cell, row, column)
            else:
                state = self.update_cell_n_i(cell, row, column)
        else:
            if column == 0:
                state = self.update_cell_i_0(cell, row, column)
            elif column == (self.gen.shape[1] - 1):
                state = self.update_cell_i_n(cell, row, column)
            else:
                state = self.update_cell_i_i(cell, row, column)

        return state 
    
    def update_cell_0_0(self, cell, r, c):
        if self.rows == 1 or self.columns == 1:
            return 0

        neighbors = [self.gen[r][c+1], self.gen[r+1][c], self.gen[r+1][c+1]]
        return self.get_state(cell, neighbors)

    def update_cell_0_i(self, cell, r, c):

        if self.rows > 1 and self.columns > 1:
            neighbors = [self.gen[r][c+1], self.gen[r][c-1], self.gen[r+1][c], self.gen[r+1][c+1], self.gen[r+1][c-1]]
        
        elif self.rows == 1 and self.columns > 1:
            
            if cell == 0:
                return 0

            neighbors = [self.gen[r][c+1], self.gen[r][c-1]]

        elif self.rows > 1 and self.columns == 1:
            return 0

        return self.get_state(cell, neighbors)

    def update_cell_0_n(self, cell, r, c):

        if self.rows > 1 and self.columns > 1: 
            neighbors = [self.gen[r][c-1], self.gen[r+1][c], self.gen[r+1][c-1]]
        elif self.rows > 1 and self.columns == 1:

            if cell == 0:
                return 0

            neighbors = [self.gen[r+1][c], self.gen[r+1][c-1]]

        elif self.columns > 1 and self.rows == 1:
            return 0

        return self.get_state(cell, neighbors)



    def update_cell_n_0(self, cell, r, c):
        if self.rows == 1 or self.columns == 1:
            return 0

        neighbors = [self.gen[r][c+1], self.gen[r-1][c], self.gen[r-1][c+1]]

        return self.get_state(cell, neighbors)

    def update_cell_n_i(self, cell, r, c):
        neighbors = [self.gen[r][c+1], self.gen[r][c-1], self.gen[r-1][c], self.gen[r-1][c+1], self.gen[r-1][c-1]]
        return self.get_state(cell, neighbors)

    def update_cell_n_n(self, cell, r, c):
        neighbors = [self.gen[r][c-1], self.gen[r-1][c], self.gen[r-1][c-1]]
        return self.get_state(cell, neighbors)



    def update_cell_i_0(self, cell, r, c):

        if self.columns > 1:
            neighbors = [self.gen[r][c+1], self.gen[r-1][c], self.gen[r-1][c+1], self.gen[r+1][c], self.gen[r+1][c+1]]
        elif self.columns == 1:

            if cell == 0:
                return 0

            neighbors = [self.gen[r-1][c], self.gen[r+1][c]]

        return self.get_state(cell, neighbors)

    def update_cell_i_i(self, cell, r, c):
        neighbors = [self.gen[r][c+1], self.gen[r][c-1], self.gen[r-1][c], self.gen[r-1][c+1], self.gen[r-1][c-1], self.gen[r+1][c], self.gen[r+1][c+1], self.gen[r+1][c-1]]
        return self.get_state(cell, neighbors)

    def update_cell_i_n(self, cell, r, c):
        neighbors = [self.gen[r][c-1], self.gen[r-1][c], self.gen[r-1][c-1], self.gen[r+1][c], self.gen[r+1][c-1]]
        return self.get_state(cell, neighbors)

    def get_state(self, cell, neighbors: np.ndarray):
        result = 0
        alives = np.array(neighbors, dtype=np.int8).sum()

        if cell == 0:
            if alives == 3:
                result = 1
        else:
            if alives == 2 or alives == 3:
                result = 1

        return result

sol = Solution()
test = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

r = sol.gameOfLife(test)
