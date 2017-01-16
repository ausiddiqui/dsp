[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.

Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.

-----
```
import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

resp = nsfg.ReadFemResp()
resp.numkdhh

pmf_numkdhh = thinkstats2.Pmf(resp.numkdhh, label = 'actual')

thinkplot.Pmf(pmf_numkdhh)
thinkplot.Config(xlabel='Number of children under 18', ylabel='PMF')
```

![PMF distribution of 'Number of Children Under 18 - actual'](/statistics/3-1-actual_biased_pmf1.png?raw=true "PMF distribution of 'Number of Children Under 18 - actual")

```
def BiasPMF(pmf, l):
    bias_pmf = pmf.Copy(label=l)

    for x, p in pmf.Items():
        bias_pmf.Mult(x, x)

    bias_pmf.Normalize()
    return bias_pmf

pmf_numkdhh_b = BiasPMF(pmf_numkdhh, "observed")

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_numkdhh, pmf_numkdhh_b])
thinkplot.Config(xlabel='Number of children under 18', ylabel='PMF')
```
![PMF distribution of 'Number of Children Under 18 - actual vs observed'](/statistics/3-1-actual_biased_pmf2.png?raw=true "PMF distribution of 'Number of Children Under 18 - actual vs observed")

```
print("Mean of Actual vs. Biased PMF of Number of Children under 18:")
pmf_numkdhh.Mean(), pmf_numkdhh_b.Mean()

# Mean of Actual vs. Biased PMF of Number of Children under 18:
# (1.0242051550438309, 2.4036791006642821)
```
The probability weighted mean of number of children under 18 varies significantly between the actual and the observed distributions, the value is 1.02 for the former and 2.40 for the latter. This difference is in part due to the fact that in the observed statistic samples with zero children are completely discarded which has a PMF of 0.47 in the actual sample. 
