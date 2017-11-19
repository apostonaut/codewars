def palindrome_chain_length(n):
    """
    >>> palindrome_chain_length(87)
    4
    """
    num_steps = 0
    while not is_palindrome(n):
        #reverse the digits, and add to the original number
        n += int(str(n)[::-1])
        num_steps += 1

    return num_steps

def is_palindrome(number):
    """Returns whether number is a palindrome"""
    return str(number)[::-1] == str(number)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

