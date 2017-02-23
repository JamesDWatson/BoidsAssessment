import random
import yaml
import numpy as np

no_boids = 50
config=yaml.load(open("boids/config.yaml"))

def sqr_dist(x, y):
    return ( x**2 + y**2)

class Bird(object):
    def __init__(self, config, no_boids): #, x_pos, y_pos, x_vel, y_vel, config, no_boids): 
        
        def is_integer(s):    #Function checks if string has a representation as a float.
            try:
                int(s)
                return True
            except ValueError:
                return False
    
        if is_integer(no_boids) == False:
            raise TypeError("Number of boids should be an integer.")
        
        self.x_pos = random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1])  #Generate initial conditions.
        self.y_pos = random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1])
        self.x_vel = random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1])
        self.y_vel = random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) 
        self.no_boids = no_boids
        
        
    def vel_change(self, other_boid):  #Calculate the change of v and then add it to the current one.
        #delta_velx = 0
        #delta_vely = 0
        
        #x_diff = self.x_pos - other_boid.x_pos
        #y_diff = self.y_pos - other_boid.y_pos
        
        #delta_velx += -x_diff*config['avoid_weight']/no_boids
        #delta_vely += -y_diff*config['avoid_weight']/no_boids
        
        #if sqr_dist(x_diff, y_diff) < config['avoid_radius']**2:  #Velocity correction due to birds avoiding each other.
        #    delta_velx += x_diff
        #    delta_vely += y_diff
        
        #if sqr_dist(x_diff, y_diff) < config['vel_radius']**2:    #Velocity correction due to velocity matching
        #    delta_velx += (other_boid.x_vel - self.x_vel)*config['vel_weight']/no_boids
        #    delta_vely += (other_boid.y_vel - self.y_vel)*config['vel_weight']/no_boids
        
        #return([delta_velx, delta_vely])
        
        if str(type(other_boid)) != "<class '__main__.Bird'>":
            raise TypeError("Input must be of class Bird.")
        
        delta_vel = np.array([0,0])
        position_diff = np.array([other_boid.x_pos - self.x_pos, other_boid.y_pos - self.y_pos ])
        
        delta_vel = delta_vel + position_diff*config['avoid_weight']/no_boids
        
        if sqr_dist(position_diff[0], position_diff[1]) < config['avoid_radius']**2:
            delta_vel = delta_vel - position_diff
            
        if sqr_dist(position_diff[0], position_diff[1]) < config['vel_radius']**2:
            delta_vel = delta_vel + position_diff*config['vel_weight']/no_boids
        
        return(delta_vel)
    
    # Function updating the positions and velocities of the boids.
    def update_boids( boid ):
        for i in range(no_boids):
            for j in range(no_boids):
                boid[i].x_vel  = boid[i].x_vel + boid[i].vel_change(boid[j])[0]
                boid[i].y_vel  = boid[i].y_vel + boid[i].vel_change(boid[j])[1]

        for i in range(no_boids):
            boid[i].x_pos=boid[i].x_pos+boid[i].x_vel
            boid[i].y_pos=boid[i].y_pos+boid[i].y_vel
        
        return(boid)
    
#    def animate_boids(frame, boid):
#        #update(boid)
#        Bird.update_boids(boid)
#        position = [0] * no_boids
#        for i in range(no_boids):
#            position[i] = (boid[i].x_pos, boid[i].y_pos)
#        scatter.set_offsets(list(position))
        
        
#birds = [0] * no_boids
    
#for x in range(no_boids):
#    birds[x] = Bird()

#print(birds[1].x_pos)