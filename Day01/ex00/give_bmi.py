import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """"""
    return list(np.divide(np.array(weight), np.array(height) ** 2))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """"""
    return [b > limit for b in bmi]
