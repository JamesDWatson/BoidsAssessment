from random import random
import random
import yaml

no_boids = 50
config=yaml.load(open("boids/config.yaml"))

def sqr_dist(x_1, x_2, y_1, y_2):
    return ( (x_1-x_2)**2 + (y_1 - y_2)**2)

class Bird(object):
    def __init__(self, config, no_boids): #, x_pos, y_pos, x_vel, y_vel, config, no_boids): 
        self.x_pos = random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1])  #Generate initial conditions.
        self.y_pos = random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1])
        self.x_vel = random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1])
        self.y_vel = random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) 
        #self.x_pos = x_pos
        #self.y_pos = y_pos
        #self.x_vel = x_vel
        #self.y_vel = y_vel
        
    def vel_change(self, other_boid):  #Calculate the change of v and then add it to the current one.
        delta_velx = 0
        delta_vely = 0
        
        #print(type(self.x_pos))
        x_diff = self.x_pos - other_boid.x_pos
        y_diff = self.y_pos - other_boid.y_pos
        
        delta_velx += -x_diff*config['avoid_weight']/no_boids
        delta_vely += -y_diff*config['avoid_weight']/no_boids
        
        if x_diff**2 +y_diff**2 < config['avoid_radius']**2:  #Velocity correction due to birds avoiding each other.
            delta_velx += x_diff
            delta_vely += y_diff
        
        if x_diff**2 +y_diff**2 < config['vel_radius']**2:    #Velocity correction due to velocity matching
            delta_velx += (other_boid.x_vel - self.x_vel)*config['vel_weight']/no_boids
            delta_vely += (other_boid.y_vel - self.y_vel)*config['vel_weight']/no_boids
        
        return([delta_velx, delta_vely])
        
#birds = [0] * no_boids
    
#for x in range(no_boids):
#    birds[x] = Bird()

#print(birds[1].x_pos)
    
#class Flock(object):
#    def __init__(self, number, config):
#        self.number = number
#        self.initial = initial    #defines the initial positions and velocities.
        
#    update_flock(self)
        
        
        