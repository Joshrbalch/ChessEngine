import chess
import chess.svg
import chess.engine
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from engine import Engine
from mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    print("Enter 'exit' to quit")

    user_side = input("White or black? (w/b): ")

    if user_side == "b":
        window.setFlipFlag(1)

    board = chess.Board()
    engine = Engine(board, chess.WHITE)

    window.renderBoard()
    window.show()

    while not board.is_game_over():
        if board.turn == chess.WHITE and user_side == "w":
            print("Score: ", engine.getScore())
            move = input("Enter a move: ")

            if move == "exit":
                exit()
        
            if not board.is_legal(chess.Move.from_uci(move)):
                print("Invalid move")
                continue

            engine.move(move)
            window.setBoard(board)
            
        elif board.turn == chess.BLACK and user_side == "b":
                print("Score: ", engine.getScore() * -1)
                move = input("Enter a move: ")

                if move == "exit":
                    exit()
            
                if not board.is_legal(chess.Move.from_uci(move)):
                    print("Invalid move")
                    continue

                engine.move(move)
                window.setBoard(board)

        else:
            move = engine.computeMove(board)
            board.push(move)
            window.setBoard(board)