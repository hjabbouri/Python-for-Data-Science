from give_bmi import give_bmi, apply_limit
import numpy as np

height = [2.71, 1.15]
weight = [165.3, 38.4]

array = np.arange(2, 8)
# print(array / 2)

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
