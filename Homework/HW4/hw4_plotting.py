import matplotlib.pyplot as plt
from hw4_simulation import *

x = range(1, 101)
plt.plot(x, is_avg)
plt.plot(x, ms_avg)
plt.legend(['insertion sort', 'merge sort'], loc = "upper left")
plt.ylabel("Average Time for 100 samples")
plt.xlabel("Size of sample")
plt.show()