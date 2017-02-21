from random import random
import random
import yaml

no_boids = 50
config=yaml.load(open("boids/config.yaml"))

def sqr_dist(x_1, x_2, y_1, y_2):
    return ( (x_1-x_2)**2 + (y_1 - y_2)**2)

class Bird(object):
    def __init__(self): 
        self.x_pos = [random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1])]  #Generate initial conditions.
        self.y_pos = [random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1])]
        self.x_vel = [random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1])] 
        self.y_vel = [random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1])] 
    
        
#birds = [0] * no_boids
    
#for x in range(no_boids):
#    birds[x] = Bird()

#print(birds[1].x_pos)
    
#class Flock(object)
#    def __init__(self, number, config):
#        self.number = number
#        self.initial = initial    #defines the initial positions and velocities.
        
#    update_flock(self)
        
        
        