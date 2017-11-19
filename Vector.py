import math

class Vector:
    """
    Create a Vector object that supports addition, subtraction, dot products, and norms.
    """

    def __init__(self, contents):
        """
        :param contents: a list of integers
        """
        self.contents = contents

    def add(self, other):
        """
        Adds Vector other to Vector self in an element-wise manner
        :param other: a Vector object
        :return: the sum of the two Vector objects
        :rtype: Vector
        """
        assert len(self.contents) == len(other.contents), "The two vectors are not of equal length"
        vector = [0 for item in range(len(self.contents))]
        for i in range(len(self.contents)):
            vector[i] = self.contents[i] + other.contents[i]
        return Vector(vector)

    def subtract(self, other):
        """
        Subtracts Vector other from Vector self in an element-wise manner
        :param other: a Vector
        :return: the difference between the two Vector objects
        :rtype: Vector
        """
        assert len(self.contents) == len(other.contents), "The two vectors are not of equal length"
        vector = [0 for item in range(len(self.contents))]
        for i in range(len(self.contents)):
            vector[i] = self.contents[i] - other.contents[i]
        return Vector(vector)

    def dot(self, other):
        """
        Takes the dot product of Vector self and Vector other
        :param other: a Vector
        :return: the dot product of the two Vector objects
        :rtype: int
        """

        assert len(self.contents) == len(other.contents), "The two vectors are not of equal length"
        dot_product = 0
        for i in range(len(self.contents)):
            dot_product += self.contents[i] * other.contents[i]
        return dot_product

    def norm(self):
        """
        Returns the Euclidian norm of the vector

        :return: the norm
        """
        norm = 0
        for i in range(len(self.contents)):
            norm += self.contents[i]**2
        norm = math.sqrt(norm)

        return norm

    def __str__(self):
        """
        :return: a string representation of Vector self
        """
        string = str(tuple(self.contents)).replace(' ', '')
        return string
        
        # output = ''
        # for char in string:
        #     if char != ' ':
        #         output += char
        # return output

    def equals(self, other):
        """
        Returns wether two Vector objects are equal
        :return: boolean
        """
        if len(self.contents) != len(other.contents):
            return False
        for i in range(len(self.contents)):
            if self.contents[i] != other.contents[i]:
                return False
        return True



"""
a toString function, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this
is a __str__ method, so that str(a) == '(1,2,3)')

an equals function, so that two vectors who have the same components are equal
"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    c = Vector([5, 6, 7, 8])
    #print(a.add(b).contents)  # should return Vector([4,6,8])
    #print(a.subtract(b).contents)  # should return Vector([-2,-2,-2])
    #print(a.dot(b))  # should return 1*3+2*4+3*5 = 26
    #print(a.norm() ) # should return sqrt(1^2+2^2+3^2)=sqrt(14)
    #a.add(c)  # raises an exception
    print(str(a))
