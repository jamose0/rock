# JM

import sys
import numpy as np
import fileReader as fr

if __name__ == "__main__":
    print('main')
    print(len(sys.argv))

    if len(sys.argv) != 3:
        print('Fatal: wrong number of args')
        quit()

    print('[OK] -> Arg count')

    fname = sys.argv[1]

    DRAGC = sys.argv[2]
    
    print('Filename: {}, Drag C: {}'.format(fname, DRAGC))
