
from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes
# Replace the Pythagoras theorem with function.

boids_x=[random.uniform(-450,50.0) for x in range(50)]               #Generates the x and y coordinates of boids.
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]        #Generates the velocities of the boids.
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

posit_weight = 0.01
vel_weight = 0.125
position_difference = 10
vel_difference = 100

def update_boids(boids):
    x_pos,y_pos,x_vel,y_vel=boids
    
    # Fly towards the middle
    for i in range(len(x_pos)):
        for j in range(len(x_pos)):
            x_vel[i]=x_vel[i]+(x_pos[j]-x_pos[i])*posit_weight/len(x_pos)
            y_vel[i]=y_vel[i]+(y_pos[j]-y_pos[i])*posit_weight/len(x_pos)
            
            if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < position_difference**2:
                x_vel[i]=x_vel[i]+(x_pos[i]-x_pos[j])
                y_vel[i]=y_vel[i]+(y_pos[i]-y_pos[j])
            
            if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < vel_difference**2:
                x_vel[i]=x_vel[i]+(x_vel[j]-x_vel[i])*vel_weight/len(x_pos)
                y_vel[i]=y_vel[i]+(y_vel[j]-y_vel[i])*vel_weight/len(x_pos)
                
                
    # Move according to velocities
    for i in range(len(x_pos)):
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