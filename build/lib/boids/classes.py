import random
import yaml
import numpy as np
import os

no_boids = 50
#config=yaml.load(open("boids/config.yaml"))
_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_ROOT,'config.yaml')) as config_file:
        config = yaml.load(config_file)


def sqr_dist(x, y):
    return ( x**2 + y**2)

class Bird(object):
    def __init__(self, config, no_boids): #, x_pos, y_pos, x_vel, y_vel, config, no_boids): 
        
        #Test no_boids is integer.
        def is_integer(s):    #Function checks if string has a representation as an integer.
            try:
                int(s)
                return True
            except ValueError:
                return False
    
        if is_integer(no_boids) == False:
            raise TypeError("Number of boids should be an integer.")
        
        #Initialise the boid's values.
        self.x_pos = random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1])  #Generate initial conditions.
        self.y_pos = random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1])
        self.x_vel = random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1])
        self.y_vel = random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) 
        self.no_boids = no_boids
        
        if self.x_pos >= config['x_pos_bound'][1]  or config['x_pos_bound'][0] >= self.x_pos:  #Ensure the generate numbers are correct.
            raise ValueError("x position is not between the expected limits.")
        
        
    def vel_change_avoid(position_diff, avoid_radius):
        if sqr_dist(position_diff[0], position_diff[1]) < avoid_radius**2:
            return([-position_diff[0], -position_diff[1]])
            #return( - position_diff)
        else:
            return(0)
        
    def vel_matching(self, position_diff, vel_diff, vel_weight, vel_match_radius):
        if sqr_dist(position_diff[0], position_diff[1]) < vel_match_radius**2:
            return( vel_diff*vel_weight/self.no_boids )
        else:
            return(0)
        
    def vel_change(self, other_boid):  #Calculate the change of v and then add it to the current one.
        if str(type(other_boid)) != "<class 'boids.classes.Bird'>":
            raise TypeError("Input must be of class Bird.")   
            
        delta_vel = np.array([0,0])
        position_diff = np.array([other_boid.x_pos - self.x_pos, other_boid.y_pos - self.y_pos ])
        vel_diff = np.array([other_boid.x_vel - self.x_vel, other_boid.y_vel - self.y_vel ])
        
        delta_vel = delta_vel + position_diff*config['avoid_weight']/self.no_boids + Bird.vel_change_avoid(position_diff,config['avoid_radius']) 
        +Bird.vel_matching( self, position_diff, vel_diff, config['vel_weight'], config['vel_radius'])
        
        return(delta_vel)
    
    # Function updating the positions and velocities of the boids.
    def update_boids(no_boids, boid ):
        
        if type(boid) !=  list or type(no_boids) != int:
            raise TypeError("Input to update_boids should be an integer and a list of boids.")
        
        for i in range(no_boids):
            for j in range(no_boids):
                boid[i].x_vel  = boid[i].x_vel + boid[i].vel_change(boid[j])[0]
                boid[i].y_vel  = boid[i].y_vel + boid[i].vel_change(boid[j])[1]

        for i in range(no_boids):
            boid[i].x_pos=boid[i].x_pos+boid[i].x_vel
            boid[i].y_pos=boid[i].y_pos+boid[i].y_vel
        
        return(boid)
    
#THE FOLLOWING CODE RUNS vel_change FASTER THAN THE ABOVE, BUT IS NOT AS READABLE. I HAVE KEPT IT FOR THE PURPOSES OF THIS ASSESSMENT.
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