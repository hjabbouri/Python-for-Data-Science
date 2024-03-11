

def odd_quartil(effect: float, arr: list[int]):
    if effect % 1 >= 0.75:
        return (arr[int(effect)-1] + arr[int(effect)] * 3)/2
    elif effect % 1 >= 0.5:
        return sum(arr[int(effect)-1:int(effect)])/2
    return (arr[int(effect)-1] * 3 + arr[int(effect)])/2


def ft_statistics(*args, **kwargs) -> None:
    arr = [i for i in args]
    len_arr = len(arr)
    sum_arr = sum(arr)
    sort_arr = sorted(arr)
    if len_arr > 0:
        # mean done
        mean = 0 if len_arr == 0 else sum_arr / len_arr
        # median done
        median = sort_arr[len_arr//2] if len_arr % 2 != 0 \
            else sum(sort_arr[len_arr//2-1: len_arr//2])/2
        # # quartil
        # effective1 = (len_arr + 3) / 4
        # effective2 = (3 * len_arr + 1) / 4
        # if effective1 % 1 == 0 and effective2 % 1 == 0:
        #     q1 = arr[int(effective1)]
        #     q3 = arr[int(effective2)]
        # else:
        #     q1 = odd_quartil(effective1, sort_arr)
        #     q3 = odd_quartil(effective2, sort_arr)

        # quartil
        """
        Yes, there's an alternative method called the "Tukey method" for \
            calculating quartiles. It involves using the position-based \
                definition of quartiles.

Here's how you can calculate quartiles using the Tukey method:

    Sort the dataset in ascending order: [1, 11, 42, 64, 360].
    Identify the positions of Q1 and Q3:
        Q1 is located at the 25th percentile (25% of the data below it).
        Q3 is located at the 75th percentile (75% of the data below it).
    Calculate the positions:
        Position of Q1 = (25/100) * (n + 1) \
            where n is the number of data points.
        Position of Q3 = (75/100) * (n + 1).
    Interpolate if necessary:
        If the position is not an integer, interpolate the values around it.\
            For Q1, take the average of the values at positions (k) and (k+1)\
                where k is the integer part of the position. For Q3,\
                    take the average of the values at positions (k) and (k+1).
    Find the values at the calculated positions.

Let's apply this method:

    Sorting: [1, 11, 42, 64, 360].
    Calculating positions:
        Position of Q1 = (25/100) * (5 + 1) = 1.5\
            (interpolate between the 1st and 2nd elements).
        Position of Q3 = (75/100) * (5 + 1) = 4.5\
            (interpolate between the 4th and 5th elements).
    Interpolating:
        Q1 = (11 + 1) / 2 = 6.
        Q3 = (64 + 360) / 2 = 212.

So, according to the Tukey method, Q1 is 6 and Q3 is 212
        """
        effective1 = (len_arr + 1) / 4
        effective2 = (3 * (len_arr + 1)) / 4
        # print(arr)
        # print(sort_arr)
        # print(effective1, effective2)
        # print(sort_arr[int(effective1)], sort_arr[int(effective2)])
        # print(arr[int(effective1)], arr[int(effective2)])
        q1 = sort_arr[int(effective1)] if effective1 % 2 == 0 else \
            (sort_arr[int(effective1) - 1] + sort_arr[int(effective1)]) / 2
        q3 = sort_arr[int(effective2)] if effective2 % 2 == 0 else \
            (sort_arr[int(effective2) - 1] + sort_arr[int(effective2)]) / 2

        # standard deviatino done
        std = pow(sum(pow(i - mean, 2) for i in arr) / len_arr, 1/2)
        # variance done
        var = sum(pow(i - mean, 2) for i in arr) / len_arr
    for _, val in kwargs.items():
        if len_arr == 0:
            print('ERROR')
        elif val == 'mean':
            print('mean :', mean)
        elif val == 'median':
            print('median :', median)
        elif val == 'quartile':
            print('quartile :', [float(q1), float(q3)])
        elif val == 'std':
            print('std :', std)
        elif val == 'var':
            print('var :', var)
