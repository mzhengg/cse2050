from matplotlib import pyplot as plt        # import plotting funcs
from TimeFunctions import  time_function    # import the time function you will write
from Duplicates import has_duplicates_1, has_duplicates_2     # import the has_duplicates functions you are interested in


# All code below is included as a demo. Feel free to change any of it.

##### Initialize datasets
# Pick x-values
x = [i for i in range(0, 1001, 50)]

##### Measure the running times
# Generate corresponding y-values
y1 = []
for n in x:
    L = [i for i in range(n)] # Worst case: A list with no duplicates
    y1.append(1000*time_function(has_duplicates_1, L)) # append running time to y

y2 = []
for n in x:
    L = [i for i in range(n)] # Worst case: A list with no duplicates
    y2.append(1000*time_function(has_duplicates_2, L)) # append running time to y

##### Plot datasets
plt.figure()                                                    # create a new figure
plt.title("number of items (n) vs. running time (ms)")
plt.scatter(x, y1, c='r', marker='x', label='has_duplicates_1')     # add scatter plot to figure
plt.xlabel("number of items (n)")
plt.ylabel("running time (ms)")                                      # label y axis
plt.legend()                                                        # add legend to figure
#plt.show()                                                          # show figure on local computer
plt.savefig('fig_1.png')                                          # save figure

# Note: You can either use plt.show() or plt.savefig(). Using both does not work.
plt.figure()                                                        # create a new figure
plt.title("number of items (n) vs. running time (ms)")
plt.scatter(x, y1, c='r', marker='x', label='has_duplicates_1')     # add scatter plot to figure
plt.scatter(x, y2, c='b', marker='o', label='has_duplicates_2')
plt.xlabel("number of items (n)")
plt.ylabel("running time (ms)")                                      # label y axis
plt.legend()                                                        # add legend to figure
#plt.show()                                                          # show figure on local computer
plt.savefig('dups.png')                                          # save figure

# Note: You can either use plt.show() or plt.savefig(). Using both does not work.