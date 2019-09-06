import numpy as np

def do_trick(num):
    if len(tricks) == 0:
        print "starting number is", num
    digits = [int(x) for x in str(num)]
    n = len(digits)
    
    if len(digits) != 4:
        print "number should have 4 digits only\nbut you passed %d with %d digits" % (num, n)
        quit()

    if len(np.unique(digits)) == 1:
        print "number should have at least 2 different digits\nbut you passed %d" % (num)
        quit()

    ascending = np.sort(digits)
    descending = ascending[::-1] # np.flip(ascending, 0)

    a = sum(descending[:] * 10 ** np.arange(n)[:])
    b = sum(ascending[:] * 10 ** np.arange(n)[:])
    c = max(a, b) - min(a, b)
    if c not in tricks:
        print "ascending %04d, descending %04d, difference %04d" % (a, b, c)
        tricks.append(c)
        c = '%04d' % c
        do_trick(c)
    else:
        print "BINGO!!! %s found" % tricks[-1]


tricks = []
do_trick(8710)

