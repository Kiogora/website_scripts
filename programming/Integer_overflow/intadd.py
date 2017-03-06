# -*- coding: utf-8 -*-
#Colormap ref: http://matplotlib.org/examples/color/colormaps_reference.html

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x,y = np.mgrid[:256,:256]
out=x+y
out=out.astype(np.uint8)

ax.plot_surface(x,y,out,cmap=plt.get_cmap('plasma'))
plt.title("Unsigned 8 bit integer addition(x+y) overflow surface plot")
plt.xlabel("Unsigned integer X")
plt.ylabel("Unsigned integer Y")
plt.xlim(0,255)
plt.ylim(0,255)
plt.show()