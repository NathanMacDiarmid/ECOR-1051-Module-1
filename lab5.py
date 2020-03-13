# Exercise 4

def repeat(s: str, n: int) -> str:
    """
    Return s repeated n times; if n is negative, return the empty string.
    
    # I'm adding this as a condition as well:
    Also if n is zero, return the empty string.
    
    >>> repeat('yes', 4)
    
    'yesyesyesyes'
    
    >>> repeat('no', 0)
    
    ''
    
    >>> repeat('no', -2)
   
    ''
    
    >>> repeat('yesnomaybe', 3)
    
    'yesnomaybeyesnomaybeyesnomaybe'
    
    """
    if n > 0:
        return s * n
    else:
        return "''"

# Exercise 5

def total_length(s1: str, s2: str) -> int:
    """
    Return the sum of the lengths of s1 and s2
    
    >>> total_length('yes', 'no')
    
    5
    
    >>> total_length('yes', '')
    
    3
    
    >>> total_length('YES!!!!', 'Noooooo')
    
    14
    
    """
    return len(s1) + len(s2)

# Exercise 6

def replicate(s: str) -> str:
    """
    Returns the copy of the given string the amount of times of the number of characters there are in the string.
    
    >>> replicate('a')
    
    'a'
    
    >>> replicate('abc')
    
    'abcabcabc'
    
    >>> replicate('Hello World, ')
    
    Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, Hello World, 
    
    """
    return s * len(s)

# TESTS

# Exercise 4

print(repeat( 'hello world ', 5))
print(repeat( 'hello world ', 0))
print(repeat( 'hello world ', -5))

# Exercise 5

print(total_length('Yes', 'no'))
print(total_length('Yes', ''))
print(total_length('Yessssssssssssss', 'nonononononononononono'))

# Exercise 6

print(replicate('a'))
print(replicate('abc'))
print(replicate('Hello World, '))
