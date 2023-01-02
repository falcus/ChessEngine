# Stores Game State. Determines valid moves. Keeps a log of moves.

class GameState():
    def __init__(self):
        #Board is an 8*8 2d list, each element represents a piece with colour and class represented by letters.
        #"--" is an empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR" ],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp" ],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR" ]]
        self.whiteToMove = True
        self.moveLog = []