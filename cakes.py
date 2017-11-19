import math

def cakes(recipe, available):
    """

    :param recipe:
    :param available:
    :return:
    # must return 2
    >>> cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
    2
    >>> cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})
    0
    """
    recipe_ings= recipe.keys()
    available_ings = available.keys()
    numcakes_lst = []
    for item in recipe_ings:
        if item not in available_ings:
            return 0
    for item in recipe_ings:
        numcakes = available[item]/recipe[item]
        numcakes_lst.append(numcakes)
    return math.floor(min(numcakes_lst))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
