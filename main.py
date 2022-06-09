from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# check for these events on each game loop
def update():
	# quit game if q is pressed:
	if held_keys['q']:
		app.quit()
	

# create a window
app = Ursina()

# improving the window
window.title = 'Plant Parents 1.0'
window.fullscreen = True 	# go full screen
window.fps_counter.enabled = False # don't show the FPS counter

# create the 3D world
ground = Entity(
	model = "plane",
	texture = "grass",
	collider = "mesh",
	scale = (200, 1, 200))

# the sky
Sky()

# player moves with w,d,a,s
class Player(Entity):
    def input(self, key):
        if key == 'w':
            self.position += self.forward

        if key == 'd':
            self.animate('rotation_y', self.rotation_y + 90, duration=.1)

        if key == 'a':
            self.animate('rotation_y', self.rotation_y - 90, duration=.1)

# Load tree
Tree_Model = Entity(
	model = "assets/tree2.obj",
	collider = "mesh",
	scale = 1)

# spawn player away from tree 
player = FirstPersonController(z= 4)

# start running the game
app.run()