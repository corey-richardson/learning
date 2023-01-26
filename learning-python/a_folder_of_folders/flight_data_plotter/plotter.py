from matplotlib import pyplot as plt
import pandas as pd

rotate = 1

data = pd.read_csv("flight_data.csv")

fig = plt.figure()
ax = plt.axes(projection='3d')

x = data.loc[:,"Longitude"]
y = data.loc[:,"Latitude"]
z = data.loc[:,"Altitude"]

speed = data.loc[:,"Speed"]

ax.scatter3D(x,y,z,c=speed)

ax.invert_yaxis() 

ax.set_xlabel("Longitude NS")
ax.set_ylabel("Latitude WE")

ax.text(28.9504, -13.6058, 0, "ACE")
ax.text(50.7350, -3.4153, 0, "EXT")

ax.plot3D(x,y,0,"red")
ax.plot3D([28.9504,50.7350],[-13.6058,-3.4153],0,"orange")

if rotate == 1:
    while True: # can only be quit with keyboard interrupts, not ideal
        import itertools as it
        for i in it.chain(range(-180, 180), range(180, 180)):
            # loops -180 --> 180 --> -180...
            # changes view angle to rotation animation
            ax.view_init(elev = 20, azim = i, roll = 0)
            plt.pause(0.01) # delay
            plt.draw() # update figure
else:
    ax.view_init(elev = 20, azim = -135, roll = 0) 
    ax.set_xlabel("Longitude SN")
    plt.show()