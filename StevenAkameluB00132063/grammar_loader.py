# -----------------------------------------------------
# grammar_loader.py
# Loads rules.txt and creates objects for:
# - POS tag list
# - Grammar rules Eg: like S -> NP VP)
# -----------------------------------------------------

class POSList:
    """
    Holds all parts of speech list from the first line of rules.txt.
    Example: DT NN NNS JJ VB VBZ
    """
    def __init__(self, tags):
        # Stores the list of POS tags
        self.tags = tags

    def __repr__(self):
        # Format display when printed
        return f"POSList({self.tags})"


class GrammarRule:
    """
    Represents a grammar rule like:
    S -> NP VP
    NP -> DT NN
    VP -> VB NP

    lhs = 'S'
    rhs = ['NP', 'VP']
    """
    def __init__(self, left_side, right_side):
        # Stores the left-hand side of the rule (e.g., "S")
        self.lhs = left_side

        # Store the right-hand side of the rule (e.g., ["NP", "VP"])
        self.rhs = right_side

    def __repr__(self):
        # Displays the rule (e.g., S -> NP VP)
        return f"{self.lhs} -> {' '.join(self.rhs)}"


def load_rules(path="rules.txt"):
    # Prepare empty space for POS tags and grammar rules
    pos_tags = []
    rules = []

   
    with open(path, "r", encoding="utf-8") as f:
        # reads all lines that are not empty
        lines = [line.strip() for line in f if line.strip()]

    # First line has all the POS tags separated by spaces
    pos_tags = lines[0].split()

    # Tag line is wrapped up by POSList object
    pos_set = POSList(pos_tags)

    # Remaining lines = rules
    for line in lines[1:]:
        # Skip lines starting with "#"
        if line.startswith("#"):
            continue
        # Only process the lines that has the " -> " separator
        if "->" in line:

            # Split the rule into left and right parts
            left_side, right_side = line.split("->")

            # Remove extra spaces
            left_side = left_side.strip()
            right_side = right_side.strip().split()

            # Convert this into a GrammarRule object
            rules.append(GrammarRule(left_side, right_side))

    # Return both the POS list and the full list of rules
    return pos_set, rules
