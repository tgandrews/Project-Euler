# All multiples of 3 or 5 less than 1000
a = 0;
total = 0;

while a < 1000:
    if (a % 3) == 0:
        total += a;
        print a;
    elif (a % 5) == 0:
        total += a;
        print a;
    a += 1;

print "Total: ", total
