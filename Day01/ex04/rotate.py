import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def load_zoom_img(path: str, name: str) -> np.array:
    img = np.asarray(Image.open(path))[100:500, 450:850, 0:1]
    print(f'The shape of image is: {img.shape} or {img.shape[0:2]}')
    print(img)
    # plt.imshow(img)
    # Image.fromarray(img).show()
    # Image.fromarray(img[:, :, 0]).save(name)
    return img


def main():
    try:
        img = load_zoom_img('animal.jpeg', 'zoom.jpeg')[:, :, 0]
        rotate = np.asarray([[row[i] for row in img] for i in range(len(img))])
        print(f'New shape after Transpose: {rotate.shape}')
        plt.imshow(rotate)
        Image.fromarray(rotate).show()
    except AssertionError as e:
        print(f'Error {e}')


if __name__ == '__main__':
    main()
