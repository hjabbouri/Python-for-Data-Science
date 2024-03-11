def all_thing_is_obj(object: any) -> int:
    typ = type(object)
    if typ is list:
        print(f'List: {typ}')
    elif typ is tuple:
        print(f'Tuple: {typ}')
    elif typ is set:
        print(f'Set: {typ}')
    elif typ is dict:
        print(f'Dict: {typ}')
    elif typ is str:
        print(f'{object} is in the kitchen: {typ}')
    else:
        print('Type not found')
    return 42
