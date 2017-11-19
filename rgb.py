def rgb(r, g, b):
    """
    >>> rgb(0,0,0)
    000000
    >>> rgb(1,2,3)
    010203
    >>> rgb(255,255,255)
    FFFFFF
    >>> rgb(254,253,252)
    FEFDFC
    >>> rgb(-20,275,125)
    00FF7D
    """
    if r < 0: r = 0
    if r > 255: r = 255
    if g < 0: g = 0
    if g > 255: g = 255
    if b < 0: b = 0
    if b > 255: b = 255

    red = [char.upper() for char in hex(r) if char != 'x']
    red_hex = '';
    for char in red: red_hex += char
    grn = [char.upper() for char in hex(g) if char != 'x']
    grn_hex = '';
    for char in grn: grn_hex += char
    blu = [char.upper() for char in hex(b) if char != 'x']
    blu_hex = '';
    for char in blu: blu_hex += char
    return (red_hex + grn_hex + blu_hex)




if __name__ == "__main__":
    import doctest
    doctest.testmod()