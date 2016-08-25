from hw4_functions import *
import timeit
import random
import numpy

## Function to run the two sort methods with
## a random sample of size 'n' with that sample
## drawn from 1:r range. (below I set that range
## to 1000)
## The function times how long it takes for each
## function to execute on the same random sample.
def sort_simulation(n, r):
	random_list = random.sample(range(r), n)

	start_time = timeit.default_timer()
	insertion_sort(random_list)
	is_time = timeit.default_timer() - start_time
	
	start_time = timeit.default_timer()
	merge_sort(random_list)
	ms_time = timeit.default_timer() - start_time

	return is_time, ms_time


## This loop calls 'sort_simulation()' 100 times
## for each n in order to average the time it
## takes for different random samples.
is_avg = []
ms_avg = []
for n in range(1, 101):
	is_avg_these = []
	ms_avg_these = []
	for i in range(100):
		is_time, ms_time = sort_simulation(n, 1000)
		is_avg_these.append(is_time)
		ms_avg_these.append(ms_time)
	is_avg.append(numpy.mean(is_avg_these))
	ms_avg.append(numpy.mean(ms_avg_these))






