import sys

NESTED_MORSE = {" ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. ",
                "0": "----- "}


def main(args):
    if len(args) != 2:
        raise AssertionError("AssertionError: the arguments are bad")
    text = args[1].upper()
    if text is None and (text.isalpha() is False or text.isdigit() is False):
        raise AssertionError("AssertionError: the arguments are bad")
    else:
        morse = "".join([NESTED_MORSE.get(c, c) for c in text])
        print(morse)
        return 0


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)
