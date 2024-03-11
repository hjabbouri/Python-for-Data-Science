from sys import argv


def main():
    try:
        ERR_MSG = 'The arguments are bad'
        assert len(argv) == 2, ERR_MSG
        assert isinstance(argv[1], str) is True, ERR_MSG
        assert argv[1].isalnum() is True or argv[1].count(' ') > 0, ERR_MSG
        dict = {
            ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
            'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
        }
        print(' '.join([dict[c.upper()] for c in argv[1]]))
    except AssertionError as e:
        print('AssertionError:', e)


if __name__ == '__main__':
    main()
