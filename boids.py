
from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes
# Replace the Pythagoras theorem with function.
# Write a Yaml file that contains all the necessary boundaries.

config=yaml.load(open("boids/config.yaml"))

#def pythogoras(source,target):
#    return (source.facing-target.facing)<source.viewport
posit_weight = 0.01
vel_weight = 0.125
position_difference = 10
vel_difference = 100
no_boids = 50

#Generate intial boid variables.
boid_x_pos=[random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1]) for x in range(no_boids)] 
boid_y_pos=[random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1]) for x in range(no_boids)]
boid_x_vel=[random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1]) for x in range(no_boids)]        #Generates the velocities of the boids.
boid_y_vel=[random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) for x in range(no_boids)]
boids=(boid_x_pos,boid_y_pos,boid_x_vel,boid_y_vel)



def update_boids(boids):
    x_pos,y_pos,x_vel,y_vel=boids
    
    # Fly towards the middle
    for i in range(no_boids):
        for j in range(no_boids):
            x_vel[i]=x_vel[i]+(x_pos[j]-x_pos[i])*posit_weight/no_boids
            y_vel[i]=y_vel[i]+(y_pos[j]-y_pos[i])*posit_weight/no_boids
            
            if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < position_difference**2:
                x_vel[i]=x_vel[i]+(x_pos[i]-x_pos[j])
                y_vel[i]=y_vel[i]+(y_pos[i]-y_pos[j])
            
            if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < vel_difference**2:
                x_vel[i]=x_vel[i]+(x_vel[j]-x_vel[i])*vel_weight/no_boids
                y_vel[i]=y_vel[i]+(y_vel[j]-y_vel[i])*vel_weight/no_boids
                
                
    # Move according to velocities
    for i in range(no_boids):
        x_pos[i]=x_pos[i]+x_vel[i]
        y_pos[i]=y_pos[i]+y_vel[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()