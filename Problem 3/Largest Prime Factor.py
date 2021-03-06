import math

def isPrime(val):
    print 'isPrime? ',val;
    a = val/2;
    b = 2;
    while b < a:
        if ((val % b) == 0):
            print 'Divisible by ',b;
            return False;
        b += 1;
    return True;

def largestPrimeFactor(value):
    # Know that all factors must be at most sqrt of it's value
    c = math.ceil(math.sqrt(value));
    # Go down 1 by 1 checking if prime
    while c > 0:
        if ((value % c) == 0):
            if isPrime(c):
                return c;
        c -= 1;
    return 'Failed';

question = 600851475143;
#question = 13195
result = largestPrimeFactor(question);
print 'Result: ', result

