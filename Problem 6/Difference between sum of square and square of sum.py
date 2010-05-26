# Difference between sum of square and square of sum
# (1^2 + 2^2) - (1 + 2)^2

import time;

def Sum(maxVal):
    resultSquares = 0;
    resultSum =  0;

    i = 0;
    while i <= maxVal:
        resultSquares += (i * i);
        resultSum += i;
        i = i + 1;

    print 'Sum: ' + str(resultSum);
    print 'Sum of squares: ' + str(resultSquares);

    resultSumSquared = resultSum * resultSum;
    result = resultSumSquared - resultSquares;

    return result;

print 'Working on first 100 natural numbers'
start = time.time();
result = Sum(100);
end = time.time();
print 'Result: ' + str(result);
print 'Took: ' + str(end - start) + ' seconds';

