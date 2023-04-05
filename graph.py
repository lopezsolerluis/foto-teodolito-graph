import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

file = sys.argv[1]
logp = sys.argv[2] if len(sys.argv)>2 else 'lin'

def process_df(df, log, file_name, number):
    # Tomado de https://stackoverflow.com/questions/66520769/python-contour-polar-plot-from-discrete-data (and more...)
    
    colormap='rainbow'
    values = np.log10(df.measure) if log=='log' else df.measure
    theta = np.radians(df.azimuth+90) # For theta=0 at the top
    rad = 90 - df.altitude
    sensor = df["sensor name"].iloc[-1]
    [day,month,year,_,h0,m0,h1,m1] = file_name.split('-')

    fig, ax = plt.subplots()
    
    ax_polar = fig.add_axes(ax.get_position(), polar=True)
    ax_polar.set_theta_zero_location("N")  # theta=0 at the top
    ax_polar.set_theta_direction(1)  
    ax_polar.set_facecolor('none') # make transparent
    ax_polar.set_rlim(bottom=df.altitude.max(), top=df.altitude.min())    

    ax.set_aspect('equal')
    ax.axis('off')

    tcf = ax.tricontourf(rad * np.cos(theta), rad * np.sin(theta), values, levels=256, cmap=colormap)

    cax = ax.inset_axes([1.15, 0, 0.05, 1])
    fig.colorbar(tcf, cax=cax)
    
    plt.title(f"{sensor}  {day}/{month}/{year}  {h0}:{m0}~{h1}:{m1}")
    
    # plt.show()
    plt.savefig(f"graphs/{file_name}--{sensor}-{log}-{number}.png")

df_total = pd.read_csv(file)

indices = [] # To get rows when altitude changes from max to min (90 to 20, let's say)
for index, value in df_total.altitude.items():
    if df_total.iloc[index-1].altitude > value:
        indices.append(index)
indices.append(len(df_total))
print(indices)

file_path = os.path.basename(file)
file_name = os.path.splitext(file_path)[0]

for i in range(len(indices)-1):
    df = df_total[indices[i]:indices[i+1]]
    # print(df)
    process_df(df, logp, file_name, i)
