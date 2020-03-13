z = {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

def sum_x(st: set) -> float:
    """
    Takes a set of "n" tuples that consist of two floating point numbers. They are the x and y coordinates respectively.
    Returns the sum of all the x coordinates.
    
    >>> {(1.0, 1.0), (2.0, 2.0)}
    3.0
    
    >>> {(1.7, 1.0), (2.3, 2.0), (44.3, 5.3), (-15, -37)}
    33.3
    """
    total = 0
    lst1 = list(st)
    for i in range(len(st)):
        lst2 = list(lst1[i])
        total += lst2[0]
    return total

def sum_y(st: set) -> float:
    """
    Takes a set of "n" tuples that consist of two floating point numbers. They are the x and y coordinates respectively.
    Returns the sum of all the x coordinates.
    
    >>> {(1.0, 1.0), (2.0, 2.0)}
    3.0
    
    >>> {(1.7, 1.0), (2.3, 2.0), (44.3, 5.3), (-15, -37)}
    33.3
    """
    total = 0
    lst1 = list(st)
    for i in range(len(st)):
        lst2 = list(lst1[i])
        total += lst2[1]
    return total

def sum_xx(st: set) -> float:
    """
    Takes a set of "n" tuples that consist of two floating point numbers. They are the x and y coordinates respectively.
    Returns the sum of all the x coordinates.
    
    >>> {(1.0, 1.0), (2.0, 2.0)}
    3.0
    
    >>> {(1.7, 1.0), (2.3, 2.0), (44.3, 5.3), (-15, -37)}
    33.3
    """
    total = 0
    lst1 = list(st)
    for i in range(len(st)):
        lst2 = list(lst1[i])
        total += lst2[0] ** 2
    return total

def sum_xy(st: set) -> float:
    """
    Takes a set of "n" tuples that consist of two floating point numbers. They are the x and y coordinates respectively.
    Returns the sum of all the x coordinates.
    
    >>> {(1.0, 1.0), (2.0, 2.0)}
    3.0
    
    >>> {(1.7, 1.0), (2.3, 2.0), (44.3, 5.3), (-15, -37)}
    33.3
    """
    total = 0
    lst1 = list(st)
    for i in range(len(st)):
        lst2 = list(lst1[i])
        total += lst2[1] * lst2[0]
    return total

print(sum_x(z))
print(sum_y(z))

print(sum_xx(z))
print(sum_xy(z))

sumx = sum_x(z)
sumy = sum_y(z)
sumxx = sum_xx(z)
sumxy = sum_xy(z)

m = (sumx * sumy - 3 * sumxy) / (sumx * sumx - 3 * sumxx)
b = (sumx * sumxy - sumxx * sumy ) / (sumx * sumx - 3 * sumxx)

print("y =", m, "x +", b)