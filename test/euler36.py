__author__ = 'dorcas'

from tool36 import *

def main(end):
    """Main Program"""
    W = []
    Answer = 0
    for i in range(1, end):
        m = binary_rep(i)
        n = reverse_binary(m)
        if m == n:
            a = int(reverse_decimal(i))
            if i == a:
                W.append(i)
        else:
            continue
    Answer = sum(W)
    print "Sum = ", Answer
    return Answer

if __name__ == '__main__':
    main(1000000)
