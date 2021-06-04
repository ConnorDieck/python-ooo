from random import choice

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    "Finds random words from a dictionary"

    def __init__(self, file):
        self.file = file
        self.wordlist = []

        self.readwords()
    
    def readwords(self):
        file = open(self.file, "r")
        numwords = 0

        for line in file:
            self.wordlist.append(line)
            numwords += 1
        
        file.close()
        print(f"{numwords} words read")
    
    def random(self):
        randword = choice(self.wordlist)
        randword = randword[0:(len(randword)-1)]
        return randword
