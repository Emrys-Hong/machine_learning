```
from matplotlib import pyplot as plt
plt.figure(num=3, figsize=(8,5),)
plt.plot(x,y)
plt.scatter(x,y)
plt.bar(x,y)
plt.xticks(x,name) # if we want to label the data, x is a list for the position where the label want to be
plt.xticks(())  # ignore xticks
plt.xlabel('x_name')
plt.xlim( (start,end) ) # to see where x start and ends
plt.plot(x,y,color='red', linewidth=1.0, linestyle='--',label='label_name')
plt.legend(handles=[first_plot,second_plot],labels=['up','down'],loc='best')
```
-----------------------------------------------------------------------------------------------------------------------------
#### others code
# 3 - simple plot
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1
# y = x**2
plt.plot(x, y)
plt.show()

# 11 - bar
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()

