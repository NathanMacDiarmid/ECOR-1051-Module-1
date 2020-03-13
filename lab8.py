# IMPORTS


def test_fn(fn, expect: bool, var1) -> bool:

    print("Testing", fn.__name__, ":")
    actual = fn(var1)
    print("Expected result:", expect, "Actual result:", actual)
    if actual == expect:
        return "\n Test passed \n"
    else:
        return "\n Test failed \n"


def test_fn2(fn, expect: bool, var1, var2) -> bool:

    print("Testing", fn.__name__, ":")
    actual = fn(var1, var2)
    print("Expected result:", expect, "Actual result:", actual)
    if actual == expect:
        return "\n Test passed \n"
    else:
        return "\n Test failed \n"

# FUNCTION DEFINITIONS

# Exercise 1 Definition


def first_last6(lst1: list) -> bool:
    """
    Returns True if the first and/or last element in the list is 6
    """
    if lst1[0] == 6:
        return True
    elif lst1[-1] == 6:
        return True
    elif lst1[0] == 6 and lst1[-1] == 6:
        return True
    else:
        return False

# Exercise 2 Definition


def same_first_last(lst2):
    """
    Returns True if the list isn't empty and if the first and last elements are equal.
    Otherwise it returns False.
    """
    if len(lst2) == 0:
        return False
    elif len(lst2) > 0 and lst2[0] == lst2[-1]:
        return True

# Exercise 3 Definition


def make_pi():
    """
    Returns a list of length that contains the first three digits of pi.
    """
    return [3, 1, 4]

# Exercise 4 Definition


def common_end(lst3, lst4):
    """
    Returns True if both fist elements are the same.
    Returns True if the first and last elements of both lists are the same.
    Returns False otherwise.
    """
    if len(lst3) == 0:
        return False
    elif len(lst4) == 0:
        return False
    elif lst3[0] == lst4[0]:
        return True
    elif lst3[-1] == lst4[-1]:
        return True
    else:
        return False

# Exercise 5 Definition


def sum3(lst5):
    """
    Returns the sum of all three elements in provided list.
    """
    return lst5[0] + lst5[1] + lst5[2]

# Exercise 6 Definition


def rotate_left3(lst6):
    """
    Returns the list given, rotated to the left by one.
    
    >>> [1, 2, 3]
    [2, 3, 1]
    """
    return [lst6[1], lst6[2], lst6[0]]

# Exercise 7 Definition


def reverse3(lst7):
    """
    Returns the given list, reversed.
    
    >>> [1, 2, 3]
    [3, 2, 1]
    """
    return [lst7[2], lst7[1], lst7[0]]

# Exercise 8 Definitino


def max_end3(lst8):
    """
    Returns a list of three of the same variable for whichever is bigger, first or last element.
    
    >>> [4, 5, 3]
    [4, 4, 4]
    """
    if lst8[0] > lst8[-1]:
        return [lst8[0], lst8[0], lst8[0]]
    elif lst8[0] == lst8[-1]:
        return [lst8[0], lst8[0], lst8[0]]
    else:
        return [lst8[-1], lst8[-1], lst8[-1]]

# Exercise 9 Definition


def sum2(lst9):
    """
    Returns the sum of the first two list elements.
    """
    if len(lst9) == 0:
        return 0
    elif len(lst9) == 1:
        return lst9[0]
    else:
        return lst9[0] + lst9[1]

# Exercise 10 Definition


def middle_way(lst10, lst11):
    """
    Returns the middle elements of two three integeger functions.
    """
    return [lst10[1], lst11[1]]

# Exercise 11 Definition


def make_ends(lst12):
    """
    Returns first and last element of a list in a new list
    """
    return [lst12[0], lst12[-1]]

# Exercise 12 Definition


def has23(lst13):
    """
    Returns True if the list contains 2 and/or 3.
    Returns False if not.
    """
    if int(2) or int(3) in lst13:
        return True
    else:
        return False

# TESTING

# Exercise 1 Testing


print("EXERCISE 1\n")

print(test_fn(first_last6, True, [1, 2, 3, 4, 5, 6]))
print(test_fn(first_last6, True, [6, 2, 3, 4, 5, 1]))
print(test_fn(first_last6, True, [6, 2, 3, 4, 5, 6]))
print(test_fn(first_last6, False, [1, 2, 3, 6, 5, 1]))
print(test_fn(first_last6, False, [1, 2, 3, 4, 5, 1]))

# Exercise 2 Testing

print("EXERCISE 2\n")

print(test_fn(same_first_last, False, []))
print(test_fn(same_first_last, True, [1, 2, 3, 4, 5, 1]))
print(test_fn(same_first_last, True, [1]))

# Exercise 3 Testing

print("EXERCISE 3\n")

print(make_pi())

# Exercise 4 Testing

print("EXERCISE 4\n")

print(test_fn2(common_end, True, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]))
print(test_fn2(common_end, True, [2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))
print(test_fn2(common_end, True, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6]))
print(test_fn2(common_end, False, [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]))
print(test_fn2(common_end, False, [1, 2, 3, 4, 5, 6], []))
print(test_fn2(common_end, False, [], []))

# Exercise 5 Testing

print("EXERCISE 5\n")

print(test_fn(sum3, 6, [1, 2, 3]))
print(test_fn(sum3, 0, [-1, -2, 3]))
print(test_fn(sum3, 0, [0, 0, 0]))

# Exercise 6 Testing

print("EXERCISE 6\n")

print(test_fn(rotate_left3, [2, 3, 1], [1, 2, 3]))
print(test_fn(rotate_left3, [5, 7, -1], [-1, 5, 7]))

# Exercise 7 Testing

print("EXERCISE 7\n")

print(test_fn(reverse3, [3, 2, 1], [1, 2, 3]))
print(test_fn(reverse3, [-3, -2, -1], [-1, -2, -3]))
print(test_fn(reverse3, [22, 5, 7], [7, 5, 22]))

# Exercise 8 Testing

print("EXERCISE 8\n")

print(test_fn(max_end3, [3, 3, 3], [1, 2, 3]))
print(test_fn(max_end3, [3, 3, 3], [2, 9, 3]))
print(test_fn(max_end3, [5, 5, 5], [5, 2, 3]))
print(test_fn(max_end3, [1, 1, 1], [1, 2, -3]))
print(test_fn(max_end3, [1, 1, 1], [1, 2, 1]))

# Exercise 9 Testing

print("EXERCISE 9\n")

print(test_fn(sum2, 0, []))
print(test_fn(sum2, 0, [1]))
print(test_fn(sum2, 3, [1, 2]))
print(test_fn(sum2, -1, [1, -2]))
print(test_fn(sum2, 15, [10, 5, 6, 9]))

# Exercise 10 Testing

print("EXERCISE 10\n")

print(test_fn2(middle_way, [2, 2], [1, 2, 3], [1, 2, 3]))
print(test_fn2(middle_way, [5, 2], [-1, 5, 3], [1, 2, 3]))
print(test_fn2(middle_way, [22, -2], [1, 22, 3], [1, -2, 3]))

# Exercise 11 Testing

print("EXERCISE 11\n")

print(test_fn(make_ends, [5, 7], [5, 2, 3, 4, 5, 7]))
print(test_fn(make_ends, [7, 7], [7, 2, 3, 4, 5, 7]))
print(test_fn(make_ends, [-22, 543], [-22, 2, 3, 4, 5, 543]))

# Exercise 12 Testing

print("EXERCISE 12 \n")

print(test_fn(has23, True, [5, 6, 4, 7, 3, 1]))
print(test_fn(has23, True, [5, 6, 2, 7, 3, 1]))
print(test_fn(has23, False, [5, 6, 4, 7, 0, 1]))
