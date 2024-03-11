import numpy as np
from PIL import Image


def ft_original(array) -> np.array:
    """Original color of the image received."""
    Image.fromarray(array).show(title='Figure VIII.3: Original')
    return array


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    invert = 255 - array
    Image.fromarray(invert).show(title='Figure VIII.3: Invert')
    return invert


def ft_red(array) -> np.array:
    """Red color of the image received."""
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    Image.fromarray(red).show(title='Figure VIII.3: Red')
    return red


def ft_green(array) -> np.array:
    """Green color of the image received."""
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    Image.fromarray(green).show(title='Figure VIII.4: Green')
    return green


def ft_blue(array) -> np.array:
    """Blue color of the image received."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    Image.fromarray(blue).show(title='Figure VIII.5: Blue')
    return blue


def ft_grey(array) -> np.array:
    """"""
    grey = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    Image.fromarray(grey).show(title='Figure VIII.5: Grey')
    return grey
