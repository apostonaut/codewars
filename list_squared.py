import math

def list_squared(m, n):
    """Given two integers m, n (1 <= m <= n) we want to find all integers
    between m and n whose sum of squared divisors is itself a square.

    >>> list_squared(1, 250)
    [[1, 1], [42, 2500], [246, 84100]]
    >>> list_squared(42, 250)
    [[42, 2500], [246, 84100]]
    """
    squares = []
    for num in range(m, n+1):
        #find all divisors of the number
        sum = 0
        for divisor in range(1, num + 1):
            if num % divisor == 0:
                sum += divisor**2
        # take square root of sum
        sqrt_sum = sum **0.5
        # append to squares if it is an integer
        if sqrt_sum/int(sqrt_sum) == 1:
            squares.append([num, sum])
    return squares


def list_squared_efficient(m, n):
    """

    >>> list_squared_efficient(1, 250)
    [[1, 1], [42, 2500], [246, 84100]]
    >>> list_squared_efficient(42, 250)
    [[42, 2500], [246, 84100]]
    """
    list=[]
    for num in range(m,n+1):
        sum=0
        for divisor in range(1,int(num**.5)+1):
            if num%divisor==0:
                div=num//divisor
                sum+=divisor**2
                if divisor!=div:
                    sum+=div**2
        sqt=sum**.5
        if int(sqt)==sqt:
            list.append([num,sum])
    return list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
