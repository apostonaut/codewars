def make_time_readable(seconds):

    """
    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
    human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

    >>> make_time_readable(359999)
    '99:59:59'
    >>> make_time_readable(0)
    '00:00:00'

    :param seconds:
    :return:
    """
    #count the number of times 60*60 = 3600 seconds fits into input
    hrs = str(int(seconds/3600)) if int(seconds/3600) >= 10 else '0' + str(int(seconds/3600))
    mins = str(int(seconds%3600/60)) if int(seconds%3600/60) >= 10 else '0' + str(int(seconds%3600/60))
    secs = str(int(seconds%60)) if int(seconds%60) >= 10 else '0' + str(int(seconds%60))

    return '{}:{}:{}'.format(hrs, mins, secs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
