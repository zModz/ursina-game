from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#movimentos
def update():
	character.y += held_keys["w"] * time.dt * 3
	character.x -= held_keys["a"] * time.dt * 3
	character.y -= held_keys["s"] * time.dt * 3
	character.x += held_keys["d"] * time.dt * 3

	

app = Ursina()
#player = FirstPersonController();

#soren's code
character = Entity(model = 'quad', texture = 'assets/doge.png')

app.run()
