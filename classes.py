from random import random
import random

no_boids = 50

class Bird(object):
    def __init__(self): 
        self.x_pos = [random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1])]  
        self.y_pos = [random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1])]
        self.x_vel = [random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1])] 
        self.y_vel = [random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1])] 
    

birds = [0] * no_boids
    
for x in range(no_boids):
    birds[x] = Bird()
       
print(birds[1].x_pos)