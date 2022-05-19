# Imports
from ursina import *
import entities as Entities
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

# Variables
points = 0


# Start
app = Ursina()
# Window control
# window.fullscreen = True

# Player
Player = PlatformerController2d(
    position = (0, 1, 0.01),
    gravity = 0.5, 
    jump_height = 2, 
    jump_duration = 0.2
)

# World
world_size = 10
for w in range(world_size):
	duplicate(Entities.Sky, x = 13 * (w + 1))
	duplicate(Entities.Sky, x = -13 * (w + 1))
	duplicate(Entities.PlatformGround, x = 10 * (w + 1))
	duplicate(Entities.PlatformGround, x = -10 * (w + 1))

camera.add_script(SmoothFollow(target = Player, offset = [0, 1, -30], speed = 4))

# Game Loop
def update():
    if Player.intersects(Entities.InteractCoin).hit:
        print("Player collected a coin!")
        Entities.InteractCoin.visible = False
        Entities.InteractCoin.collider = "none"
        
        uiString = "Points = " + str(points)
        Entities.uiPoints.text = uiString


#End
app.run()