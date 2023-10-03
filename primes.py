"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if (number_of_primes <=0):
        raise ValueError(f"{number_of_primes}, should have been a positive number.")
    list = []
    counter = 0
    i = 2
    while(counter < number_of_primes):
        prime = True
        for j in range (2,i):
            if (i%j == 0):
                prime = False
        if (prime = True):
            list.append(i)
            counter = counter + 1
        i = i + 1
    return list
