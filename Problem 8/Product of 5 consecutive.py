# Calculate the max consecutive product of 5 digits from the question list of numbers

import math;
import time;

# val: The string to

def CalculateConsecutiveProduct(val, consec):
    result = 1;

    # Used to work out the max attainable
    max_dif_1 = 9;
    max_dif_2 = int(math.pow(9, 2));
    max_dif_3 = int(math.pow(9, 3));
    max_dif_4 = int(math.pow(9, 4));

    for i in range(len(val) - 4):
        end = i + consec;
        current_vals = val[i:end];
        current_tot = 1;

        for j in range(len(current_vals)):
            mul = int(current_vals[j]);

            if mul == 0:
                break;

            current_tot = current_tot * mul;

            if j == 0:
                maximum = current_tot * max_dif_4;
                if maximum < result:
                    break;

            elif j == 1:
                maximum = current_tot * max_dif_3;
                if maximum < result:
                    break;

            elif j == 2:
                maximum = current_tot * max_dif_2;
                if maximum < result:
                    break;

            elif j == 3:
                maximum = current_tot * max_dif_1;
                if maximum < result:
                    break;

            elif j == 4:
                if current_tot > result:
                    result = current_tot;

    return result;




question = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

starttime = time.time();
answer = CalculateConsecutiveProduct(question, 5)
endtime = time.time();
print 'Answer: ' + str(answer);
print 'Took: ' + str(endtime - starttime) + ' seconds';

