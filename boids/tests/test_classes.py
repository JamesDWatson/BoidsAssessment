
""" Unit tests for the command file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from classes import Bird
import numpy
import yaml
import random

config=yaml.load(open("boids/config.yaml"))
no_boids = 50

def test_command_fails_non_numerical_input():                       #Tests that the argument is a valid place.
    with assert_raises(TypeError) as exception: 
        Bird(config, '10.1')
        
def test_Bird_fails_wrong_type():
    with assert_raises(TypeError) as exception:
        Bird(config, 50).vel_change('example')

def test_update_boids():
    with assert_raises(TypeError) as exception:
        Bird.update_boids( 'example' )
        
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

    
    