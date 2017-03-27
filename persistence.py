def persistence(n):
    """
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative
    persistence, which is the number of times you must multiply the digits in num until you reach a single
    digit.

    >>> persistence(999)
    4
    >>> persistence(39)
    3

    :param n: integer
    :return:
    """
    current_number = n
    while_loop = 0
    while len(str(current_number)) > 1:
        next_number = 1
        for i in str(current_number):
            next_number *= int(i)
        current_number = next_number
        #print(current_number)
        while_loop += 1

    return while_loop


if __name__ == '__main__':
    import doctest
    doctest.testmod()
