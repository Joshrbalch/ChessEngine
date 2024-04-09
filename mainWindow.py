from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
import chess
import chess.svg

class MainWindow(QWidget):
    FLIP_FLAG = 0

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 550, 550)
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(5, 5, 540, 540)
        self.chessboard = chess.Board()

    def setFlipFlag(self, flag):
        self.FLIP_FLAG = flag

    def renderBoard(self):
        self.chessboardSvg = chess.svg.board(self.chessboard, flipped = self.FLIP_FLAG).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def setBoard(self, board):
        self.chessboard = board
        self.renderBoard()