import random

def main():
    number = random.randint(1,10)
    print number
    print 'raadt getal tussen 1-99'
    guessing(number)

def guessing(number):
    print number
    answer= input('>')
    print answer
    if answer == number:
        print 'jij wint!'
        print 'nog een keer?[j/n]'
        answer2 = raw_input('>')
        if answer2 =='j'or answer2=='':
            main()
    if answer> number:
        print 'lager'
        guessing(number)
    if answer< number:
        print 'hoger'
        guessing(number)

if __name__ == '__main__':
    main()
