[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the
difference between the groups. How does it compare to the difference in pregnancy length?

-----
```
import numpy as np
import nsfg
import first
import thinkstats2

# This is the pregnancy data stored as a data frame, subsequently separated into only the live births data.
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

# This splits the live births into two separate data frames for first born babies vs. non-first born babies.
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

print('first vs other using total weight in lbs')
print('mean:', firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean())
print('variance:', firsts.totalwgt_lb.var(), others.totalwgt_lb.var())
print('standard deviation:', firsts.totalwgt_lb.std(), others.totalwgt_lb.std())

# first vs other using total weight in lbs:
# mean: 7.20109443044 7.32585561497
# variance: 2.01802730092 1.9437810259
# standard deviation: 1.42057287772 1.39419547621

import math

def CohenEffectSize(g1, g2):
    mean_diff = g1.mean() - g2.mean()
    var1, var2 = g1.var(), g2.var()
    n1, n2 = len(g1), len(g2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    cd = mean_diff / math.sqrt(pooled_var)
    return cd

CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
```
First born babies tend to be lighter in total weight than the others group when comparing the mean. First born babies are 7.20 lbs versus 7.33 lbs for others, however, the standard deviation is higher for first babies who can vary by another 1.42 lbs versus 1.39 lbs for the others group. The effect size of the difference in total weight between first born babies and non-first born babies is -0.089 standard deviations, which is small.
