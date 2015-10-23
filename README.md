# parallel-python
A set of very short, simple scripts that demonstrate how to run multi-threaded code with the python  multiprocessing module.

Set 1
------
loop.py, map.py, numpyVectorize.py, poolmap.py

Each script is executing the same function (defined in helper.py) a specified number of times, given at the command line. There are several different ways to run this - in a simple loop, using the map function, using numpy.vectorize, and using a multiprocess pool.

A comparison of the timings will show that using multiprocessing is slower for small tasks (i.e. a low-load function or a small number of iterations), due to the overhead required to set up the threads. 

Set 2
------
loop-fitG.py, poolmap-fitG.py

Slight more useful example, where we use astropy to fit a Gaussian function to pixel data. 