import copy

class NodeState:
    def __init__(self, board):
        self.board = [row[:] for row in board]  #  Estrutura do tabuleiro

    def find_zero(self):
        """"encontra em que lugar da matriz está o espaço vazio ('0')"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def get_possible_moves(self):
        """serve para encontrar quais movimentações no eight puzzle são possiveis """
        zero_pos = self.find_zero()
        i, j = zero_pos
        moves = []

        if i > 0: 
            moves.append((i - 1, j))  # move pra cima
        if i < 2: 
            moves.append((i + 1, j))  # move pra baixo
        if j > 0: 
            moves.append((i, j - 1))  # move pra esquerda
        if j < 2: 
            moves.append((i, j + 1))  # move pra direita

        return moves

    def make_move(self, move):
        new_state = copy.deepcopy(self)
        i, j = self.find_zero()
        newI, newJ = move
        new_state.board[i][j], new_state.board[newI][newJ] = new_state.board[newI][newJ], new_state.board[i][j]
        return new_state

    def print_board(self):
        for row in self.board:
            print(row)
