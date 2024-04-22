import chess
import chess.svg
import random

class CandidateMove:
    def __init__(self, move, score):
        self.move = move
        self.score = score
        self.children = []

    def set_move(self, move):
        self.move = move

    def add_child(self, child):
        self.children.append(child)

    def set_score(self, score):
        self.score = score

class BoardTree:
    root = None

    def __init__(self, board):
        self.board = board
        self.children = []
        self.root = CandidateMove(None, 0)  # Initialize root with None move
    
    def evaluate_material(self, board):
        PV = {
            'pawn': 100,
            'knight': 320,
            'bishop': 330,
            'rook': 500,
            'queen': 950
        }

        DRAW_VALUE = 0

        if board.is_insufficient_material():
            return DRAW_VALUE

        wp = len(board.pieces(chess.PAWN, chess.WHITE))
        bp = len(board.pieces(chess.PAWN, chess.BLACK))

        wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(board.pieces(chess.KNIGHT, chess.BLACK))

        wb = len(board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(board.pieces(chess.BISHOP, chess.BLACK))

        wr = len(board.pieces(chess.ROOK, chess.WHITE))
        br = len(board.pieces(chess.ROOK, chess.BLACK))

        wq = len(board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(board.pieces(chess.QUEEN, chess.BLACK))

        value = (
            PV['pawn'] * (wp - bp) +
            PV['knight'] * (wn - bn) +
            PV['bishop'] * (wb - bb) +
            PV['rook'] * (wr - br) +
            PV['queen'] * (wq - bq)
        )

        if board.turn == chess.WHITE:
            return value
        return -value
    
    def evaluate_king_safety(self, board):
        king_position = board.king(board.turn)
        enemy_attackers = board.attackers(not board.turn, king_position)

        # If the king is under attack, penalize the position
        if enemy_attackers:
            return -100

        # Otherwise, reward positions where the king has castle options
        if board.has_kingside_castling_rights(board.turn) or board.has_queenside_castling_rights(board.turn):
            return 50

        return 0

    def evaluate_piece_activity(self, board):
        activity_score = 0

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                # Reward pieces that have more available moves
                mobility_score = len(list(board.attacks(square)))
                activity_score += mobility_score

        return activity_score
    
    def reward_capture(self, board, move):
        # Make the move on a copy of the board
        new_board = board.copy()
        new_board.pop()

        if new_board.is_capture(move):
            return 150
        
        # Ensure the move is legal before pushing it

        # No capture or illegal move, return 0
        return 0

    def calculate_score(self, board):
        material_score = self.evaluate_material(board)
        king_safety_score = self.evaluate_king_safety(board)
        piece_activity_score = self.evaluate_piece_activity(board)
        capture_score = self.reward_capture(board, board.peek())

        total_score = material_score + king_safety_score + piece_activity_score + capture_score

        if board.is_checkmate():
            if board.turn == chess.WHITE:
                return -9999
            return 9999
        if board.is_stalemate():
            return 0
        
        return total_score, material_score, king_safety_score, piece_activity_score, capture_score
    
    def get_best_move(self, depth):
        self.populate_root_children(depth)
        best_move = self.root.children[0]

        print("Legal Moves: ", self.board.legal_moves)

        for child in self.root.children:
            print("Move: ", child.move, " Score: ", child.score)
            if child.score > best_move.score:
                best_move = child

        if best_move.score == 0:
            best_move = random.choice(self.root.children)

        print("Best move: ", best_move.move, " Score: ", best_move.score)
        self.root.children = []  # Clear children list for next move
        return best_move.move

    def populate_tree(self, depth, board, node):
        if depth == 0:
            return

        for move in board.legal_moves:
            board.push(move)
            score = self.calculate_score(board)  # Evaluate position after making the move
            child_node = CandidateMove(move, score)  # Create a child node for each legal move
            node.add_child(child_node)  # Add child node to the parent node's children list
            self.populate_tree(depth - 1, board, child_node)  # Recursively populate children
            board.pop()

    def populate_root_children(self, depth):
        self.populate_tree(depth, self.board, self.root)

    def get_board(self):
        return self.board


class Engine:
    tree = BoardTree(chess.Board())
    
    def __init__(self, board, side):
        self.board = board
        self.chessboardSvg = chess.svg.board(self.board).encode("UTF-8")

        if side == 1:
            self.side = "b"
        else:
            self.side = "w"

    def getScore(self):
        return self.tree.evaluate_material(self.board)

    def move(self, move):
        self.board.push(chess.Move.from_uci(move))
        self.chessboardSvg = chess.svg.board(self.board).encode("UTF-8")
        return self.chessboardSvg
    
    def randomMove(self, board):
        move = random.choice(list(board.legal_moves))
        board.push(move)
        return board
    
    def computeMove(self, board):
        # Make a copy of the current board
        new_board = self.board.copy()

        # Populate the tree based on the copied board
        self.tree = BoardTree(new_board)
        self.tree.populate_root_children(3)

        # Get the best move from the tree
        best_move = self.tree.get_best_move(3)

        # Ensure the best move is for the side the engine controls
        new_board.push(best_move)

        return best_move

    def get_board(self):
        return self.board
