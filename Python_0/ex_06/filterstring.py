import sys
from ft_filter import ft_filter


def main(args):
    if len(args) != 3:
        raise AssertionError("Please provide a string and an integer")
    text = args[1]
    n = args[2]
    if not n.isdigit():
        raise AssertionError("The second argument must be an integer")
    n = int(n)
    if text is None:
        raise AssertionError("Please provide a string")
    else:
        words = text.split(" ")
        long_words = list(ft_filter(lambda x: len(x) > n, words))
        print(long_words)
        return 0


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)
