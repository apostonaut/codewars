

def multiplication_table(row,col):
    """
    >>> multiplication_table(2,2)
    [[1,2],[2,4]]
    >>> multiplication_table(3,3)
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    """

        # Good Luck!
    array = []
    row = [x for x in range(1, row + 1)]
    for num in range(1, col + 1):
        array.append([num*elem for elem in row])
    return array

if __name__ == "__main__":
    import doctest
    doctest.testmod()
