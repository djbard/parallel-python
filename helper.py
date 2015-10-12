import math

def my_func(x):
    for i in range(100):
        x+=(math.cos(x) + math.sin(x))
    return x

## a more useful function. Fitting a Gaussian to pixels? 
## to use the astropy module, you need to:
##  module load python/2.7-anaconda
import numpy as np
from astropy.modeling import models, fitting

def my_func2(y):
    ## note that this is totally hacky, cos we know what x will be. You can only pass one array to the pool,ap. This is less than ideal. 
    x = np.linspace(-5, 5, 100)

    g_init = models.Gaussian1D(amplitude=1., mean=0, stddev=1.)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_init, x, y)

    return g
