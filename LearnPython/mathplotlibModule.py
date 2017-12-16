from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

'''
x= [5,6,7,9]
y= [7,8,9,15]

x2= [3,4,5,6]
y2= [3,5,2,7]

#plt.grid(True, color='k')
#plt.plot(x,y,'g',linewidth=5, label='line1')
#plt.plot(x2,y2,'c',linewidth=6, label='line2')

#plt.scatter(x,y,color='c')
#plt.scatter(x2,y2,color='g')

plt.bar(x,y,color='c')
plt.bar(x2,y2,color='g')
'''


x, y = np.loadtxt('matplotCSV.csv', unpack=True, delimiter=',')
x = np.sort(x)
y = np.sort(y)
plt.plot(x,y)
print(x)
print(y)



plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X Axis')
#plt.legend()



plt.show()
