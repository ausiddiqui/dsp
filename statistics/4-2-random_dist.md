[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The numbers generated by random.random are supposed to be uniform between 0 and 1; that is, every value in the range should have the same probability.

Generate 1000 numbers from random.random and plot their PMF and CDF. Is the distribution uniform?

-----
```
import numpy as np
import thinkstats2
import thinkplot

sample = np.random.random(1000)

pmf = thinkstats2.Pmf(sample)
thinkplot.Pmf(pmf, linewidth=0.05)
thinkplot.Config(xlabel='Random sample values', ylabel='PMF')
```

![PMF distribution of 'Random sample values'](/statistics/4-2-random_dist1.png?raw=true "PMF distribution of 'Random sample values'")

```
cdf = thinkstats2.Cdf(sample)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random sample values', ylabel='CDF')
```
![CDF distribution of 'Random sample values'](/statistics/4-2-random_dist2.png?raw=true "CDF distribution of 'Random sample values'")

The sampled values are uniformly distributed as all 1,000 values roughly have a similar number of observations and chance of occurrence. The PMF distribution chart shows that almost all the values roughly have the same probability of occurring. In the CDF chart, it can be seen that the line is a nearly straight line that is proportional, roughly 20% of the sample are below the 20th percentile and 50% below 50th and so on.
