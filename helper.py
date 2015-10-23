


### A simple, somewhat arbitrary function 
def my_func(x):
    import math
    for i in range(100):
        x+=(math.cos(x) + math.sin(x))
    return x


## a more useful function. Fitting a Gaussian to pixel data. 
## Note: to use the astropy module on Edison, you need to:
##  module load python/2.7-anaconda

def my_func2(y):
    import numpy as np
    from astropy.modeling import models, fitting
    ## You can only pass one variable to the function (not ideal) so we re-define x here. 
    x = np.linspace(-5, 5, 100)

    g_init = models.Gaussian1D(amplitude=1., mean=0, stddev=1.)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_init, x, y)

    return g
