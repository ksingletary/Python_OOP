"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        file = open(path)

        self.wrd = self.read_file(file)

        print(len(self.wrd), " words read")

    def read_file(self, file):
        """parse the file for us"""
        return [word.strip() for word in file]
    

    def random(self):

        return random.choice(self.wrd)
    
    
class SpecialWordFinder(WordFinder):
    def parse(self, file):
        """Parse file -> list of words, skipping blanks/comments."""

        for word in file:
            if word.strip() and not word.startswith("#"):
                return [word.strip()]
        



    
