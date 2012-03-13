def between(first, last):
    count = 0
    while first != last:
        if prime(first) == 'prime!':
                print str(count)+ '. '  + str(first)
                count += 1
        first+= 1



def prime(dig):
    count = 2
    while count <= dig/2:
        if dig % count == 0:
            return 'not prime'
        count = count + 1
    return 'prime!'    

def main():
    between(1000, 50000)
    
if __name__ == '__main__':
    main()
