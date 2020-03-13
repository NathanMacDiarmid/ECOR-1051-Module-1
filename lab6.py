# Imports

import math

# FUNCTION DEFINITIONS

# Exercise 1 Definition

def factorial(n: int) -> int:
    """
    
    Return n! for postive values of n.
    
    >>> factorial(1)
    
    1
    
    >>> factorial(2)
    
    2
    
    >>> factorial(3)
    
    6
    
    >>> factorial(4)
    
    24
    
    """
    fact = 1
    for i in range(2, n+1):
        fact *= n
        
    return fact

actual1 = factorial(1)
actual2 = factorial(2)
actual3 = factorial(3)
actual4 = factorial(4)

# Exercise 2 Definition

TOTALLY_SATISFIED = 0.20
SOMEWHAT_SATISFIED = 0.15
DISSATISFIED = 0.05

def tip(meal: float, sat_lvl: int) -> float:
    """
    Returns the amount of tip the customer should give (before tax) based on the level of satisfaction with a rating of either 1, 2, or 3.
    1 being totally satisfied.
    2 being somewhat satisfied.
    3 being dissatisfied.
    
    >>> tip(15.79, 1)
    3.158
    
    >>> tip(16.44, 2)
    2.466
    
    >>> tip(14.35, 3)
    0.7175
    """
    if sat_lvl == 1:
        return abs(meal*TOTALLY_SATISFIED)
    elif sat_lvl == 2:
        return abs(meal*SOMEWHAT_SATISFIED)
    elif sat_lvl == 3:
        return abs(meal*DISSATISFIED)
    else:
        return meal

actual_tip1 = tip(15.00, 1)
actual_tip2 = tip(15.00, 2)
actual_tip3 = tip(15.00, 3)

# Exercise 3 Definition

def coupon(groceries: float) -> float:
    """
    Returns the amount of a coupon based on the amount spent on groceries in dollars.
    
    >>> coupon(8.99)
    NO COUPON
    
    >>> coupon(14.44)
    1.16
    
    >>>coupon(112.75)
    11.28
    
    >>>coupon(205.99)
    24.72
    
    >>> coupon(300.99)
    42.14
    """
    if groceries > 210:
        return groceries*0.14
    elif 150 < groceries <= 210:
        return groceries*0.12
    elif 60 < groceries <= 150:
        return groceries*0.10
    elif 10 <= groceries <= 60:
        return groceries*0.08
    else:
        return 0

actual_coupon1 = round(coupon(8.99), 2)
actual_coupon2 = round(coupon(14.44), 2)
actual_coupon3 = round(coupon(112.75), 2)
actual_coupon4 = round(coupon(205.99), 2)
actual_coupon5 = round(coupon(300.99), 2)

# Exercise 4 Definitions

def test_int(fn, expect: int, var: int) -> int:
    """
    Returns the incremented value of arg.
    Tests by comparing the returned value with the actual value and the exepcted value to make sure that the function is adding 1.
    Actual value is what actually comes out when subtracting the absolute value of arg and actual.
    Exepcted value is always 1.
    If the actual - arg != expect, the function fails and returns 0.
    
    >>> test_int(3, 1, 4)
    1
    
    >>> test_int(1, 1, 2)
    0
    
    >>> test_int(1, 1, 2)
    1
    """
    print("Testing", fn.__name__,":")
    actual = fn(var)
    print("Expected result:", expect, "Actual result:", actual)
    if  actual == expect:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0

# TESTING

# Exercise 1 Testing
passedtests += test_int()
print("TESTING EXERCISE 1 \n")

print("Testing factorial(1)")
print("Expected result: 1 Actual result:", actual1)
if actual1 == 1:
    print("Test passed")
else:
    print("Test failed")
    
print("Testing factorial(2)")
print("Expected result: 2 Actual result:", actual2)
if actual2 == 2:
    print("Test passed")
else:
    print("Test failed")
    
print("Testing factorial(3)")
print("Expected result: 6 Actual result:", actual3)
if actual3 == 6:
    print("Test passed")
else:
    print("Test failed")
    
print("Testing factorial(4)")
print("Expected result: 24 Actual result:", actual4)
if actual4 == 24:
    print("Test passed")
else:
    print("Test failed")

if actual1 == 1 and actual2 == 2 and actual3 == 6 and actual4 == 24:
    print("All 4 tests passed for Exercise 1")
elif actual1 == 1 and actual2 == 2 and actual3 == 6:
    print("3 tests passed for Exercise 1 \n1 test failed for Exercise 1")
elif actual1 == 1 and actual2 == 2:
    print("2 tests passed for Exercise 1 \n2 tests failed for Exercise 1")
elif actual1 == 1:
    print("1 test passed for Exercise 1 \n3 tests failed for Exercise 1")
else:
    print("All tests failed for Exercise 1")
print("\n")
    
# Exercise 2 Testing

print("TESTING EXERCISE 2 \n")

print("Testing tip(15.00, 1)")
print("Expected result: 3 Actual result:", actual_tip1)
if actual_tip1 == 3.0:
    print("Test passed")
else:
    print("Test failed")
    
print("Testing tip(15.00, 2)")
print("Expected result: 2.25 Actual result:", actual_tip2)
if actual_tip2 == 2.25:
    print("Test passed")
else:
    print("Test failed")

print("Testing tip(15.00, 3)")
print("Expected result: 1.5 Actual result:", actual_tip3)
if actual_tip3 == 0.75:
    print("Test passed")
else:
    print("Test failed")
    
if actual_tip1 == 3.0 and actual_tip2 == 2.25 and actual_tip3 == 0.75:
    print("All 3 tests passed for Exercise 2")
elif actual_tip1 == 3.0 and actual_tip2 == 2.25:
    print("2 tests passed for Exercise 2 \n1 test failed for Exercise 2")
elif actual_tip1 == 3.0:
    print("1 test passed for Exercise 2 \n2 tests failed for Exercise 2")
else:
    print("All tests failed for Exercise 2")
print("\n")
    
# Exercise 3 Testing

print("TESTING EXERCISE 3 \n")

print("Testing coupon(8.99)")
print("Expected result: 0 Actual result:", actual_coupon1)
if actual_coupon1 == 0:
    print("Test passed")
else:
    print("Test failed")
    
print("Testing coupon(14.44)")
print("Expected result: 1.16 Actual result:", actual_coupon2)
if actual_coupon2 == 1.16:
    print("Test passed")
else:
    print("Test failed")

print("Testing coupon(112.75)")
print("Expected result: 11.28 Actual result:", actual_coupon3)
if actual_coupon3 == 11.28:
    print("Test passed")
else:
    print("Test failed")
    
print("Testing coupon(205.99)")
print("Expected result: 24.72 Actual result:", actual_coupon4)
if actual_coupon4 == 24.72:
    print("Test passed")
else:
    print("Test failed")
    
print("Testing coupon(300.99)")
print("Expected result: 42.14 Actual result:", actual_coupon5)
if actual_coupon5 == 42.14:
    print("Test passed")
else:
    print("Test failed")
    
if actual_coupon1 == 0 and actual_coupon2 == 1.16 and actual_coupon3 == 11.28 and actual_coupon4 == 24.72 and actual_coupon5 == 42.14:
    print("All tests passed for Exercise 3")
    
elif actual_coupon1 == 0 and actual_coupon2 == 1.16 and actual_coupon3 == 11.28 and actual_coupon4 == 24.72:
    print("4 tests passed for Exercise 3 \n1 test failed for Exercise 3")
    
elif actual_coupon1 == 0 and actual_coupon2 == 1.16 and actual_coupon3 == 11.28:
    print("3 tests passed for Exercise 3 \n2 tests failed for Exercise 3")
    
elif actual_coupon1 == 0 and actual_coupon2 == 1.16:
    print("2 tests passed for Exercise 3 \n3 tests failed for Exercise 3")
    
elif actual_coupon1 == 0:
    print("1 test passed for Exercise 3 \n4 tests failed for Exercise 3")
    
else:
    print("All tests failed for Exercise 3")
print("\n")
    
# Exercise 4 Testing

print("TESTING EXERCISE 4 \n")

actual_test1 = test_int(factorial, 1, 1)
actual_test2 = test_int(factorial, 2, 2)
actual_test3 = test_int(factorial, 6, 3)
actual_test4 = test_int(factorial, 24, 4)

print(actual_test1)
print(actual_test2)
print(actual_test3)
print(actual_test4)