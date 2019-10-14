scale = 0.8
game_width = int(1600 * scale)
game_height = int(900 * scale)
gameover_width = 193
gameover_height = 13
game_restart_width = 36
game_restart_height = 32
BACKGROUND_COLOR = (250, 250, 250)

dino_width = 88
dino_height = 95
dion_jump_initial_speed = 1200
dino_jump_acceleration = 5000

speed_ratio = 1.0
speed = 3


def set_speed_ratio(new_ratio):
    global speed_ratio
    speed_ratio = new_ratio


def get_speed_ratio():
    return speed_ratio
