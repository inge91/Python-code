################################################
#
#   Board class used to define the board space
#
#

import Players as p


class board:
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
        if (board.checkHorizontal(self) is not p.Players.NONE):
            print "horizontal win"
            return board.checkHorizontal(self)
        elif (board.checkVertical(self) is not p.Players.NONE):
            print "vertical win"
            return board.checkVertical(self)
        elif (board.checkDiagonal(self) is not p.Players.NONE):
            print "diagonal win"
            return board.checkDiagonal(self)
        else: 
            return p.Players.NONE

    # check if there is a win in the horizontal row of the last turn
    def checkHorizontal(self):
        tempTurn = self.lastTurn
        if (self.lastTurn == 1 or self.lastTurn == 2):
            tempTurn = 0
        elif (self.lastTurn == 4 or self.lastTurn == 5):
            tempTurn = 3
        else:
            tempTurn = 6

        if ( self.board[tempTurn] == p.Players.CROSS 
                and self.board[tempTurn +
                    1] == p.Players.CROSS and
                self.board[tempTurn + 2] == p.Players.CROSS):
            return p.Players.CROSS
        elif ( self.board[tempTurn] == p.Players.CIRKLE
                and self.board[tempTurn + 1] == p.Players.CIRKLE and
                self.board[tempTurn + 2] == p.Players.CIRKLE):
            return p.Players.CIRKLE
        else: return p.Players.NONE

    def checkVertical(self):
        tempTurn = self.lastTurn
        print tempTurn
        if (self.lastTurn == 3 or self.lastTurn == 6):
            tempTurn = 0
        elif (self.lastTurn == 4 or self.lastTurn == 7):
            tempTurn = 1
        else:
            tempTurn = 2

        if ( self.board[tempTurn] == p.Players.CROSS and
                self.board[tempTurn + 3] == p.Players.CROSS and
                self.board[tempTurn + 6] == p.Players.CROSS):
            return p.Players.CROSS
        elif ( self.board[tempTurn] == p.Players.CIRKLE and 
                self.board[tempTurn + 3] == p.Players.CIRKLE and
                self.board[tempTurn + 6] == p.Players.CIRKLE):
            return p.Players.CIRKLE
        else:
            return p.Players.NONE


    def checkDiagonal(self):
        listdiag = [[self.board[0], self.board[4], self.board[7]], [self.board[6], self.board[4],
            self.board[2]]]
        listdiagone = listdiag[0]
        listdiagtwo = listdiag[1]

        if ( ((p.Players.CROSS in listdiagone) and (p.Players.CIRKLE not in
            listdiagone and p.Players.NONE not in listdiagone)) or
                ((p.Players.CROSS in listdiagtwo) and (p.Players.CIRKLE not in
                    listdiagtwo and p.Players.NONE not in listdiagtwo))):
                    return p.Players.CROSS
        elif (((p.Players.CROSS not in listdiagone) and( p.Players.CIRKLE in
            listdiagone and p.Players.NONE not in listdiagone)) or
            ((p.Players.CROSS not in listdiagtwo) and (p.Players.CIRKLE in
                listdiagtwo and p.Players.NONE not in listdiagtwo))):
                return p.Players.CIRKLE
        else:
            return p.Players.NONE

    # checks if slot is full
    def isfull(self, slot):
        if (self.board[slot] == p.Players.NONE):
            return False
        else:
            return True

    # make a move and change turn and lastTurn
    def makeMove(self, slot):
        if (board.isFull(self, slot) or slot < 0 or slot > 8) :
            print "Invalid move"
            return False
        else:

            self.board[slot] = self.turn
            if (self.turn == p.Players.CROSS):
                self.turn = p.Players.CIRKLE
            else:
                self.turn = p.Players.CROSS
            self.lastTurn = slot
            return True

    # checks if slot is full
    def isFull(self, slot):
        if(self.board[slot] == p.Players.NONE):
            return False
        else:
            return True

        # return a list with all possible children of the board
    def children(self):
        all_children
        copy = []
        for i in range(0, len(self.board)) :
            for j in range(0, len(self.board)) :
                # make a new empty gameboard
                copy = copy + [self.board[j]]
            if (turn == p.Players.CROSS) :
                child = Board(copy, self.lastTurn, turn)
            if (turn == p.Players.CIRKLE) :
                child = Board(copy, self.lastTurn, turn)
            # in case the move is possible add to all_children
            if( child.move(i) == true ) : 
                all_children = all_children + child
        return all_children


    def printBoard(self):
        print "Board state:"
        a = ''
        for i in range (0, len(self.board)):
            if (self.board[i] == p.Players.CROSS):
                a = 'x'
            elif (self.board[i] == p.Players.CIRKLE):
                a = 'o'
            else:
                a = '_'
            if ( i == 2 or i == 5):
                print a
            else: print a,
        
        if (self.turn == p.Players.CROSS):
            a = 'x'
        elif (self.turn == p.Players.CIRKLE):
            a = 'o'
        else:
            a = '_'
        print
        print "you are: " + a

