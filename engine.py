import chess
import chess.svg
import random

class Engine:
    def __init__(self, board):
        self.board = board
        self.chessboardSvg = chess.svg.board(self.board).encode("UTF-8")

    def move(self, move):
        self.board.push(chess.Move.from_uci(move))
        self.chessboardSvg = chess.svg.board(self.board).encode("UTF-8")
        return self.chessboardSvg
    
    def randomMove(self, board):
        move = random.choice(list(board.legal_moves))
        board.push(move)
        return board
    
    def get_board(self):
        return self.board