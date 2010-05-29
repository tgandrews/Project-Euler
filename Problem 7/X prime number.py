# Finding the 1001st prime numbers

import time;

primes = [];

def IsPrime(val):
    for p in primes:
        if ((val % p) == 0):
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

