import matplotlib.pyplot as plt
from hw4_simulation import *

x = range(1, 101)
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, is_avg)
plt.plot(x, ms_avg)
plt.legend(['insertion sort', 'merge sort'], loc = "upper left", prop = {"size":10})
plt.ylabel("Average Time")
plt.xlabel("Size of sample")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
The figure shows the effect of the complexity of different sorting algorithms on runtime. The x-axis
represents sample size. The y-axis represents averge runtime across 100 different samples. All samples
were randomly drawn from the range of 1 to 1000. While runtime for both algorithms increases as the
size of the sample to sort increases, runtime for insertion sort increases more rapidly.
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
plt.savefig('hw4_plot.pdf')