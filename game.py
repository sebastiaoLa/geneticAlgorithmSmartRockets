from pyglet.gl import *
from pyglet import clock
from classes.target import Target
from classes.popControl import Population
from classes.constants import WIDTH,HEIGHT,FULLSCREEN,MAXOBSTACLES
from classes.text import Text
from classes.obstacle import Obstacle
from time import time

clock.set_fps_limit(60)

main_batch = pyglet.graphics.Batch()

window = pyglet.window.Window(width=WIDTH,height=HEIGHT,fullscreen=FULLSCREEN)

target = Target(batch=main_batch)
target.set_center((WIDTH/2,HEIGHT-int(HEIGHT*0.1)))

population = Population(batch = main_batch)

text = Text(batch = main_batch)

obstacles = [Obstacle()]

def update(dt):
    text.set_text(str(1/dt),str(population.gen),str(population.count))
    population.update()
    population.checkCollide(obstacles)
    if len(obstacles) < MAXOBSTACLES:
        if population.gen > len(obstacles):
            obstacles.append(Obstacle(obstacles))

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT) 
    main_batch.draw()
    text.draw()
    for i in obstacles:
        i.draw()
    
clock.schedule_interval(update, 1/60.0)
clock.set_fps_limit(75)

pyglet.app.run()