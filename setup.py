
from setuptools import setup, find_packages

setup(
    name = "betterboids",
    description='Bird Flock Simulator',
    version = "0.1.0",
    author='James Watson',
    author_email='05watson.j@gmail.com',
    url='https://github.com/JamesDWatson',
    packages = find_packages(exclude=['*test']),
    keywords = 'simulation, flocking, boids, birds, animals',
    license='MIT',
    include_package_data = True,
    scripts = ['scripts/betterboids'],
    install_requires = ['argparse', 'pyyaml', 'matplotlib', 'numpy', 'pyrandom', 'nose']   
)