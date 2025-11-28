# -----------------------------------------------------
# lexicon_loader.py
# This file loads the lexicon.txt file.
# It defines the LexiconEntry class.
# -----------------------------------------------------

class LexiconEntry:
    """
    Represents one row in the lexicon file.

    Eg: a line from lexicon.txt:
        king NN king sg

    word  = 'king'
    pos   = 'NN'
    root  = 'king'
    num   = 'sg'
    """
    def __init__(self, word, parts_of_speech, root, number):
        # Stores the word (e.g., "king")
        self.word = word

        # Stores the part-of-speech (e.g., NN = noun)
        # Internally we call it 'pos'
        self.pos = parts_of_speech

        # Store the root form (e.g., king → king, kings → king)
        self.root = root

        # Store the number (e.g., sg = singular, pl = plural)
        self.number = number

    def __repr__(self):
        # This helps display the object when printed
        # NOTE: use self.pos (the attribute name), not self.parts_of_speech
        return f"LexiconEntry({self.word}, {self.pos}, {self.root}, {self.number})"


def load_lexicon(path="lexicon.txt"):
    """
    Reads lexicon.txt and returns a dictionary:

        lexicon[word] -> list of LexiconEntry objects

    This allows multiple parts of speech for the same word if needed.
    """
    # Create an empty dictionary to store lexicon entries
    lexicon = {}

    # Open the lexicon file
    with open(path, "r", encoding="utf-8") as f:
        # Loop through each line in the file
        for line in f:
            # Remove leading/trailing whitespace (spaces, newlines)
            line = line.strip()

            # Skip empty lines or comment lines starting with "#"
            if not line or line.startswith("#"):
                continue

            # Split the line into pieces (word, POS, root, number, and maybe comments)
            parts = line.split()

            # If there are fewer than 4 items, skip this bad line
            if len(parts) < 4:
                continue

            # Take only the first 4 items: word, POS, root, number
            word, parts_of_speech, root, number = parts[:4]

            # Create a LexiconEntry object
            entry = LexiconEntry(word, parts_of_speech, root, number)

            # If this word is not in the lexicon yet, create a new list for it
            if word not in lexicon:
                lexicon[word] = []

            # Append the entry to the list for this word
            lexicon[word].append(entry)

    # Return the dictionary full of lexicon entries
    return lexicon
