def factorial(n : int) -> int:
    if n == 0:
        return 1
    
    if n < 0:
        return None
    
    return n * factorial(n-1)

def factorial_iterative(n):
    if n < 0:
        return None
    
    mult = 1
    for i in range(1, n + 1):
        mult *= i

    return mult

factorial(3) # expected return 6