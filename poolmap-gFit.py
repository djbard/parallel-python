from multiprocessing import cpu_count
from multiprocessing import Pool
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

processes=cpu_count()
print "I have", processes, "cores here"
pool = Pool(processes)


results = pool.map(my_func2, y)
pool.close() 
pool.join()
print "pool.map:", results[0]
