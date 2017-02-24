
""" Unit tests for the command file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from boids.classes import Bird
from boids.classes import sqr_dist
import numpy
import yaml
import random
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_ROOT,'config_tests.yaml')) as config_file:
        config = yaml.load(config_file)
no_boids = 50

def test_command_fails_non_numerical_input():                       #Tests that the argument is a valid place.
    with assert_raises(TypeError) as exception: 
        Bird(config, '10.1')
        
def test_vel_change_fails_wrong_type():
    with assert_raises(TypeError) as exception:
        Bird(config, 50).vel_change('example')

def test_update_boid():
    with assert_raises(TypeError) as exception:
        Bird(config, 50).update_boids( 2, 'example' )
        
def test_update_boid_2():
    with assert_raises(TypeError) as exception:
        boid = [0] * no_boids
        Bird(config, 50).update_boids( 'example', boid )        
        
def test_vel_change_avoid():                          # No change in velocity if outside the chosen radius.
    assert_equal(0, Bird.vel_change_avoid([10,10],1))
    
def test_vel_change_avoid_2():                          # Check for non-zero value for inside radius.
    assert abs(Bird.vel_change_avoid([10,10],1000)[0]) > 0 
    
def test_rand_generation():                          #Check correct random numbers are generated.
    for i in range(10):
        assert Bird(config, 10).x_pos < config['x_pos_bound'][1]
        assert Bird(config, 10).x_pos > config['x_pos_bound'][0]
    
def test_vel_matching():
    assert_equal(0, Bird(config, 50).vel_matching([10,10],[10,10], 1, 1))
    
def test_vel_change():
    random.seed(0)                #Use the same seed when the test is run.
    boid1 = Bird(config, no_boids)
    boid2 = Bird(config, no_boids)
    delta_velx = boid1.vel_change(boid2)[0]  #should be in some range.
    assert abs(delta_velx - -0.0999) < 0.1
    
def test_update_boids():
    random.seed(0)
    boids = [ Bird(config, no_boids), Bird(config, no_boids)] 
    Bird.update_boids( 2, boids)
    assert abs(boids[0].x_pos -  -23.68) < 0.1 
    assert abs(boids[0].y_pos - 517.72) < 0.1
    
def test_sqr_dist():   
    assert_equal(25, sqr_dist(3,4))
    