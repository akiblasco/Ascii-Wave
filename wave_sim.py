import math
import time
import os
import platform


AMPLITUDE = 10  
WAVE_LENGTH = 20  
SPEED = 0.1  
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 20

# FPS wave
def generate_wave_frame(time_step):
    screen_buffer = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

    for x in range(SCREEN_WIDTH):
        y = int(AMPLITUDE * math.sin(2 * math.pi * (x / WAVE_LENGTH - time_step))) + SCREEN_HEIGHT // 2
        if 0 <= y < SCREEN_HEIGHT:
            screen_buffer[y][x] = '*'

    return screen_buffer

def clear_screen():
    # Clear command as per OS, there seems to be issues when running on other OS
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)

# Test
clear_screen()
for time_step in range(100):
    frame = generate_wave_frame(time_step / 10)
    clear_screen()
    for row in frame:
        print(''.join(row))
    time.sleep(SPEED)  # Adjust this for faster or slower animation

