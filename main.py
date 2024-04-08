import chess
import chess.svg
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from engine import Engine
from mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    board = chess.Board()
    engine = Engine(board)

    print("Enter 'exit' to quit")

    while not board.is_game_over():
        move = input("Enter a move: ")

        if move == "exit":
            exit()
    
        if not board.is_legal(chess.Move.from_uci(move)):
            print("Invalid move")
            continue

        engine.move(move)
        window.setBoard(board)

        board = engine.randomMove(board)
        window.setBoard(board)

        print(engine.score_board())

    app.exec()