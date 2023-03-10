# Main driver File. Handles user input and displaying current GameState object.

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 IS ANOTHER OPTION. SMT DIVISIBLE BY 8
DIMENSION = 8 #dimensions of a chess board are 8*8
SQ_SIZE = HEIGHT//DIMENSION 
MAX_FPS = 15 # for animation later on
IMAGES = {}

# Initialize a global repo of images. To be called once in the main.
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        # Now we can access an image by saying 'IMAGES['wp']'   

# Main Driver for code. This will handle user input and updating the graphics

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves =  gs.getValidMoves()
    moveMade = False # Flag variable for when a move is mad

    loadImages()
    running = True
    sqSelected = () #no square selected initially. Keeps track of the last click of the user (tuple: (row,col))
    playerClicks = [] # keep track of player clicks (two tuples: [(6,4), (4,4)])

    while running:
        # if we have a Quit event then the while loop will stop
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # x,y location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col): # the user clicked the square twice
                    sqSelected = () # deselect
                    playerClicks = [] # clear player clicks
                
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected) # appends for both first and second clicks
                # now if it was the users second click we need to do smt
                if len(playerClicks) == 2: # after second click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = () #clears sqSelected and playerClicks to allow user to make more that one move. 
                    playerClicks = []
            #key handlers
            elif e.type ==p.KEYDOWN:
                if e.key == p.K_z: #undo when 'z' is pressed
                    gs.undoMove()
                    


        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
        
 #responible for all graphics within current GameState
def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    # add in placece highlighting or move suggestion
    drawPieces(screen, gs.board)# draw pieces on the board

#draw squares on board. Top left square is always light
def drawBoard(screen):
    colors = [p.Color('white'), p.Color('Gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

#draw the pieces on the board using the current GameState.board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))




if __name__  == "__main__":
    main()

main()