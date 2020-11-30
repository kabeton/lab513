import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
mpl.rcParams['figure.constrained_layout.use'] = True

d4 = pd.read_csv('data.csv')
i4 = np.array(d4['I'])[1:] / 100 
v4 = np.array(d4['V'])[1:]
d6 = pd.read_csv('data2.csv')
i6 = np.array(d6['I'])[1:] / 100 
v6 = np.array(d6['V'])[1:]

plt.scatter(v4, i4, label=r'$V = 2.3$', s=62)
plt.plot(v4, i4)
plt.scatter(v6, i6, label=r'$V = 2.9$', s=62)
plt.plot(v6, i6)

plt.xlabel(r'$V, V$', fontsize=30)
plt.ylabel(r'$I, mA$', fontsize=30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.legend(fontsize='30')

plt.grid()
plt.show()
