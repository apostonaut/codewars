def scramble(s1,s2):
    """
    Returns true if a portion of str1 characters can be rearranged
    to match str2, otherwise returns false.

    >>> scramble('rkqodlw','world')
    True
    >>> scramble('cedewaraaossoqqyt','codewars')
    True

    :param s1:
    :param s2:
    :return:
    """

    str2_aslst = [char for char in s2]
    for i in range(len(s1)):
        if s1[i] in str2_aslst:
            str2_aslst.remove(s1[i])
            if len(str2_aslst) == 0:
                break
    return len(str2_aslst) == 0


    # str1_aslst = [char for char in s1]
    # str1_aslst.sort()
    # str1_aslst.reverse()
    # str2_aslst = [char for char in s2]
    # str2_aslst.sort()
    # #print('str1', str1_aslst )
    # #print('str2', str2_aslst)
    #
    # #check to see that all characters of s2 are in s1. remove char from str1_aslst
    # for char in str2_aslst:
    #     if char in str1_aslst:
    #         str1_aslst.remove(char)
    #     else:
    #         return False
    # return True

# SOLUTION FROM CODEWARS
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
