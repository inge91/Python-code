
import Players as p
import Board 
game = Board.board([0,0,0,0,0,0,0,0,0],None,None)
class TextInterface:

    def __init__(self):
        print"set"

    def gameLoop(self):
        global Board
        global game
        print "How would you like to play?"
        print "press 1 for p vs p"
        answer = raw_input()
        if(answer == '1'):
            while(True):
                TextInterface.playerMove(self)
                if (game.winner() is not p.NONE):
                    break
                printBoard()
        print "its a draw or someone won"


    def playerMove(game):
        moveValid = True
        while(not moveValid):
            print "Make a move!"
            i = raw_input()
            moveValid = game.move(i)


