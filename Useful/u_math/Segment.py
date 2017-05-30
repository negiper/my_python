class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

class Vector(object):
    def __init__(self, start_point, end_point):
        self.start, self.end = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y


ZERO = 1e-9

def negative(vector):
    return Vector(vector.end, vector.start)

def product(VA, VB):
    return VA.x*VB.y - VB.x*VA.y

def is_intersected(A, B, C, D):
    AC = Vector(A, C)
    AD = Vector(A, D)
    BC = Vector(B, C)
    BD = Vector(B, D)
    CA = negative(AC)
    CB = negative(BC)
    DA = negative(AD)
    DB = negative(BD)

    return (product(AC, AD) * product(BC, BD) <= ZERO) and \
            (product(CA, CB) * product(DA, DB) <= ZERO)

A = Point(1,0)
B = Point(0,2)
C = Point(1.5,1)
D = Point(2,2)
print is_intersected(A,B,C,D)
