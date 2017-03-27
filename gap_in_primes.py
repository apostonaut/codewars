
    # The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1.
    # From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following
    # pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
    #
    # A prime gap of length n is a run of n-1 consecutive composite numbers between two
    # In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the
    # first pair between 3 and 50 with a 2-gap.


def is_prime(num):
    """
    Returns whether a number is prime.

    >>> is_prime(101)
    True
    >>> is_prime(15)
    False

    :param num: int
    :return: bool
        Whether a number is prime

    """
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                return False
    return True
    # if num <1:
    #     return 'number must be 1 or greater'
    # elif num <= 3:
    #     return True
    # elif num%2 == 0:
    #     #case where number is even:
    #     return False
    # else:
    #     for i in range(3, int(num/3) + 1, 2):
    #         if num%i == 0:
    #             return False
    # return True


def gap_in_primes(gap, m, n):
    """
    >>> gap_in_primes(4, 130, 200)
    [163, 167]
    >>> gap_in_primes(2,100,110)
    [101, 10]

    :param g:(integer >= 2) which indicates the gap we are looking for
    :param m:(integer > 2) which gives the start of the search (m inclusive)
    :param n:(integer >= m) which gives the end of the search (n inclusive)
    :return:the first pair of two prime numbers spaced with a gap of g
    between the limits m, n if these numbers exist otherwise None.

    """
    primes = [num for num in range(m, n+1) if is_prime(num)]
    #print(primes)
    for prime_index in range(len(primes)):

        if prime_index + 1 <= primes.index(primes[-1]):
            cur_prime = primes[prime_index]
            next_prime = primes[prime_index + 1]
            if next_prime - cur_prime == gap:
                return [cur_prime, next_prime]

    #return None

    #find first prime between m and n:
    # start = m
    # while not is_prime(start):
    #     start += 1
    # end = start + 1 if start + 1 < n else n
    # prime_pair = None
    # while end < n:
    #     while not is_prime(end) and end < n:
    #         end += 1
    #     #if is_prime(start) and is_prime(end):
    #     if (end-start) == gap:
    #         prime_pair = [start, end]
    #         return prime_pair
    #     else:
    #         start = end
    #         end = start + 1
    # return prime_pair

if __name__ == '__main__':
    import doctest
    doctest.testmod()
