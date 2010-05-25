# Largest palindrome number of 3 digits
import time;

# Return palindrome
def isPalindrome(val):
    forward = str(val);
    # Using python slicing to reverse the string
    reverse = forward[::-1];
    if (forward == reverse):
        return True;
    else:
        return False;


def largestPalindrome(digits):

    maxStr = '';
    maxDigits = digits;
    while maxDigits > 0:
        maxStr += '9';
        maxDigits = maxDigits - 1;

    minStr = '1';
    minDigits = digits - 1;
    while minDigits > 0:
        minStr += '0';
        minDigits = minDigits - 1;

    print 'Starting point: ';
    starting = val = int(maxStr);
    print starting;

    print 'Ending point: ';
    ending = int(minStr);
    print ending;

    largest = 0;

    while starting > ending:
        # Avoid duplication 4 x 5 = 5 x 4
        val = starting;

        while val > ending:
            calc = val * starting;
            # Stop when the largest multiple that can be calculated by this number
            # is less than the largest palindrome we know
            if (val == starting) and (calc < largest):
                return  largest;

            if isPalindrome(calc):
                if calc > largest:
                    largest = calc;
                    break;
                else:
                    break;
            else:
                val = val - 1;

        #print 'Searching failed for: ' + str(starting);
        starting = starting - 1;





question = 3;
start = time.time();
print 'Result: ' + str(largestPalindrome(question));
end = time.time();

print 'Result took: ' + str(end - start);

#result = largestPalindrome(question);
#print 'Result: ', result

