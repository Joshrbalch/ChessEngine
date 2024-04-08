import chess
import chess.svg
import random

class CandidateMove:
    def __init__(self, move, score):
        self.move = move
        self.score = score
        self.children = []

    def init_children(self, board, depth):
        if depth == 0:
            return
        
        for move in board.legal_moves:
            child = CandidateMove(move, 0)
            self.children.append(child)

        depth -= 1

    def set_move(self, move):
        self.move = move

    def add_child(self, child):
        self.children.append(child)
    
    def set_score(self, score):
        self.score = score

class BoardTree:
    def __init__(self, board):
        self.board = board
        self.children = []

        root = CandidateMove(None, 0)
    
    def get_board(self):
        return self.board

class Engine:
    tree = BoardTree(chess.Board())
    
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