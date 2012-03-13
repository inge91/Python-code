import os
import pickle
import requests
import bcolors
from collections import defaultdict
from BeautifulSoup import BeautifulSoup
import re
from clint.textui import colored
from clint.textui import puts, indent


def main():
    favorites= [ 'gaming', 'aww', 'pics', 'funny']
    url = "http://www.reddit.com"
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    soup = soup.findAll(attrs={'class':'subreddit hover'})
    listje = []
    for word in soup:
        listje = listje +  [word.text]
    wordDict = defaultdict(lambda:0)
    for word in listje:
        wordDict[word]+=1
    for word in wordDict:
        print "subreddit %s makes up for %d percent of the frontpage \n" %(word,
                (float(wordDict[word])/len(listje))*100)
    print "\n\nfor the illiterate:"
    placeholder = ''
    for word in wordDict:
        if len(word) > len(placeholder):
            placeholder = word
    listOfKeys = wordDict.keys()
    listofKeysSorted = sorted(listOfKeys,key = lambda word: wordDict[word],
            reverse = True )
    for word in listofKeysSorted:
        if word in favorites:
            print(colored.magenta(word)),
            print ((len(placeholder)+2) - len(word)) * ' ',
            print(colored.magenta(wordDict[word] *3*  '#'))
        else:
            print word,
            print ((len(placeholder)+2) - len(word)) * ' ',
            print wordDict[word] * 3 * '#'

    
if __name__ == '__main__':
    main()
