"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes < 1):
        raise ValueError(f"{number_of_primes} should be a number bigger than zero!")
    list = [2]
    i=3
    while number_of_primes-len(list) > 0:
        j=2
        count=True
        while j * j <= i:
            if(i%j==0):
                count=False
                break
            j+=1
        if(count):
            list.append(i)
        i+=2
    return list