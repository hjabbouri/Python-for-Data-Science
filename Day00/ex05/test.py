import sys

if __name__ == '__main__':
    line = ''
    try:
        tmp = sys.stdin.read()
        line = line + ' ' + tmp[:-1]
        print(f'{line}|{tmp}')
    except KeyboardInterrupt:
        pass
    print('final line', line)
