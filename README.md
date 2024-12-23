# Chess Engine

This project is a custom chess engine built using the python-chess library. The engine evaluates chess positions and calculates moves based on several heuristics, including material balance, king safety, piece activity, and potential captures.
## Features

  Position Evaluation:
  - Material evaluation based on piece values.
  - King safety assessment considering attackers and castling rights.
  - Piece activity scoring based on mobility.
  - Reward for capturing opponent pieces.

  Move Generation:
  - Generates and evaluates candidate moves using a recursive tree structure.
  - Supports up to a configurable depth for move calculation.

  Random and Computed Moves:
  - Ability to generate a random legal move.
  - Computes the best move using a combination of heuristics.

## Getting Started
### Prerequisites

Python 3.7+
Install the python-chess library:

    pip install python-chess

### Running the Engine

Import the engine classes:

    import chess
    from engine import Engine

Initialize the engine with a starting board and side:

    board = chess.Board()
    engine = Engine(board, side=1)  # side=1 for Black, side=0 for White

Perform moves:

- Make a random move:

      engine.randomMove(board)

- Compute the best move:

      best_move = engine.computeMove(board)
      print("Best move:", best_move)

Get the current board state:

    print(engine.get_board())

## Project Structure
CandidateMove: 
- Represents a potential move with its associated evaluation score and children in the search tree.

BoardTree: 
- A recursive tree structure for move generation and evaluation.

Engine: 
- The main chess engine that interacts with the BoardTree to calculate and execute moves.

## Evaluation Heuristics

Material Value: 
- Assigns point values to each piece type (e.g., pawn = 100, queen = 950).

King Safety: 
- Penalizes positions where the king is under attack and rewards castling options.

Piece Activity: 
- Rewards positions where pieces have high mobility.

Captures: 
- Rewards moves that capture opponent pieces.

## Example

Below is a basic example of using the chess engine to calculate a move:

    import chess
    from engine import Engine
    
    # Initialize board and engine
    board = chess.Board()
    engine = Engine(board, side=0)  # White side
    
    # Make a move
    print("Current board:\n", board)
    best_move = engine.computeMove(board)
    print("Engine's best move:", best_move)
    
    # Apply the move
    board.push(best_move)
    print("Updated board:\n", board)

## Future Improvements

    Add more sophisticated evaluation metrics like pawn structure and control of open files.
    Implement additional search algorithms like minimax or alpha-beta pruning.
    Optimize performance for deeper move calculations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
