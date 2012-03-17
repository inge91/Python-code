
import Players as p
import Board 
game = Board.board([0,0,0,0,0,0,0,0,0],None,p.Players.CROSS)
class TextInterface:

    def __init__(self):
        print"set"

    def gameLoop(self):
        global Board
        global game
        print "How would you like to play?"
        print "press 1 for p vs p \n >>"
        answer = raw_input()
        if(answer == '1'):
            print "answer was 1"
            while(True):
                TextInterface.playerMove(self)
                game.printBoard()
                if (game.winner() is not p.Players.NONE):
                    break
            if (game.winner() == p.Players.CROSS):
                print "cross won!"
            elif (game.winner() == p.Players.CIRKLE):
                print "cirkle won!"
            else:
                print "draw!"
            print "want to play again?[y/n] \n >>"
            answer = raw_input()
            while(answer is not 'y' or answer is not 'n'):
                print "illegal input!"
                print "want to play again?[y/n] \n >>"
                answer = raw_input()
            if(answer == 'y'):
                TextInterface.gameLoop(self)
            else:
                System.exit(0)
        else:
            print "Illegal input"
            TextInterface.gameloop(self)


    def playerMove(self):
        moveValid = False
        while(moveValid == False):
            print "Make a move! \n >>"
            i = raw_input()
            moveValid = game.makeMove(int(i))
            print moveValid


