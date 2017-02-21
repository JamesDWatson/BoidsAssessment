
#!/usr/bin/env python
from argparse import ArgumentParser
from .boids import update_boids          #Need to replace this.
from matplotlib import pyplot as plt

config=yaml.load(open("boids/config.yaml"))

def process():
    parser = ArgumentParser(description = "Generate boids movement")
    parser.add_argument('--number', action="store_true", help='Specify the number of boids for the simulation')
    arguments= parser.parse_args()
    

#    mygraph=Greengraph( arguments.start, arguments.finish)  #Find equivalent 
#    data = mygraph.green_between(arguments.steps)
    

    boid_x_pos=[random.uniform(config['x_pos_bound'][0],config['x_pos_bound'][1]) for x in range(no_boids)] 
    boid_y_pos=[random.uniform(config['y_pos_bound'][0],config['y_pos_bound'][1]) for x in range(no_boids)]
    boid_x_vel=[random.uniform(config['x_vel_bound'][0],config['x_vel_bound'][1]) for x in range(no_boids)]       
    boid_y_vel=[random.uniform(config['y_vel_bound'][0],config['y_vel_bound'][1]) for x in range(no_boids)]
    boids=(boid_x_pos,boid_y_pos,boid_x_vel,boid_y_vel) 
    
    figure=plt.figure()
    axes=plt.axes(xlim=(config['x_lim'][0],config['x_lim'][1]), ylim=(config['y_lim'][0],config['y_lim'][1]))
    scatter=axes.scatter(boids[0],boids[1])
    
    def animate(frame):
        update_boids(boids)
        scatter.set_offsets(list(zip(boids[0],boids[1])))


    anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)   
    
    plt.show()
    

if __name__ =="__main__":
    process() 
    