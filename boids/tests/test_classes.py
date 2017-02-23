
import yaml
from nose.tools import assert_raises, assert_almost_equal, assert_equal


""" Unit tests for the command file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from classes import Bird
import numpy

config=yaml.load(open("boids/config.yaml"))

def test_command_fails_non_numerical_input():                       #Tests that the argument is a valid place.
    with assert_raises(TypeError) as exception: 
        Bird(config, '10.1')
