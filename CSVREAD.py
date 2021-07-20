from glob import glob
files = glob('csv*.csv')
files.sort()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
for file in files:
    data = (pd.read_csv(file))
    x = np.sort(data)
    y = np.arange(1, len(x) +1) / len(x)
    plt.plot(x,y, marker ='.', linestyle='none')
plt.show()
