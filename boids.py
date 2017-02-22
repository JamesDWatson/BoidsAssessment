
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml
import random
from classes import Bird

# Import variables from yaml file.
config=yaml.load(open("boids/config.yaml"))

no_boids = 50


# Define an array of boids.
boid = [0] * no_boids
for x in range(no_boids):
    boid[x] = Bird(config, no_boids) 

def update(boid):
    for i in range(no_boids):
        for j in range(no_boids):
            boid[i].x_vel  = boid[i].x_vel + boid[i].vel_change(boid[j])[0]
            boid[i].y_vel  = boid[i].y_vel + boid[i].vel_change(boid[j])[1]
            
    for i in range(no_boids):
        boid[i].x_pos=boid[i].x_pos+boid[i].x_vel
        boid[i].y_pos=boid[i].y_pos+boid[i].y_vel
                
        
figure=plt.figure()
axes=plt.axes(xlim=(config['x_lim'][0],config['x_lim'][1]), ylim=(config['y_lim'][0],config['y_lim'][1]))
scatter=axes.scatter([0] * no_boids,[0] * no_boids)

def animate(frame):
    #update(boid)
    Bird.update_boids(boid)
    position = [0] * no_boids
    for i in range(no_boids):
        position[i] = (boid[i].x_pos, boid[i].y_pos)
    scatter.set_offsets(list(position))
    
anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()