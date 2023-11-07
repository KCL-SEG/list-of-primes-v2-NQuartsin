"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if (number_of_primes <=0):
        raise ValueError(f"{number_of_primes}, should have been a positive number.")
    list = []
    
    i = 2 # where i is a possible prime number

    #could place a comment here to explain the purpose of the while loop
    while(len(list) < number_of_primes):
        isPrime = True
        for j in range (2,i): # where j is a possible factor of i
            if (i % j == 0):
                isPrime = False
        if (isPrime == True):
            list.append(i)
        i = i + 1
    return list
