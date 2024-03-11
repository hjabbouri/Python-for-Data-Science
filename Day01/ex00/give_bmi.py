import numpy as np

# TODO handel the error cases list are not the same size, not int or float
# TODO __doc__


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    # return np.array(weight / (height/100) ** 2)
    return list(np.divide(np.array(weight), np.array(height) ** 2))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [b > limit for b in bmi]
