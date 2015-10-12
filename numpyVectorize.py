from numpy import vectorize, arange, sum, shape
from helper import my_func
import sys


n = int(sys.argv[1])

arr = arange(n)
results = vectorize(my_func)
print "numpy.vectorize:", sum(results(arr))

