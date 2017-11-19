def anagrams_concise(word, words):
    """
    Finds all anagrams of word in list words

    :param word: word for which we are trying to find anagrams
    :param words: list through which we are sorting to see which words are anagrams of word
    :return: List of anagrams, or empty list if there are none

    >>> anagrams_concise('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
    ['aabb', 'bbaa']
    >>> anagrams_concise('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
    ['carer', 'racer']
    """
    return [item for item in words if is_anagram(word, item)]

# def anagrams(word, words):
#     """
#     Finds all anagrams of word in list words
#
#     :param word: word for which we are trying to find anagrams
#     :param words: list through which we are sorting to see which words are anagrams of word
#     :return: List of anagrams, or empty list if there are none
#
#     >>> anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
#     ['aabb', 'bbaa']
#     >>> anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
#     ['carer', 'racer']
#     """
#     anagram_lst = []
#     for item in words:
#         if is_anagram(word, item):
#             anagram_lst.append(item)
#     return anagram_lst

def is_anagram(word1, word2):
    """Determines whether two words are anagrams of one another"""

    word1_list, word2_list = list(word1), list(word2)
    word1_list.sort(); word2_list.sort()
    return word1_list == word2_list



if __name__ == "__main__":
    import doctest
    doctest.testmod()