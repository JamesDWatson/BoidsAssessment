
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml
import random
from boids.classes import Bird
import os

 # Import variables from yaml file.
#config=yaml.load(open("boids/config.yaml"))
_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_ROOT,'config.yaml')) as config_file:
        config = yaml.load(config_file)
#no_boids = int(arguments.number)
no_boids = 50   #Need to get this from the command line.

# Initialise an array of boids, specified by the Bird class.
boid = [0] * no_boids
for x in range(no_boids):
        boid[x] = Bird(config, no_boids) 

figure=plt.figure()
axes=plt.axes(xlim=(config['x_lim'][0],config['x_lim'][1]), ylim=(config['y_lim'][0],config['y_lim'][1]))
scatter=axes.scatter([0] * no_boids,[0] * no_boids)

def animate(frame):
    Bird.update_boids(no_boids, boid)
    position = [0] * no_boids
    for i in range(no_boids):
        position[i] = (boid[i].x_pos, boid[i].y_pos)
    scatter.set_offsets(list(position))

anim = animation.FuncAnimation(figure, animate,
                                   frames=50, interval=50)


if __name__ == "__main__":
    plt.show()