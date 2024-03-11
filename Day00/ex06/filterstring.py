from sys import argv
from ft_filter import ft_filter


def main():
    """"""
    try:
        ERR_MSG = 'The arguments are bad'
        assert len(argv) == 3, ERR_MSG
        assert isinstance(argv[1], str), ERR_MSG
        assert argv[2].isdigit() and isinstance(int(argv[2]), int), ERR_MSG
        # filterd = ft_filter(lambda x: x > 18, [i for i in range(1, 30, 3)])
        filterd = ft_filter(lambda x: len(x) > int(argv[2]), argv[1].split())
        print(filterd)
    except AssertionError as e:
        print('AssertionError:', e)


if __name__ == '__main__':
    main()
