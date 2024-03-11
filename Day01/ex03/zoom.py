from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def main():
    """"""
    try:
        img = ft_load('animal.jpeg')
        print(img)
        arr = img[100:500, 450:850, 0:1]
        pic = img[100:500, 450:850, 0]
        print(f'New shape after slicing: {arr.shape} or {arr.shape[0:2]}')
        print(arr)
        plt.imshow(arr)

        data = Image.fromarray(pic)
        data.show()
        data.save('zoom.jpeg')
    except AssertionError as e:
        print(f'Error {e}')


if __name__ == '__main__':
    main()
