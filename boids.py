
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml
import random
from classes import Bird


# Import variables from yaml file.
config=yaml.load(open("boids/config.yaml"))

# Calculates distance between points via Pythogaras' theorem -- used later.
def sqr_dist(x_1, x_2, y_1, y_2):
    return ( (x_1-x_2)**2 + (y_1 - y_2)**2)

no_boids = 50

#Generate intial boid variables.
#boid_x_pos=[random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1]) for x in range(no_boids)] 
#boid_y_pos=[random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1]) for x in range(no_boids)]
#boid_x_vel=[random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1]) for x in range(no_boids)]       
#boid_y_vel=[random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) for x in range(no_boids)]
#boids=(boid_x_pos,boid_y_pos,boid_x_vel,boid_y_vel)

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
    
            
    
# Updates the postions of the boids.
#def update_boids(boids):
#    x_pos,y_pos,x_vel,y_vel= boids    # Use a np array to simplify loops.
    
    # Fly towards the middle
#    for i in range(no_boids):
#        for j in range(no_boids):
#            x_vel[i]=x_vel[i]+(x_pos[j]-x_pos[i])*config['avoid_weight']/no_boids
#            y_vel[i]=y_vel[i]+(y_pos[j]-y_pos[i])*config['avoid_weight']/no_boids
            
#            if sqr_dist(x_pos[j], x_pos[i], y_pos[j], y_pos[i]) < config['avoid_radius']**2:
#                x_vel[i]=x_vel[i]+(x_pos[i]-x_pos[j])
#                y_vel[i]=y_vel[i]+(y_pos[i]-y_pos[j])
            
#            if sqr_dist(x_pos[j], x_pos[i], y_pos[j], y_pos[i]) < config['vel_radius']**2:
#                x_vel[i]=x_vel[i]+(x_vel[j]-x_vel[i])*config['vel_weight']/no_boids
#                y_vel[i]=y_vel[i]+(y_vel[j]-y_vel[i])*config['vel_weight']/no_boids
                
              
    # Move according to velocities
#    for i in range(no_boids):
#        x_pos[i]=x_pos[i]+x_vel[i]
#        y_pos[i]=y_pos[i]+y_vel[i]


#For convinience, define boids as the array of position values.
for i in range(no_boids): #This won't change with time as it's outside function.
        boids =[ boid[i].x_pos, boid[i].y_pos ]

figure=plt.figure()
axes=plt.axes(xlim=(config['x_lim'][0],config['x_lim'][1]), ylim=(config['y_lim'][0],config['y_lim'][1]))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    #update_boids(boids)
    update(boid)

    #scatter.set_offsets(list(zip(boids[0],boids[1]))) # need to update the positions.
    x_position =  [0] * no_boids
    y_position = [0] * no_boids
    for i in range(no_boids):
        x_position[i] = boid[i].x_pos
        y_position[i] = boid[i].y_pos
    
    scatter.set_offsets(list(zip(x_position, y_position)))
    #scatter.set_offsets(np.array(boids).transpose())
    
anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()