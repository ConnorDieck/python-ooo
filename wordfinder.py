from random import choice

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    "Finds random words from a dictionary"

    def __init__(self, file):
        self.word_file = open(file)
        
        self.words = self.readwords()

        print(f"{len(self.words)} words read")
    
    def readwords(self):
        "Reads words from file and prints the numbers of lines read"
        numwords = 0

        return [word.strip() for word in self.word_file]
        
    
    def random(self):
        "Returns a random word from file"
        randword = choice(self.words)
        return randword

class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)

    def readwords(self):
        "Reads words from file and prints the numbers of lines read"
        return [word.strip() for word in self.word_file if word.strip() and not word.startswith("#")]

# Original attempt:
# -------------------------
# class WordFinder:
#     "Finds random words from a dictionary"

#     def __init__(self, file):
#         self.file = file
#         self.wordlist = []

#         self.readwords()
    
#     def readwords(self):
#         "Reads words from file and prints the numbers of lines read"
#         file = open(self.file, "r")
#         numwords = 0

#         for line in file:
#             self.wordlist.append(line)
#             numwords += 1
        
#         file.close()
#         print(f"{numwords} words read")
    
#     def random(self):
#         "Returns a random word from file"
#         randword = choice(self.wordlist)
#         randword = randword[0:(len(randword)-1)]
#         return randword

# class SpecialWordFinder(WordFinder):
#     def __init__(self, file):
#         super().__init__(file)

#     def readwords(self):
#         "Reads words from file and prints the numbers of lines read"
#         file = open(self.file, "r")
#         numwords = 0

#         for line in file:
#             if line != "" or "#" not in line:
#                 self.wordlist.append(line)
#                 numwords += 1
        
#         file.close()
#         print(f"{numwords} words read")