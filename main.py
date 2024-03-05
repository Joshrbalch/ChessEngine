import chess
import chess.svg
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from engine import Engine

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 550, 550)
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(5, 5, 540, 540)
        self.chessboard = chess.Board()
        self.renderBoard()

    def renderBoard(self):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def setBoard(self, board):
        self.chessboard = board
        self.renderBoard()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    board = chess.Board()
    engine = Engine(board)

    while not board.is_game_over():
        move = input("Enter a move: ")
        
        if move == "exit":
            break
    
        if not board.is_legal(chess.Move.from_uci(move)):
            print("Invalid move")
            continue

        engine.move(move)
        window.setBoard(board)

        board = engine.randomMove(board)
        window.setBoard(board)

    app.exec()
