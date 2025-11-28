# -----------------------------------------------------
# main.py
# This is the main program that:
# 1. Loads my lexicon and grammar rules
# 2. Creates a Parser object
# 3. Asks the user for sentences to parse
# 4. Prints whether each sentence can be accepted or rejected
#    and shows the parse tree if accepted.
# -----------------------------------------------------

from lexicon_loader import load_lexicon
from grammar_loader import load_rules
from parser_code import Parser


def main():
    # Load lexicon entries from lexicon.txt
    lexicon = load_lexicon("lexicon.txt")

    # Load POS list and grammar rules from rules.txt
    pos_set, rules = load_rules("rules.txt")

    # Create a Parser object using the loaded data
    parser = Parser(lexicon, pos_set, rules)

    print("=== Simple Sentence Parser ===")
    print("This parser recognises sentences like:")
    print("  'The king dislikes the new cat'")
    print("  'The kings like the new cat'")
    print()
    print("Type a sentence to parse, or type 'quit' to exit.")
    print("-" * 50)

    # Main input loop: keep asking the user for sentences
    while True:
        sentence = input("Sentence> ").strip()

        # If the user types nothing, just ask again
        if not sentence:
            continue

        # Exit conditions
        if sentence.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        # Ask the user to parse the sentence
        tree, ok = parser.parse(sentence)

        if ok:
            # Sentence was accepted by the grammar
            print("\nACCEPTED: The sentence matches the grammar.\n")

            # Show bracketed representation (from __repr__)
            print("Bracketed structure:")
            print(tree)

            # Show a pretty, indented tree
            print("\nParse tree:")
            tree.pretty()
        else:
            # Sentence did not match the grammar
            print("\nREJECTED: The sentence does NOT match the grammar.\n")

        print("-" * 50)

if __name__ == "__main__":
    main()
