import sys


def main(args):
    if (len(args) == 2 or len(args) > 2):
        print("Usage: python building.py [text]")
        sys.exit(1)
    if len(args) >= 2:
        text = args[1]
        if text is None:
            print("Please provide a string")
            sys.exit(1)
        else:
            upper = 0
            lower = 0
            punct = 0
            space = 0
            digit = 0
            for c in text:
                if c.isupper():
                    upper += 1
                elif c.islower():
                    lower += 1
                elif c.isspace():
                    space += 1
                elif c.isdigit():
                    digit += 1
                else:
                    punct += 1
            print(f"The text contains {len(text)} characters:")
            print(f"{upper} upper letters")
            print(f"{lower} lower letters")
            print(f"{punct} punctuation marks")
            print(f"{space} spaces")
            print(f"{digit} digits")
    else:
        input_text = input("What is the text to count?\n")
        upper = 0
        lower = 0
        punct = 0
        space = 0
        digit = 0
        for c in input_text:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c.isspace():
                space += 1
            elif c.isdigit():
                digit += 1
            else:
                punct += 1
        print(f"The text contains {len(input_text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")


if __name__ == "__main__":
    main(sys.argv)
