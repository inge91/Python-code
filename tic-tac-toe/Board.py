################################################
#
#   Board class used to define the board space
#
#

import Players as p


class board:
    board = []
    turn = None
    lastTurn = None
   # def __init__(self):
   #     # the board
    #    self.board =[p.NONE, p.NONE, p.NONE,
     #           p.NONE, p.NONE, p.NONE,
      #          p.NONE, p.NONE, p.NONE]
       # # the player whose turn it is
        #self.turn = p.CROSS
        # index of last turn
        #self.lastTurn = None

    def __init__(self, board_state,last_made_turn, whose_turn ):
        self.board = board_state
        self.turn = whose_turn
        self.lastTurn = whose_turn

    # determine if someone has won
    def winner(self):
        if (board.checkHorizontal(self) is not p.NONE):
            return board.checkHorizontal(self)
        elif (board.checkVertical(self) is not p.NONE):
            return board.checkVertical(self)
        elif (board.CheckDiagonal(self) is not p.NONE):
            return board.checkDiagonal(self)
        else: 
            return p.NONE
    
    # check if there is a win in the horizontal row of the last turn
    def checkHorizontal(self):
        global lastTurn
        global board
        tempTurn = lastTurn
        if (lastTurn == 1 or lastTurn == 2):
            tempTurn = 0
        elif (lastTurn == 4 or lastTurn == 5):
            tempTurn = 3
        else:
            tempTurn = 6
        
        if ( board[tempTurn] == p.CROSS and board[tempTurn + 1] == p.CROSS and
                board[tempTurn + 1] == p.CROSS):
            return p.CROSS
        elif ( board[tempTurn] == p.CIRKLE and board[tempTurn + 1] == p.CIRKLE and
                board[tempTurn + 1] == p.CIRKLE):
            return p.CIRKLE
        else: return p.NONE
    
    def checkVertical(self):
        global lastTurn
        global board
        tempTurn = lastTurn
        if (lastTurn == 3 or lastTurn == 6):
            tempTurn = 0
        elif (lastTurn == 4 or lastTurn == 7):
            tempTurn = 1
        else:
            tempTurn = 2

        if ( board[tempTurn] == p.CROSS and board[tempTurn + 3] == p.CROSS and
                board[tempTurn + 6] == p.CROSS):
            return p.CROSS
        elif ( board[tempTurn] == p.CIRKLE and board[tempTurn + 2] == p.CIRKLE and
                board[tempTurn + 6] == p.CIRKLE):
            return p.CIRKLE
        else:
            return p.NONE


    def checkDiagonal(self):
        global lastTurn
        global board
        listdiag = [[board[0], board[4], board[7]], [board[6], board[4],
            board[2]]]
        listdiagone = listdiag[0]
        listdiagtwo = listdiag[1]
        
        if ( ((p.CROSS in listdiagone) and (p.CIRKLE not in listdiagone)) or
                ((p.CROSS in listdiagtwo) and (p.CIRKLE not in
                    listdiagtwo))):
            return p.CROSS
        elif (((p.CROSS not in listdiagone) and( p.CIRKLE in
            listdiagone)) or
                ((p.CROSS not in listdiagtwo) and (p.CIRKLE in
                    listdiagtwo))):
            return p.CIRKLE
        else:
            return p.NONE

        # checks if slot is full
        def isfull(self, slot):
            global board
            if (board[slot] == p.NONE):
                return False
            else:
                return True
        
        # make a move and change turn and lastTurn
        def makeMove(self, slot):
            global turn
            global lastTurn
            if (isFull(slot) or slot < 0 or slot > 8) :
                print "Invalid move"
                return false
            else:
                if (turn == p.CROSS):
                    turn = p.CIRKLE
                else:
                    turn = p.CIRKLE
                lastTurn = slot
                return true
        
        # return a list with all possible children of the board
        def children(self):
            global board
            global turn
            all_children
            copy = []
            for i in range(0, len(board)) :
                for j in range(0, len(board)) :
                    # make a new empty gameboard
                    copy = copy + [board[j]]
                if (turn == p.CROSS) :
                    child = Board(copy, lastTurn, turn)
                if (turn == p.CIRKLE) :
                    child = Board(copy, lastTurn, turn)
                # in case the move is possible add to all_children
                if( child.move(i) == true ) : 
                    all_children = all_children + child
            return all_children

    
        def printBoard(self):
            global board
            print "Board state:"
            a = ''
            for i in range (0, len(board)):
                if (board[i] == p.CROSS):
                    a = 'x'
                elif (board[i] == p.CIRKLE):
                    a = 'o'
                else:
                    a = '_'
                if ( i == 2 or i == 5):
                    print i
                else: print i,
        
            if (board[i] == p.CROSS):
                a = 'x'
            elif (board[i] == p.CIRKLE):
                a = 'o'
            else:
                a = '_'
            print "you are: " + a
                
