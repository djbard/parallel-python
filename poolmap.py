from multiprocessing import cpu_count
from multiprocessing import Pool
from helper import my_func
import sys


n = int(sys.argv[1])

arr = []
for i in range(n):
    arr.append(n)

processes=cpu_count()
print "I have", processes, "cores here"
pool = Pool(processes)


results = pool.map(my_func, arr)
pool.close() 
pool.join()
print "pool.map:", sum(results)
