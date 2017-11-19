#incomplete, forfeited solution

def is_merge(s, part1, part2):
    """
    Checks to see whether string s can be formed if part1 and part2 are merged.
    The restriction is that the characters in part1 and part2 are in the same order as in s.

    :return: boolean

    >>> is_merge('codewars', 'cdw', 'oears')
    True
    >>> is_merge('codewars', '', 'codewars')
    True
    >>> is_merge('bananas', 'aaa', 'bnns')
    True
    >>> is_merge("ab", "b", "a")
    True
    """
    #ensurse a merge is possible at all
    if len(s) != len(part1 + part2):
        return False

    s_list = list(s)
    merge_list = ['0' for i in range(len(s_list))]

    def assign_to_mergelist(part, merge_list, s_list):
        """Iterate through part, assign characters to merge_list
        """
        # ensures part is not an empty string
        if len(part) == 0:
            return merge_list
        part_index = 0
        i = 0
        for char in s_list:
            if part[part_index] == char and merge_list[i] == '0':
                merge_list[i] = part[part_index]
                part_index += 1
                if part_index >= len(part):
                    break
            i += 1
        return merge_list

    merge_list = assign_to_mergelist(part1, merge_list, s_list)
    merge_list = assign_to_mergelist(part2, merge_list, s_list)

    return (merge_list == s_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
