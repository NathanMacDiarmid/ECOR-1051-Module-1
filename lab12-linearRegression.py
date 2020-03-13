# IMPORTS

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

# ECOR 1051 Lab 12 File: lab12-linearRegression.py

from typing import Set, Tuple
# See Practical Programming, Chapter 8, section Type Annotations For Lists,
# and Chapter 11, first paragraph of section Creating New Type Annotations. 

# DEFINITIONS

# PART 1 DEFINITION

def get_points() -> Set[Tuple[float, float]]:
    """Return a set of (x, y) points.
    
    >>> get_points()
    {(1.0, 5.0), (3.5, 12.5), (2.0, 8.0)}
    # The order of the points may vary, depending on how sets are implemented
    # in the version of Python you're using.
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

def fit_line_to_points(points: Set[Tuple[float, float]]) -> Tuple[float, float]:
    """
    Returns a tuple with the y-intercept and the slope, best fitting all the x, y coordinates in the set provided.
    
    >>> {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}
    (3.0, 2.0)
    """
    n = len(points)
    
    sumx = sum_x(points)
    sumy = sum_y(points)
    sumxx = sum_xx(points)
    sumxy = sum_xy(points)
    
    m = (sumx * sumy - n * sumxy) / (sumx * sumx - n * sumxx)
    b = (sumx * sumxy - sumxx * sumy ) / (sumx * sumx - n * sumxx)
    
    return (m, b)

# Part 2 DEFINITIONS

def read_and_print_lines() -> None:
    infile = open('lab12-data.txt', 'r')
    for line in infile:
        print(line)
    infile.close()
    
# Exercise 7 Definition

def read_points(filename: str) -> Set[Tuple[float, float]]:
    """
    Returns a set of tuples from a file, with the first value in each tuple being an x value and the second being a y value.
    """
    infile = open(filename)
    lst1 = []
    for line in infile:
        x = float(line.split()[0])
        y = float(line.split()[1])
        z = (x, y)
        lst1.append(z)
    infile.close()
    return set(lst1)
    
# TESTING

# PART 1 Testing
print("\n")
print("The best-fit line is y =", (fit_line_to_points(get_points()))[0], "x +", (fit_line_to_points(get_points()))[1])
print("\n")
# PART 2 Testing

print(read_points('lab12-data.txt'))
print("\n")
# Excercise 8 Script

print(fit_line_to_points(read_points(input("Please enter a filename:"))))