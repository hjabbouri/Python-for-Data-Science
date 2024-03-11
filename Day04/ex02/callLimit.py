def callLimit(limit: int):
    """
    Wrappers around the functions AKA decorators
    a very powerful and useful tool in Python,
    allows modification (function or classs) behavior.
    Decorators wrap another function to extend
    the behavior of the wrapped function, without permanently modifying it.
    In Decorators, functions are taken as the argument into another function
    and then called inside the wrapper function.
    """
    count = 0

    def callLimiter(function):

        def limit_function(*args, **kwargs):
            nonlocal count
            count += 1
            if count <= limit:
                return function()
            else:
                print('Error:', function, 'call too many times.')
        return limit_function
    return callLimiter
