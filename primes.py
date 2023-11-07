"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if (number_of_primes <=0):
        raise ValueError(f"{number_of_primes}, should have been a positive number.")
    list = []
    
    #could use more indicative variable names than i and j. I guess
    possible_prime = 2 

    #could place a comment here to explain the purpose of the while loop
    while(len(list) < number_of_primes):
        isPrime = True
        for j in range (2,i): # where j is a possible factor of i
            if (possible_prime % j == 0):
                prime = False
        if (prime == True):
            list.append(i)
        i = i + 1
    return list
