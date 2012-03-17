
import Players as p

# minimax returns index of next move
def minimax(state, player):
    newstate = minimaxDecision(state, player)
    print newstate.board
    print state.board
    for i in range(0, len(newstate.board)):
        if (not (newstate.board[i] == state.board[i])):
            print "value of i"
            print i
            return i
    print "there are no differences"

# calculates best decision
def minimaxDecision(state, player):
    bestState = None
    for i in state.children():
        if(player == p.Players.CROSS):
            if (maxValue(i, player) == 1):
                return i
            elif(maxValue(i, player == 0)):
                bestState = i 
            else:
                allBad = i;
        else:
            if (minValue(i, player) == 1):
                return i
            elif(minValue(i, player == 0)):
                bestState = i 
            else:
                allBad = i;
    if(bestState == None):
        return allBad
    else:
        return bestState

# maxvalue function
def maxValue(state, player):
    if (state.winner() is not p.Players.NONE or state.boardFull()):
        return utility(state, player)
    v = 9999
    for a in state.children():
        v = max(v, minValue(a, player))
    return v

# minvalue function
def minValue(state, player):
    if (state.winner() is not p.Players.NONE or state.boardFull()):
        return utility(state, player)
    v = - 9999
    for a in state.children():
        v = min(v, minValue(a, player))
    return v

# utility function
def utility(state, player):
    if( state.boardFull()):
        return 0
    if( state.winner() == player):
        return 1
    else:
        return -1






