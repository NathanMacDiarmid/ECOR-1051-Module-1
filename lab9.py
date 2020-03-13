# IMPORTS


def test_fn(fn, expect: bool, var1) -> bool:

    print("Testing", fn.__name__, ":")
    actual = fn(var1)
    print("Expected result:", expect, "Actual result:", actual)
    if actual == expect:
        return "\n Test passed \n"
    else:
        return "\n Test failed \n"

# FUNCTION DEFINITIONS

# Exercise 1 Definition


def count_evens(lst1):
    """
    Returns the number of even integers in the inputed list
    """
    count = 0
    for num in lst1:
        if len(lst1) == 0:
            return 0
        elif (num % 2) == 0:
            count += 1
    return count

# Exercise 2 Definition


def big_diff(lst2):
    """
    Assuming the list has at least two integers, it returns the difference between the largest and smallest integer.
    """
    i = lst2[0]
    j = lst2[0]
    for num1 in lst2:
        if num1 < i:
            i = num1
    for num2 in lst2:
        if num2 > j:
            j = num2
    return j - i

# Exercise 3 Definition


def has22(lst3):
    """
    Return True if there are two 2's next to each other.
    If not, it returns False.
    
    >>> [1, 2, 2, 3]
    True
    
    >>> [2, 1, 2, 3]
    False
    """
    count = 0
    for num in lst3:
        if num == 2:
            count += 1
            if count == 2:
                return True
        else:
            count = 0
    else:
        return False

# Exercise 4 Definition


def centered_average(lst4):
    """
    Returns the average of the integers inside the list with exception to the largest and smallest inputs ONE TIME.
    (Assuming that the list has 3 variables)
    
    >>> [1, 2, 3]
    2
    >>> [1, 2, 3, 4, 5, 6, 7]
    4
    """
    return (sum(lst4) - min(lst4) - max(lst4)) / ((len(lst4)) - 2)

# TESTING

# Exercise 1 Testing


print("EXERCISE 1\n")

print(test_fn(count_evens, 3, [1, 2, 3, 4, 5, 6]))
print(test_fn(count_evens, 2, [1, 2, 3, 5, 6]))
print(test_fn(count_evens, 3, [0, 2, 3, 5, 6]))
print(test_fn(count_evens, 6, [0, 0, 0, 0, 0, 0]))
print(test_fn(count_evens, 0, []))

# Exercise 2 Testing

print("EXERCISE 2\n")

print(test_fn(big_diff, 5, [1, 2, 3, 4, 5, 6]))
print(test_fn(big_diff, 86, [1, 2, -43, 4, 5, 43]))
print(test_fn(big_diff, 6, [1, 0, 3, 4, 5, 6]))

# Exercise 3 Testing

print("EXERCISE 3\n")

print(test_fn(has22, True, [1, 3, 2, 3, 4, 2, 2, 5, 6]))
print(test_fn(has22, False, [1, 3, 2, 3, 4, 2, 5, 6]))
print(test_fn(has22, False, []))

# Exercise 4 Testing

print("EXERCISE 4\n")

print(test_fn(centered_average, 3.5, [1, 2, 3, 4, 5, 6]))
print(test_fn(centered_average, 3.75, [5, 1, 3, 1, 7, 6]))
print(test_fn(centered_average, 6.4, [0, 2, 3, -1, 5, 22, 45]))
