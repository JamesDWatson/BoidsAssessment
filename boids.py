
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
    #boid_x_pos=random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1]) 
    #boid_y_pos=random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1]) 
    #boid_x_vel=random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1])        
    #boid_y_vel=random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) 
    boid[x] = Bird(config, no_boids) #boid_x_pos,boid_y_pos,boid_x_vel,boid_y_vel, config, no_boids)

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
    #update_boids(boids)
    update(boid)
    position = [0] * no_boids
    for i in range(no_boids):
        position[i] = (boid[i].x_pos, boid[i].y_pos)
    scatter.set_offsets(list(position))
    
    #x_position = [0] * no_boids    #Replace this with just position = [boid.x_pos, boid.y_pos]
    #y_position = [0] * no_boids
    #for i in range(no_boids):
    #    x_position[i] = boid[i].x_pos
    #    y_position[i] = boid[i].y_pos
    
    #scatter.set_offsets(list(zip(x_position, y_position)))
    
    
anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()