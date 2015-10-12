from helper import my_func
import sys

n = int(sys.argv[1])

arr = []
for i in range(n):
    arr.append(n)

results1 = map(my_func, arr)
print "map sum:", sum(results1)
