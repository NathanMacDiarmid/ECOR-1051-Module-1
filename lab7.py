# CONSTANTS

WEEKDAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKEND = ["Saturday", "Sunday"]
SUMMER = ["June", "July", "August"]
MIN_PASTRIES = 40
MAX_PASTRIES = 60
MIN_TEMP = 60
MAX_TEMPS = 100
MAX_TEMP = 90
GREAT_42 = 42
BLACKJACK = 21


def test_fn(fn, expect: bool, var1, var2) -> bool:

    print("Testing", fn.__name__, ":")
    actual = fn(var1, var2)
    print("Expected result:", expect, "Actual result:", actual)
    if actual == expect:
        return "\n Test passed \n"
    else:
        return "\n Test failed \n"


def test_fn2(fn, expect: bool, var1, var2, var3) -> bool:

    print("Testing", fn.__name__, ":")
    actual = fn(var1, var2, var3)
    print("Expected result:", expect, "Actual result:", actual)
    if actual == expect:
        return "\n Test passed \n"
    else:
        return "\n Test failed \n"

# FUNCTION DEFINITIONS

# Exercise 1 Definition


def bakers_party(pastries: int, day_of_week: str) -> bool:
    """
    Takes the number of pastries (pastries > 40 for weekends and 40 <= pasteries <= 60 for weekdays) to see if was a successful party.
    Returns True or Fasle based on inputs.
    """
    if day_of_week in WEEKDAY and MIN_PASTRIES <= pastries <= MAX_PASTRIES:
        return True
    elif day_of_week in WEEKDAY and pastries < MIN_PASTRIES:
        return False
    elif day_of_week in WEEKDAY and pastries > MAX_PASTRIES:
        return False
    elif day_of_week in WEEKEND and pastries >= MIN_PASTRIES:
        return True
    elif day_of_week in WEEKEND and pastries < MIN_PASTRIES:
        return False

# Exercise 2 Definition


def squirrel_play(temp: int, month: str) -> bool:
    """
    "Returns whether or not the squirrels are playing because I enjoy  playing with squirrels very, very , very much.... hehe ;p
    """
    if month in SUMMER and MIN_TEMP <= temp <= MAX_TEMPS:
        return True
    elif month in SUMMER and temp < MIN_TEMP:
        return False
    elif month in SUMMER and temp > MAX_TEMPS:
        return False
    elif month not in SUMMER and MIN_TEMP <= temp <= MAX_TEMP:
        return True
    elif month not in SUMMER and temp < MIN_TEMP:
        return False
    elif month not in SUMMER and temp > MAX_TEMP:
        return False

# Exercise 3 Definition


def great_42(a: int, b: int) -> bool:
    """
    Returns True if either a, b or the additions or subtraction of a and b is 42.
    Returns False if not.
    """
    if a == GREAT_42:
        return True
    elif b == GREAT_42:
        return True
    elif abs(a + b) == GREAT_42:
        return True
    elif abs(a - b) == GREAT_42:
        return True
    else:
        return False

# Exercise 4 Definition


def blackjack(a: int, b: int) -> int:
    """
    Returns whicher value is closer to 21 without going over 21.
    Returns 0 if both are over 21.
    """
    if BLACKJACK >= a > b:
        return a
    elif BLACKJACK >= b > a:
        return b
    elif a == b:
        return "TIE"
    else:
        return 0

# Exercise 5 Definition


def sum_uniques(a: int, b: int, c: int) -> int:
    """
    Returns the sum of all three variables, unless two variables are the same, then it returns the variable that is different.
    """
    if a == b:
        return c
    elif c == a:
        return b
    elif b == c:
        return a
    else:
        return a + b + c

# TESTING

# Exercise 1 Testing


print("\nEXERCISE 1: \n")

print(test_fn(bakers_party, True, 40, "Wednesday"))
print(test_fn(bakers_party, False, 61, "Monday"))
print(test_fn(bakers_party, False, 39, "Thursday"))
print(test_fn(bakers_party, True, 40, "Saturday"))
print(test_fn(bakers_party, False, 39, "Saturday"))
print(test_fn(bakers_party, True, 149, "Sunday"))

# Exercise 2 Testing

print("EXERCISE 2: \n")

print(test_fn(squirrel_play, True, 60, "June"))
print(test_fn(squirrel_play, True, 100, "July"))
print(test_fn(squirrel_play, True, 75, "August"))
print(test_fn(squirrel_play, True, 60, "June"))
print(test_fn(squirrel_play, False, 59, "June"))
print(test_fn(squirrel_play, True, 90, "December"))
print(test_fn(squirrel_play, False, 100, "November"))
print(test_fn(squirrel_play, False, 59, "September"))

# Exercise 3 Testing

print("EXERCISE 3: \n")

print(test_fn(great_42, True, 42, 5))
print(test_fn(great_42, True, -7, 42))
print(test_fn(great_42, True, 65, 23))
print(test_fn(great_42, True, 35, 7))
print(test_fn(great_42, True, -55, -13))
print(test_fn(great_42, False, 3, 5))
print(test_fn(great_42, False, -43, 43))
print(test_fn(great_42, True, -42, 42))

# Exercise 4 Testing

print("EXERCISE 4: \n")

print(test_fn(blackjack, "TIE", 21, 21))
print(test_fn(blackjack, "TIE", 18, 18))
print(test_fn(blackjack, 21, 21, 18))
print(test_fn(blackjack, 21, 18, 21))
print(test_fn(blackjack, 19, 19, 13))

# Exerceise 5 Testing

print("EXERCISE 5: \n")

print(test_fn2(sum_uniques, 6, 1, 2, 3))
print(test_fn2(sum_uniques, 2, 3, 2, 3))
print(test_fn2(sum_uniques, 3, 1, 1, 3))
print(test_fn2(sum_uniques, 1, 1, 2, 2))
