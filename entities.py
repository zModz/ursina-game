from ursina import *
from ursina import collider
from ursina import texture

## Static Entities
# Sky
Sky = Entity(
    model = "quad",
    scale = (13, 6),
    texture = "assets/skybox.png",
    z = 1
)

## Dynamic Entities


# Platforms
PlatformGround = Entity(
	model = "quad",
	position = (0, -2),
	scale = (10, 1),
	collider = "box",
	color = color.yellow
)

PlatformLevel = Entity(
	model = "quad",
	position = (2, 0),
	scale = (3, 1),
	collider = "box",
	color = color.red
)

PlatformCeiling = Entity(
	model = "quad",
	position = (-2.5, 1),
	scale = (3, 1),
	collider = "box",
	color = color.cyan
)
    

#   wall = Entity(
#   	model = "quad",
#   	x = 5.5,
#   	scale = (1, 5),
#   	collider = "box",
#   	color = color.azure
#   )