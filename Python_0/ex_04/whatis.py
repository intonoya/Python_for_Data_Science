import sys


def main(args):
    if len(args) >= 2:
        if not args[1].isdigit():
            raise AssertionError("Not a number")
        assert len(args) == 2, "More than one argument is provided"
        if len(args) >= 2:
            text = int(args[1])
            if text % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)
