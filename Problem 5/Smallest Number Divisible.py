# Smallest number divisible
import time;

def IsPrime(val):
    i = 2;
    while i < val:
        if (val % i) == 0:
            return False;
        else:
            i = i + 1;
        return True;
    return True;

def DivisibleByList(l, val):
    for k in l:
        if (val % k) != 0:
            return False;
    return True;

def SmallestNumberDivisible(minVal, maxVal):

    # Add all primes to array
    primes = [];
    # All others added, so only check these if passed primes
    others = [];
    for i in range(minVal, maxVal):
        if IsPrime(i):
            primes.append(i);
        else:
            others.append(i);

    for j in primes:
        print j;

    found = False;
    result = 0;
    while found == False:
        result += maxVal;
        if DivisibleByList(primes, result) and DivisibleByList(others, result):
            return result;

print 'Working on numbers 1 to 20';
start = time.time();
print 'Result: ' + str(SmallestNumberDivisible(1,20));
end = time.time();
print 'It took ' + str(end - start) + ' seconds.';

