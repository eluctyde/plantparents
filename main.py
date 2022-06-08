from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# create a window
app = Ursina()


# create the 3D world
ground = Entity(
	model = "plane",
	texture = "grass",
	collider = "mesh",
	scale = (200, 1, 200))

Sky()

player = FirstPersonController()

class Player(Entity):
    def input(self, key):
        if key == 'w':
            self.position += self.forward

        if key == 'd':
            self.animate('rotation_y', self.rotation_y + 90, duration=.1)

        if key == 'a':
            self.animate('rotation_y', self.rotation_y - 90, duration=.1)

# start running the game
app.run()
