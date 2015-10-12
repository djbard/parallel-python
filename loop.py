from helper import my_func
import sys

n = int(sys.argv[1])

arr = []
for i in range(n):
    arr.append(n)

results = []
for i in range(n):
    results.append(my_func(arr[i]))

print "loop sum:", sum(results1)
