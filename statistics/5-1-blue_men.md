[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters mu = 178 cm and sigma = 7:7 cm for men, and mu = 163 cm and sigma = 7:3 cm for women.

In order to join Blue Man Group, you have to be male between 5'10" and 6'1" (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

-----

```
# Calculating based on the BRFSS raw data.

import brfss

brfss = brfss.ReadBrfss()

male_ht = brfss.htm3[brfss.sex == 1]

h_low = 177.80 # 5'10" in cm
h_high = 185.42 # 6'1" in cm

cdf_data = thinkstats2.Cdf(male_ht)
thinkplot.Cdf(cdf_data)
thinkplot.Config(xlabel='Male Height (cm)', ylabel='CDF')

print("Pct. of US Male eligible to join BMG: ", cdf_data[h_high] - cdf_data[h_low])

mu, var, sigma = male_ht.mean(), male_ht.var(), np.sqrt(var)
print('Mean', 'Var', 'Stdev', mu, var, sigma)

x, p = thinkstats2.RenderNormalCdf(mu, sigma, low=50, high=250)
thinkplot.PrePlot(1)
thinkplot.plot(x, p, label='normal', color = '0.1')

# Pct. of US Male eligible to join BMG:  0.477290537346
# Mean Var Stdev 178.066221091 59.6534324401 7.72356345478
```
![CDF distribution of 'US Male Height (cm) - BRFSS data vs Normal Distribution'](/statistics/5-1-blue_men.png?raw=true "CDF distribution of 'US Male Height (cm) - BRFSS data vs Normal Distribution'")

```
# Calculating based on the normal distribution using scipy.stats.norm

from scipy import stats

m = 178 # BRFSS male mean height in cm
s = 7.7 # BRFSS male stdev height in cm

normal = stats.norm(m, s)
print("Pct. of US Male eligible to join BMG:", normal.cdf(h_high) - normal.cdf(h_low))

# Pct. of US Male eligible to join BMG: 0.342746837631


print("6'01\" data:", cdf_data[h_high], "dist: ", normal.cdf(h_high))
print("5'10\" data:", cdf_data[h_low], "dist: ", normal.cdf(h_low))

# 6'01" data: 0.878684256543 dist:  0.832385865496
# 5'10" data: 0.401393719197 dist:  0.489639027865

```
The BRFSS raw dataset was imported and used first. The difference in the CDFs calculated using the thinkstats2 built-in function for the data is 47.7%. This was charted against the normal distribution and then the scipy.stats.norm function was used to create a normal distribution CDF and calulated by plugging in the provided mean and sigma and the percentage of population between 5'10" and 6'1" using this method was 34.2%. Looking at the values of the percentile for the two heights using the two methods shows there is some discrepancy. 
