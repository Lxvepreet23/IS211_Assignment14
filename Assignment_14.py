# Assignment 14

# The Implement the Fibonnaci Sequence
def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2) # fib sequence

# The Euclid’s GCD Algorithm
def gcd2(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a

    return gcd2(b, a % b) # Greatest Common Denominator


# The String Comparison
def compareTo(s1, s2):
    if not (s1) == '' and not (s2) == '':
        if s1[0] < s2[0]:
            return -1
        if (s1)[0] == (s2)[0]:
            return 0
        return 1, compareTo(s1[1:], s2[1:]) # Comparison