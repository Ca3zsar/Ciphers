"""
A module that will encapsulate some math functions that will be used
in different ciphers.
"""

# Euclid's Algorithm for Greatest Common Divisor.
def GCD(a,b):
    """
    Takes in two arguments: a and b and returns their greatest common divisor
    """
    while b != 0:
        a, b = b, a % b
    return a

# Euclid's Extended Algorithm used for modular inverse.
def mInverse(a,n):
    """
    Takes in two arguments: a and n and returns a^(-1) modulo n
    For a number a to have modular inverse, it has to be coprime with n.
    a*x + n*y = 1 mod n, so we are interested in determining x.
    """
    x, newX = 0, 1
    y, newY = 1, 0
    r, newR = n, a
    
    while newR != 0:
        quotient = r // newR
        r, newR = newR, r % newR
        x, newX = newX, x - quotient * newX
        y, newY = newY, y - quotient * newY
      
    if r > 1:
        return None  
        
    if x < 0:
        x += n
    
    return x
    
