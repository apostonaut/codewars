# from this exercise, I learned that brute-force algorithms are rarely very efficient. It is more
# efficient to think about the properties of the element you are looking for, and try indexing a
# sequence instead of producing all possible sequences

import itertools
def middle_permutation(string):
    """
    You are given a string s. Every letter in s appears once.

    Consider all strings formed by rearranging the letters in s. After ordering these
    strings in dictionary order, return the middle term. (If the sequence has a even
    length n, define its middle term to be the (n/2)th term.)

    :param string:
    :return:

    >>> middle_permutation("abc")
    'bac'
    >>> middle_permutation("abcd")
    "bdca"
    >>> middle_permutation("abcdx")
    "cbxda"
    >>> middle_permutation("abcdxgz")
    "dczxgba"
    """
    def lst_to_str(list):
        """
        Converts a list of characters to a string
        """
        str = ''
        for char in list:
            str += char
        return str
    lst = list(string)
    # create all possible permutations of string
    permutations = itertools.permutations(lst)
    # convert each permutation list to a string
    permutations = [''.join(e for e in perm) for perm in permutations]
    #permutations.sort()
    # get middle term
    middle = int(len(permutations)/2) - 1
    return permutations[middle]



def create_permutations(lst):
    """
    Returns all permutations of input lst.
    """
    # base case
    if len(lst) == 1:
        return [lst]
    perms = []
    for char in lst:
        lst_copy = lst.copy()
        lst_copy.remove(char)
        permutation = [[char] + item for item in create_permutations(lst_copy)]
        perms += permutation
    return perms

def mid_permutation(string):
    s = "".join(sorted(string))
    mid = int(len(s) / 2) - 1
    if len(s) % 2 == 0:
        return s[mid] + (s[:mid] + s[mid + 1:])[::-1]
    else:
        return s[mid:mid + 2][::-1] + (s[:mid] + s[mid + 2:])[::-1]
if __name__ == "__main__":
    import doctest
    doctest.testmod()