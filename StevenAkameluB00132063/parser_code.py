# -----------------------------------------------------
# parser_core.py
# Defines:
# - Node class -> used to build a parse tree
# - Parser class -> recursive descent parser using rules.txt and lexicon.txt
# -----------------------------------------------------

class Node:
    """
    A node represents one element in the parse tree:
    Example:
        NP
        /  \
      DT   NN
    label = category (S, NP, DT, NN, VP, PP, etc.)
    children = list of child nodes or words from the sentence
    """
    def __init__(self, label, children=None):
        self.label = label  # The name of the node (NP, S, VP, etc.)
        self.children = children or [] # The thing inside the node

    def __repr__(self):
        # Formats the node in thd bracket: [NP [DT The] [NN king]]
        return f"[{self.label} {' '.join(str(c) for c in self.children)}]"

    def pretty(self, indent=0):
        print("  " * indent + self.label)
        for child in self.children:
            if isinstance(child, Node):
                child.pretty(indent + 1)  # Recursively prints the child nodes
            else:
                print("  " * (indent + 1) + child)  # Prints word


class Parser:
    """
    Very simple recursive-descent parser.
    Grammar structure is guided by rules.txt.
    """

    def __init__(self, lexicon, pos_set, rules):
        self.lexicon = lexicon  # Dictionary of words → POS entries
        self.pos_set = pos_set  # List of all POS tags
        self.rules = rules      # List of GrammarRule objects

        # Values used during parsing
        self.tokens = [] # Words in the sentence
        self.position = 0 # Current position in the sentence
        self.subject_number = None   # Used for agreement (sg/pl)


    # Return the current word we are trying to parse
    def current_word(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    #Try to match a POS tag at the current position
    def match_pos(self, wanted_pos):
        """
        Checks if current word has the POS tag we need.
        or it returns None if it doesn't match.
        """
        word = self.current_word()
        if word is None:
            return None

        # Retrieve all lexicon entries for the lowercased word
        word_entries = self.lexicon.get(word.lower(), [])

        # Checks each entry to see if its POS matches
        for entry in word_entries:
            if entry.pos == wanted_pos:
                # matches!
                self.position += 1

                # if it's the subject noun, store number
                if wanted_pos in ("NN", "NNS") and self.subject_number is None:
                    self.subject_number = entry.number

                # Return a Node representing the POS tag & word
                return Node(wanted_pos, [word])

        return None

    # ------------- Grammar rules Eg: S → NP VP -------------

    def parse_S(self):
        start = self.position # Saves the starting point in case we fail

        np = self.parse_NP() # Try to parse the subject noun phrase NP
        if np is None:
            self.position = start
            return None

        vp = self.parse_VP() # Try to parse the verb phrase VP
        if vp is None:
            self.position = start
            return None

        #  If both NP and VP succeeded, return the S node
        return Node("S", [np, vp])

    # Grammar Rule: NP → DT NN
    #                NP → DT JJ NN
    #                NP → DT NNS

    def parse_NP(self):
        start = self.position  # Remembers position for going back

        # Every NP must start with a determiner (DT)
        det = self.match_pos("DT")
        if det is None:
            self.position = start
            return None

        # Try NP -> DT JJ NN
        adj = self.match_pos("JJ")
        noun = self.match_pos("NN")
        if noun:
            children = [det]
            if adj:
                children.append(adj)
            children.append(noun)
            return Node("NP", children)
        
        

        # If NP→DT JJ NN failed, try NP→DT NNS (plural noun)
        self.position = start + 1   # Move back to just after the DT
        nns = self.match_pos("NNS")
        if nns:
            return Node("NP", [det, nns])

        # No valid noun phrase structure was found
        self.position = start
        return None

        # PP → IN NP
    def parse_PP(self):
        start = self.position

        prep = self.match_pos("IN")
        if not prep:
            self.position = start
            return None

        np = self.parse_NP()
        if not np:
            self.position = start
            return None

        return Node("PP", [prep, np])

    # ---------------------------------------------------
    # Grammar Rule: VP → VBZ NP
    #                VP → VB NP
    # ---------------------------------------------------
    def parse_VP(self):
        start = self.position

        # First try VP with singular verb: VBZ (likes/dislikes)
        v_sing = self.match_pos("VBZ")
        if v_sing:
            # Agreement check: singular verb + plural subject → warning
            if self.subject_number == "pl":
                print("⚠️ Agreement warning: plural subject with singular verb")

            np = self.parse_NP()
            if np:
                return Node("VP", [v_sing, np])

        # Reset and try plural/base verb: VB (like/dislike)
        self.position = start
        v_pl = self.match_pos("VB")
        if v_pl:
            # Checking for agreement: plural verb + singular subject
            if self.subject_number == "sg":
                print("⚠️ Agreement warning: singular subject with plural verb")

            np = self.parse_NP()
            if np:
                return Node("VP", [v_pl, np])

        # No VP found
        self.position = start
        return None


   
    def parse(self, sentence):
        # Split sentence into words
        self.tokens = sentence.split()

        # Reset parser state
        self.position = 0
        self.subject_number = None

        # Start parsing from rule S
        tree = self.parse_S()

        # Parsing succeeds only if:
        # - We built a valid tree
        if tree and self.position == len(self.tokens):
            return tree, True

        return None, False