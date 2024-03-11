import sys

if len(sys.argv) == 1:
    sys.exit(1)

assert len(sys.argv) == 2, 'More than one argument is provided'

assert sys.argv[1].isdigit() is True and \
        isinstance(int(sys.argv[1]), int) is True, 'Argument is not an integer'

print('I\'m Even.' if int(sys.argv[1]) % 2 == 0 else 'I\'m Odd.')
