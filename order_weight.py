def order_weight(st):
    """
    >>> order_weight("56 65 74 100 99 68 86 180 90")
    "100 180 90 56 65 74 68 86 99"

    :param strng:
    :return:
    """
    weight_list = st.split(" ")
    weight_digits = []

    #create list of tuples of (weight, sum of weight digits)
    for weight in weight_list:
        weight_sum = sum([int(num) for num in weight])
        weight_digits.append((weight_sum, weight))
    print(weight_digits)
    weight_digits.sort()
    print(weight_digits)
    sorted_string = ""
    for item in weight_digits:
        weight = str(item[1])
        sorted_string = sorted_string + weight + ' '
    sorted_string = sorted_string.rstrip()
    print(sorted_string)

if __name__ == '__main__':
    import doctest
    doctest.testmod()