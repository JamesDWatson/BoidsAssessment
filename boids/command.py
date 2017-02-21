
#!/usr/bin/env python
from argparse import ArgumentParser
#from boids import update_boids         
from matplotlib import pyplot as plt
import yaml

#config=yaml.load(open("config.yaml"))

def process():
    parser = ArgumentParser(description = "Generate boids movement")
    parser.add_argument('--number', action="store_true", help='Specify the number of boids for the simulation')
    arguments= parser.parse_args()
    
    boid_x_pos=[random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1]) for x in range(no_boids)] 
    boid_y_pos=[random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1]) for x in range(no_boids)]
    boid_x_vel=[random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1]) for x in range(no_boids)]       
    boid_y_vel=[random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) for x in range(no_boids)]
    boids=(boid_x_pos,boid_y_pos,boid_x_vel,boid_y_vel) 
    
    
    # Updates the postions of the boids.
    def update_boids(boids):
        x_pos,y_pos,x_vel,y_vel= boids    # Use a np array to simplify loops.

        # Fly towards the middle
        for i in range(no_boids):
            for j in range(no_boids):
                x_vel[i]=x_vel[i]+(x_pos[j]-x_pos[i])*config['pos_weight']/no_boids
                y_vel[i]=y_vel[i]+(y_pos[j]-y_pos[i])*config['pos_weight']/no_boids

                if sqr_dist(x_pos[j], x_pos[i], y_pos[j], y_pos[i]) < config['pos_diff']**2:
                    x_vel[i]=x_vel[i]+(x_pos[i]-x_pos[j])
                    y_vel[i]=y_vel[i]+(y_pos[i]-y_pos[j])

                if sqr_dist(x_pos[j], x_pos[i], y_pos[j], y_pos[i]) < config['vel_diff']**2:
                    x_vel[i]=x_vel[i]+(x_vel[j]-x_vel[i])*config['vel_weight']/no_boids
                    y_vel[i]=y_vel[i]+(y_vel[j]-y_vel[i])*config['vel_weight']/no_boids


        # Move according to velocities
        for i in range(no_boids):
            x_pos[i]=x_pos[i]+x_vel[i]
            y_pos[i]=y_pos[i]+y_vel[i]
    
    
    figure=plt.figure()
    axes=plt.axes(xlim=(config['x_lim'][0],config['x_lim'][1]), ylim=(config['y_lim'][0],config['y_lim'][1]))
    scatter=axes.scatter(boids[0],boids[1])
    
    def animate(frame):
        update_boids(boids)
        scatter.set_offsets(list(zip(boids[0],boids[1])))


    anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)   
    
    plt.show()
    

if __name__ =="__main__":
    process() 
    