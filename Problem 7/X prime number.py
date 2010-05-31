# Finding the 10001st prime numbers

import time;
import math;

primes = [];

def IsPrime(val):
    # A number is only prime if the ceiling of it's not divisible by any
    # prime less than it's square root
    maxPrime = math.ceil(math.sqrt(val));
    for p in primes:
        if (p > maxPrime):
            break;
        elif ((val % p) == 0):
            return False;
    return True;

def FindXPrime(nth):
    i = 1;
    while(len(primes) < nth):
        i = i+1;
        if (IsPrime(i)):
            primes.append(i);

    #Finished
    last = nth - 1;
    return primes[last];

print 'Starting';
start = time.time();
print 'Result: ' + str(FindXPrime(10001));
end = time.time();
print 'Took: ' + str(end - start) + ' seconds';

