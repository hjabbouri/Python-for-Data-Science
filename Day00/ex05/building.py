import sys


def ispunct(line):
    """"""
    count = 0
    for c in line:
        if c in '!"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}~':
            count += 1
    return count


def main():
    """"""
    try:
        line = ''
        if len(sys.argv) == 1:
            line = str(input('What is the text to count?\n'))
        else:
            assert len(sys.argv) == 2, 'More than one argument is provided'
            line = sys.argv[1]
        ft_dict = {'upper': sum(c.isupper() for c in line),
                   'lower': sum(c.islower() for c in line),
                   'space': sum(c.isspace() for c in line),
                   'digit': sum(c.isdigit() for c in line),
                   'punct': sum(c in '!"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}~'
                                for c in line)}
        ft_dict_map = {'upper': sum(map(str.isupper, line)),
                       'lower': sum(map(str.islower, line)),
                       'space': sum(map(str.isspace, line)),
                       'digit': sum(map(str.isdigit, line)),
                       'punct': sum(map(ispunct, line))}
        print(f'The text contains {len(line)} characteres:')
        print(ft_dict['upper'], ' upper letters')
        print(ft_dict['lower'], ' lower letters')
        print(ft_dict['punct'], ' punctuation marks')
        print(ft_dict['space'], ' spaces')
        print(ft_dict['digit'], ' digits')
        print(ft_dict)
        print(ft_dict_map)
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
