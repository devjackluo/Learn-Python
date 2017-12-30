#from statistics import *
from statistics import stdev as sd, mean as m


example_list = [3, 5, 7, 8,23,2,5,3,51,52,626,62,623]

x = sd(example_list)
print(x)

x = m(example_list)
print(x)




'''
import statistics as s

example_list = [3,5,7,8,23,2,5,3,51,52,626,62,623]

x = s.mean(example_list)
print(x)

x = s.median(example_list)
print(x)

x = s.stdev(example_list)
print(x)

x = s.variance(example_list)
print(x)

'''