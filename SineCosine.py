import numpy as np
from matplotlib import pyplot as plt
np.pi = 3.14

'''
Numpy related code
'''
angles = np.arange(start = -360,stop = 360, step = 1)
deg = np.array(angles)
Sineval = np.sin(deg * np.pi/180)
CosVal = np.cos(deg * np.pi/180)
print(Sineval)
print(CosVal)

'''
Matplotlib related code
'''
plt.plot(angles,Sineval, label = "Sine")
plt.plot(angles,CosVal, label = "Cos")
plt.title("Sine and Cosine wave")
plt.xlabel("Angles")
plt.ylabel("Values")
plt.legend()
plt.show()