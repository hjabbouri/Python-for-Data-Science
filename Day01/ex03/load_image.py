import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    img = Image.open(path)
    if img.format != 'JPEG' and img.format != 'JPG':
        return np.array(0)
    np_img = np.asarray(img)
    print(f'The shape of image is: {np_img.shape}')
    return np_img
