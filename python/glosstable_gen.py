def glosstable_gen(filepath):
    """
    Generates gloss tables for Attic Greek sentences. Note: there's something
    weird about the width of Greek characters, as they aren't quite
    monospaced. Therefore, the output should be corrected by hand.
    """
    sentences = open(filepath, 'r')
    for sentence in sentences:
        print("\n")
        print("| Greek word       | Type  | Gloss | Meaning |")
        print("|------------------|-------|-------|---------|")
        for word in sentence.split():
            print("| {0:17}|   |   |   |".format(word))

glosstable_gen("sappho-31-lines.txt")
