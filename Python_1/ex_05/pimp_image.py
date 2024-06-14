import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image.
    """
    plt.figure("Figure VIII.1: Original")
    plt.imshow(array)
    plt.show()
    max_value = np.max(array)
    inverted_image = max_value - array
    plt.figure("Figure VIII.2: Invert")
    plt.imshow(inverted_image)
    plt.show()


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image to red.
    """
    red_channel = array[:, :, 0]
    red_image = np.zeros_like(array)
    red_image[:, :, 0] = red_channel
    plt.figure("Figure VIII.3: Red")
    plt.imshow(red_image)
    plt.show()


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image to green.
    """
    green_channel = array[:, :, 1]
    green_image = np.zeros_like(array)
    green_image[:, :, 1] = green_channel
    plt.figure("Figure VIII.4: Green")
    plt.imshow(green_image)
    plt.show()


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image to blue.
    """
    blue_channel = array[:, :, 2]
    blue_image = np.zeros_like(array)
    blue_image[:, :, 2] = blue_channel
    plt.figure("Figure VIII.5: Blue")
    plt.imshow(blue_image)
    plt.show()


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image to gray.
    """
    grey_image = np.dot(array, [0.2989, 0.5870, 0.1140])
    plt.figure("Figure VIII.6: Gray")
    plt.imshow(grey_image, cmap="gray")
    plt.show()
