import string

def compare(s1,s2):
    """
    Compare two strings by comparing the sum of their values (ASCII character code).
    For comparing treat all letters as UpperCase. Null-Strings should be treated as if
    they are empty strings.If the string contains other characters than letters, treat
    the whole string as it would be empty.

    >>> compare('zz1', '')
    True
    """
    if s1 is not None:
        for i in s1:
            if i not in (string.ascii_uppercase + string.ascii_lowercase):
                s1 = ""
                break
    if s2 is not None:
        for j in s2:
            if j not in (string.ascii_uppercase + string.ascii_lowercase):
                s2 = ""
                break
    s1_sum, s2_sum = 0, 0

    if s1 is not None:
        s1= s1.upper()
        for i in s1:
            s1_sum += ord(i)
    if s2 is not None:
        s2 = s2.upper()
        for j in s2:
            s2_sum += ord(j)
    return s1_sum == s2_sum

def compare_improved(s1,s2):
    """
    >>> compare('zz1', '')
    True
    """
    if not s1.isalpha():
        s1 = ""
    if not s2.isalpha():
        s2 = ""
    s1_sum, s2_sum = 0, 0
    s1= s1.upper()
    for i in s1:
        s1_sum += ord(i)
    s2 = s2.upper()
    for j in s2:
        s2_sum += ord(j)
    return s1_sum == s2_sum

print('test', compare('zz1', ''))

if __name__ == '__main__':
    import doctest
    doctest.testmod()