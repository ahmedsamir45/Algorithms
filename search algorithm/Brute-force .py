def BF(x, y):
    m = len(x)
    n = len(y)
    """
    Brute-force string matching algorithm
    :param x: pattern string
    :param m: length of pattern string
    :param y: text string
    :param n: length of text string
    """
    # Searching
    for j in range(n - m + 1):
        i = 0
        while i < m and x[i] == y[i + j]:
            i += 1
        if i >= m:
            return('found in index:',j) # or OUTPUT(j) if a function is defined

print( BF('qwer','qwdffggqwerggggqwer'))
