from helper import my_func2
import numpy as np
import sys


n = int(sys.argv[1])

x, y = np.zeros( (n, 100)), np.zeros( (n, 100))

for i in range(n):
    x[i] = np.linspace(-5, 5, 100)
    t = 3 * np.exp(-0.5 * (x[i] - 1.3)**2 / 0.8**2)
    t += np.random.normal(0., 0.2, x[i].shape)
    y[i] = t


gfit_results = []
for i in range(n):
    gfit_results.append(my_func2(y[i]) )

print "loop", gfit_results[0]

