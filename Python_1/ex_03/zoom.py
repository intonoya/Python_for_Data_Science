from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
import os


def ft_zoom():
    """
    Zoom an image
    """
    path = "animal.jpeg"
    if not (path.endswith('.png') or path.endswith('.jpeg')
            or path.endswith('.jpg')):
        raise AssertionError("The file has a wrong format!")
    elif path is None or path == "" or not os.path.exists(path):
            raise AssertionError("The image does not exist!")
    ft_load(path)
    image = Image.open(path)
    grayscale_image = image.convert('L')
    image_array = np.array(grayscale_image)
    print(image_array)
    zoomed_image = image_array[100:500, 450:850]
    new_shape = zoomed_image.shape
    zoomed_image = np.expand_dims(zoomed_image, axis=-1)
    nnew_shape = zoomed_image.shape
    print(f"New shape after slicing is: {new_shape} or {nnew_shape}")
    print(zoomed_image)
    plt.imshow(zoomed_image, cmap="gray")
    plt.show()


def main():
    ft_zoom()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
