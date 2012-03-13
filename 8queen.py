
def start(lista):
    while len(lista[0]) != 8:
        moves = legalmoves(lista[0]) 
        lista.pop(0)
        counter = 0
        while counter < len(moves):
            lista.insert(0, moves[counter])
            counter +=1
    return lista

def legalmoves(lista):
    endlist = []
    if lista == []: 
        counter = 1
        while counter < 65:
            endlist.insert(0, [counter]) 
            counter+=1
    else:
        illpositions =illegalmoves(lista)
        illpositions.sort()
        counter =1
        while counter <65:
            if counter not in illpositions:
                listb = lista + [counter]    
                endlist.insert(0, listb)
            counter+=1
    return endlist

def illegalmoves(lista):
    counter = 0
    globallist = [] 
    while counter < len(lista):
        horizontalmoves = horizontal(lista[counter])
        verticalmoves = vertical(lista[counter])
        diagonalmoves= diagonal(lista[counter])
        position = horizontalmoves + verticalmoves + diagonalmoves
        for i in position:
            globallist.insert(0, i)
        counter+=1
    globallist = globallist + lista
    return globallist

def horizontal(getal):
    getal2 = getal
    lista = []
    while getal % 8 != 0:
        getal +=1
        lista.insert(0,getal)
    while getal2-1 % 8 != 0:
        getal2 -=1
        lista.insert(0,getal2)
    return lista
    
def vertical(getal):
    getal2=getal
    lista = []
    while getal+8 < 65:
        getal= getal +8
        lista.insert(0, getal)
    while getal2-8 > 0:
        getal2 =getal2-8
        lista.insert(0,getal2)
    return lista


def diagonal(getal):
    getal2 = getal
    getal3 = getal
    getal4 = getal
    lista = []
    rightborder= [8,16,24,32,40,48,56,64]
    underborder = [1,2,3,4,5,6,7,8]
    upperborder = [57,58,59,60,61,62,63,64]
    leftborder = [1,9,17,25,33,41,49,57]
    while not ((getal in rightborder) or (getal in upperborder)):
        getal +=9
        lista.insert(0,getal)
    while not ((getal2 in underborder) or (getal2 in leftborder)):
        getal2 -= 9
        lista.insert(0,getal2)
    while not ((getal3 in leftborder) or (getal3 in upperborder)):
        getal3 += 7
        lista.insert(0,getal3)
    while not ((getal4 in underborder) or (getal4 in rightborder)):
        getal4 -= 7
        lista.insert(0,getal4)
    return lista



def main():
    lists= start([[]])
    print 'possible solution:'
    print lists[0]
    ask(lists)

def ask(lists):
    answer = raw_input('want another solution?[Y/n]')
    if answer == 'y' or answer == '':
        nlists = start(lists[1:])
        print nlists[0]
        ask(nlists)
    elif answer == 'n':
        print 'shutting down'
    else:
        print 'fuck you'
        ask(lists)

    
if __name__ == '__main__':
    main()

