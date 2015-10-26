# parallel-python
A set of very short, simple scripts that demonstrate how to run multi-threaded code with the python multiprocessing module. See the file multiprocessing-examples.pdf for timing info on Edison (24-core node) at NERSC, and on a MacBook Air (4-core). 

Set 1
------
loop.py, map.py, numpyVectorize.py, poolmap.py

Each script is executing the same function (defined in helper.py) a specified number of times, given at the command line. There are several different ways to run this - in a simple loop, using the map function, using numpy.vectorize, and using a multiprocess pool.

A comparison of the timings will show that using multiprocessing is slower for small tasks (i.e. a low-load function or a small number of iterations), due to the overhead required to set up the threads. 

It is recommended to run the timing test using the system function time, for example:

 >time python poolmap.py 100000
 
in order to see how much CPU time is used in the multi-threaded example, in comparison to the real time passing. 

Set 2
------
loop-fitG.py, poolmap-fitG.py

Slightly more useful example, where we use astropy to fit a 1D Gaussian function to pixel data. 
