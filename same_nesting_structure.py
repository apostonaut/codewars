def same_structure_as(original,other):
    """
    Determines whether an array has the same nesting structure as another array.

    :param original: The first array
    :param other: The second array
    :return: Whether the two arrays have the same nesting structure
    :rtype: boolean
    >>> same_structure_as([1,[1,1]],[2,[2,2]])
    True
    >>> same_structure_as([1,[1,1]],[[2,2],2])
    False
    """
    if type(original) != list or type(other) != list:
        return False
    # creates copy of input arrays in case they are not allowed to be mutated
    original_copy = original.copy()
    other_copy = other.copy()

    def all_zeros(lst):
        """
        Makes all items in array and subarrays 0
        :param lst:
        :return:
        """
        i = 0
        for item in lst:
            if type(item) != list:
                lst[i] = 0
                i += 1
            elif type(item) == list:
                all_zeros(item)
                i += 1
        return lst
    return all_zeros(original_copy) == all_zeros(other_copy)




if __name__ == '__main__':
    import doctest
    doctest.testmod()