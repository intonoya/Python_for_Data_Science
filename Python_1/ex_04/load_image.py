from numpy import array
import matplotlib.pyplot as plt
import os


def ft_load(path: str) -> array:
    if not (path.endswith('.png') or path.endswith('.jpg')
            or path.endswith('.jpeg')):
        try:
            raise AssertionError("The file has a wrong format!")
        except AssertionError as e:
            return e
    elif path is None or path == "" or not os.path.exists(path):
        try:
            raise AssertionError("The image does not exist!")
        except AssertionError as e:
            return e
    else:
        matrix = plt.imread(path)
    return matrix
