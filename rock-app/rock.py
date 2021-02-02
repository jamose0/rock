import sys
import numpy as np

if __name__ == "__main__":
    print('main')
    print(len(sys.argv))

    if len(sys.argv) != 2:
        print('Fatal: wrong number of args')
        quit()

    print('OK')
    fname = sys.argv[1]

    print('Filename: {}'.format(fname))
