
def transl(d: int, b: int) -> str:
    """
    >>> transl(2, 2)
    '10'
    >>> transl(2 ,8)
    '2'
    >>> transl(8, 2)
    '1000'
    >>> transl(8, 8)
    '10'
    >>> transl(10, 2)
    '1010'
    >>> transl(10, 8)
    '12'
    """

    l = []
    while d > 0:
        d, f = divmod(d, b)
        l.append(str(f))
    return ''.join(l[::-1])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)