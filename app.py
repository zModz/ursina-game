from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#movimentos
def update():
	character.y += held_keys["w"] * time.dt * 3
	character.x -= held_keys["a"] * time.dt * 3
	character.y -= held_keys["s"] * time.dt * 3
	character.x += held_keys["d"] * time.dt * 3


def update():
	enemy.y += held_keys["i"] * time.dt * 3
	enemy.x -= held_keys["j"] * time.dt * 3
	enemy.y -= held_keys["k"] * time.dt * 3
	enemy.x += held_keys["l"] * time.dt * 3
	


app = Ursina()
#player = FirstPersonController();

#objects
character = Entity(model = 'quad', texture = 'assets/doge.png', collider='box', Z = 2) 

enemy =  Entity(model = 'quad', texture = 'assets/Pedobear.png', collider='box', Z = 1)

app.run()
