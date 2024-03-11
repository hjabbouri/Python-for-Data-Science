def NULL_not_found(object: any) -> int:
    if object is None:
        print('Nothing: ', object, type(object))
    elif object is False and isinstance(object, bool):
        print('Fake: ', object, type(object))
    elif object == 0 and isinstance(object, int):
        print('Zero: ', object, type(object))
    elif object == '' and isinstance(object, str):
        print('Empty: ', object, type(object))
    elif object != float('nan') and isinstance(object, float):
        print('Cheese: ', object, type(object))
    else:
        print('Type not Found')
        return 1
    return 0
