#verbeteringen:
# kolom, rij en quadrant in een lijst stoppen
# deze lijst controleren door moiddel van count
# quadrant slimmer herkennen
import copy
import time
def check(the_list,value):
    if the_list.count(value)> 1:
        return 0
    else:
        return 1

#checking the row
def check_row(sudoku, row, value):
    return check(sudoku[row],value)

def check_column(sudoku, column, value):
    awesomelist = []
    for i in sudoku:
        awesomelist.append(i[column])
    return check(awesomelist,value)    
    
def check_quadrant(sudoku, row, column, value):
    if row < 3 and column < 3:
        return checking(sudoku, 0, 0,value)
    if row < 3 and column <6:
        return checking(sudoku, 0, 3,value)
    if row < 3 and column >5:
        return checking(sudoku, 0, 6,value)
    if row < 6 and column <3:
        return checking(sudoku, 3, 0,value)
    if row < 6 and column <6:
        return checking(sudoku, 3, 3, value)
    if row < 6 and column >5:
        return checking(sudoku,3, 6,value)
    if row > 5 and row <3:
        return checking(sudoku, 6, 0,value)
    if row > 5 and column < 6:
        return checking(sudoku, 6, 3,value)
    if row >5 and column > 5 :
        return checking(sudoku, 6, 6,value)

def checking(sudoku, row, column, value):
    superlist = []
    #print  sudoku
    ocolumn = column
    counter = row + 3
    counter2 = column + 3
    while row <  counter:
        #print  'row:',
        #print  row
        while column < counter2:
            #print  'column:',
            #print  column
            superlist.append(sudoku[row][column])
            column += 1
        row += 1
        column = ocolumn
    #print  superlist
    return check(superlist, value)        
    

#analyses a move by quadrant, row and column        
def legal(sudoku, row, column, value):
    returnvalue = 0
    if check_row(sudoku, row, value) ==1:
        #print  'rows ok'
        if check_column(sudoku, column,value) == 1: 
            #print  'columns ok'
            if check_quadrant(sudoku, row, column,value) ==1:
                #print  'quads ok'
                returnvalue =1
    return returnvalue


#makes all (not just legal) moves, given a sudoku
def new_moves(sudoku):
    all_moves = []
    rowc = 0
    columnc = 0
    counter = 1
    for row in sudoku:
        for element in row:
            if element == ' ':
                while counter <=9:
                    sudoku[rowc][columnc] = counter
                    if legal(sudoku, rowc, columnc,counter)==1:
                        new_sudoku = copy.deepcopy(sudoku)
                        all_moves.append(new_sudoku)
                    counter+=1
            columnc +=1
        rowc +=1
        columnc = 0
    return all_moves

#checks for empty space        
def empty_space(sudoku):
    returnvalue = 0
    for row in sudoku:
        for element in row:
            if element == ' ':
                returnvalue = 1
                break
    return returnvalue

def solve(nodes):
    #while the first node has an empty space
    while empty_space(nodes[0]) == 1:
        #we choose the first node
        first_node = nodes[0]
        #remove it from the list
        nodes.remove(first_node)
        #new_nodes contains a list of all legal moves
        #based on firt_node
        for i in new_moves(first_node):
            nodes.append(i) 
    return nodes[0]    

def main():
    start =time.time()
    solved= solve([[[' ',2,' ',' ', ' ',3, 5, ' ', ' ',], [' ', 5, 7, ' ', 8, ' ', ' ', ' ', 9], [9,8, ' ', 4, 1, ' ', ' ', ' ', ' '],[7,' ',' ',' ',' ',' ',' ',5,' '], [1,' ',' ',' ',' ',' ',' ',3,6],[' ',' ',' ',5,' ',6,4,9,' '],[' ',7,' ',' ',' ',4,' ',' ',3], [3,' ',' ',2,' ',' ',' ',8,' '], [' ',' ',2,1,' ',8,' ',' ',' ']]])
    print  solved
    stop = time.time()
    print  stop - start
    
if __name__ == '__main__':
    main()
