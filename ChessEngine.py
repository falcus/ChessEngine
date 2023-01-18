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
    
    # takes a move as a parameter and executes it.
    def makeMove(self, move):
        #now we make the actual move. So we'll just be reassigning the values 
        # taking the piece from starting position to end position
        # this won't really work for castleing or en passant
        
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #logs the move. Allows us to undo it later
        self.whiteToMove = not self.whiteToMove #swapping players




class Move():
    #this will allow us to see the game slightly easier. In standard chess notation
    # We can also keep a log move that will be easier for the user to read

    # maps keys to values in rank file notation (files are columns)
    ranksToRows = {"1": 7, "2" : 6, "3" : 5, "4" : 4,
                    "5" : 3, "6" : 2, "7" : 1, "8" : 0}
    #the fww just reverses the dictionary
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b" : 1, "c" : 2, "d" : 3, 
                    "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    colsToFiles = { v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol] #this is just keeping track of information. Which blocks thhe squares would be on.

    def getChessNotation(self):
        # you can add to make this more accurate chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

        # creates a string of the row and column in notation (according to the dictionary)
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
         