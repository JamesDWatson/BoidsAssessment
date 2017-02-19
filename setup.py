
from setuptools import setup, find_packages

setup(
    name = "Boids",
    description='Bird Flock Simulator',
    version = "0.1.0",
    author='James Watson',
    author_email='05watson.j@gmail.com',
    url='https://www.placeholder.org',
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greet'],
    install_requires = ['argparse']   #Need to update with relevant packages.
)