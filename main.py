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

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def paintEvent(self, board):
         self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
         self.widgetSvg.load(self.chessboardSvg) 

    def setBoard(self, board):
        self.chessboard = board

    def renderBoard(self):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

if __name__ == "__main__":
    engine = Engine()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()