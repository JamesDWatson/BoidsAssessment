
""" Unit tests for the command file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from boids.classes import Bird
import numpy
import yaml
import random
import os

#config=yaml.load(open("boids/config.yaml"))
_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_ROOT,'config_tests.yaml')) as config_file:
        config = yaml.load(config_file)
no_boids = 50

def test_command_fails_non_numerical_input():                       #Tests that the argument is a valid place.
    with assert_raises(TypeError) as exception: 
        Bird(config, '10.1')
        
def test_Bird_fails_wrong_type():
    with assert_raises(TypeError) as exception:
        Bird(config, 50).vel_change('example')

def test_update_boid():
    with assert_raises(TypeError) as exception:
        Bird(config, 50).update_boids( 2, 'example' )
        
def test_vel_change_avoid():                          # No change in velocity if outside the chosen radius.
    assert_equal(0, Bird.vel_change_avoid([10,10],1))
    
def test_vel_matching():
    assert_equal(0, Bird(config, 50).vel_matching([10,10], 1, 1))
    
def test_vel_change():
    #Here generate two boids and find the velocity change of one relative to another.
    random.seed(0)
    boid1 = Bird(config, no_boids)
    boid2 = Bird(config, no_boids)
    delta_velx = boid1.vel_change(boid2)[0]  #should be in some range.
    assert_almost_equal(delta_velx, -0.0333147)
    
def test_update_boids():
    random.seed(0)
    boids = [ Bird(config, no_boids), Bird(config, no_boids)] 
    Bird.update_boids( 2, boids)
    assert_almost_equal( boids[0].x_pos, -23.61667314218311)  
    assert_almost_equal(boids[0].y_pos, 517.72180967788)
    
    
    