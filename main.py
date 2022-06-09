from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# create a window
app = Ursina()

#improving the window
window.title = 'Plant Parents 1.0'
window.borderless = False 	# show a border
window.fullscreen = True 	# go full screen
window.fps_counter.enabled = False # don't show the FPS counter

# create the 3D world
ground = Entity(
	model = "plane",
	texture = "grass",
	collider = "mesh",
	scale = (200, 1, 200))

Sky()

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

player = FirstPersonController(z= 4)

# start running the game
app.run()