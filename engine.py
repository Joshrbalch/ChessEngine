import chess
import chess.svg

class Engine:
    def __init__(self):
        self.board = chess.Board()
        self.chessboardSvg = chess.svg.board(self.board).encode("UTF-8")

    def move(self, move):
        self.board.push(chess.Move.from_uci(move))
        self.chessboardSvg = chess.svg.board(self.board).encode("UTF-8")
        return self.chessboardSvg
    
    def get_board(self):
        return self.chessboardSvg