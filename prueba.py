import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('microbit.csv')

print(df)

# Tomado de https://stackoverflow.com/questions/66520769/python-contour-polar-plot-from-discrete-data

fig = plt.figure(figsize=(12, 4))

ax = fig.add_subplot(121)
ax.tricontourf(df.azimuth, df.altitude, df.measure, levels=256, cmap='hsv')

ax = fig.add_subplot(122)
theta = np.radians(df.azimuth)
rad = df.altitude
ax.tricontourf(rad * np.cos(theta), rad * np.sin(theta), df.measure, levels=256, cmap='hsv')
ax.set_aspect('equal')
ax.axis('off')

ax_polar = fig.add_axes(ax.get_position(), polar=True)
ax_polar.set_facecolor('none') # make transparent
ax_polar.set_ylim(0, rad.max())

plt.show()
