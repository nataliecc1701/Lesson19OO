"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder():
    '''reads from a text file containing words, one word per line
    provides a function (wordfinder.random) which can be used to read off a random word
    
    
    >>> finder = WordFinder("words.txt")
    235886 words read
    
    returns strings
    >>> type(finder.random()) == str
    True
    
    doesn't return the same thing with repeated calls
    >>> finder.random() != finder.random()
    True
    
    the constructor removes the newline characters from the end of the string
    >>> ord(finder.random()[-1]) == 10 # newlines count as one character with an ord of 10
    False
    
    '''    
    def __init__(self, file_path):
        try:
            file = open(file_path)
            
            self.words = []
            self.iterate_lines(file)
            print(f"{len(self.words)} words read")
        
        finally:    
            file.close()
    
    def strip_newline(self, line):
        '''strips newline characters off the end of a line in the file'''
        if line != "" and line[-1] == "\n":
            return line[:-1]
        else:
            return line
    
    def iterate_lines(self, file):
        for line in file:
            self.words.append(self.strip_newline(line))
            
    def random(self):
        '''pulls a random word from the word list'''
        return choice(self.words)
    
class SpecialWordFinder(WordFinder):
    '''reads a formatted text file containing words. ignores blank lines and lines 
    beginning with #
    
    >>> finder = SpecialWordFinder("foods.txt")
    23 words read
    
    >>> finder.random()[0] == "#"
    False
    
    >>> finder.random == ""
    False
    
    >>> type(finder.random()) == str
    True
    
    this test document has a smaller pool to draw from, but three draws are distinct
    more than 99% of the time
    >>> finder.random() == finder.random() == finder.random()
    False
    
    '''
    def __init__(self, file_path):
        super().__init__(file_path)
    
    def iterate_lines(self, file):
        for line in file:
            if len(line) > 1 and line[0] != "#": # blank lines have a newline char (len of 1)
                self.words.append(self.strip_newline(line))
        
        