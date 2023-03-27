import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

file = sys.argv[1]
logp = sys.argv[2] if len(sys.argv)>2 else 'lin'

df = pd.read_csv(file)

print(df)

# Tomado de https://stackoverflow.com/questions/66520769/python-contour-polar-plot-from-discrete-data (and more...)

colormap='rainbow'
values = np.log10(df.measure) if logp=='log' else df.measure

fig = plt.figure(figsize=(12, 4))

ax = fig.add_subplot(121)
tcf = ax.tricontourf(df.azimuth, df.altitude, values, levels=256, cmap=colormap)

fig.colorbar(tcf)

theta = np.radians(df.azimuth+90) # For theta=0 at the top
rad = 90 - df.altitude
ax = fig.add_subplot(122)

ax_polar = fig.add_axes(ax.get_position(), polar=True)
ax_polar.set_theta_zero_location("N")  # theta=0 at the top
ax_polar.set_theta_direction(1)  
ax_polar.set_facecolor('none') # make transparent
ax_polar.set_rlim(bottom=df.altitude.max(), top=df.altitude.min())

ax.tricontourf(rad * np.cos(theta), rad * np.sin(theta), values, levels=256, cmap=colormap)
ax.set_aspect('equal')
ax.axis('off')

#ax.set_title("A line plot on a polar axis", va='bottom')

plt.show()
