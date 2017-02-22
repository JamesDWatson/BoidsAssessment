
from setuptools import setup, find_packages

setup(
    name = "Boids",
    description='Bird Flock Simulator',
    version = "0.1.0",
    author='James Watson',
    author_email='05watson.j@gmail.com',
    url='https://github.com/JamesDWatson',
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/betterboids'],
    install_requires = ['argparse', 'pyyaml', 'matplotlib', 'numpy']   
)