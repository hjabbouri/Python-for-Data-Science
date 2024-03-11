import numpy as np

# TODO handel error cases size of the list and the start and end index __doc__


def slice_me(family: list, start: int, end: int) -> list:
    arr = np.array(family)
    print('My shape is: ', arr.shape)
    print('My new shape is: ', arr[start:end].shape)
    # print(arr[start:end])
    return arr[start:end]
