# main

# solresol text editor v0.1. released 5/1/2020 (dd/mm/yyyy)
# all code by CUBE
# all stenograph images by misolsi misido, owner of the la lasiresa discord server

import math
from key_input import *
from renderer import *

# define some colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

WIDTH = 500
HEIGHT = 500
FPS = 30
BGCOLOR = WHITE

pygame.init()
pygame.midi.init()

# midi_count = pygame.midi.get_count()
# for device in range(midi_count):
#     print(pygame.midi.get_device_info(device))

# sets midi device to default midi device, if a default exists
default_midi = pygame.midi.get_default_input_id()
if default_midi < 0:
    midi_enabled = False
    pygame.midi.quit()
else:
    midi_enabled = True
    midi_input = pygame.midi.Input(default_midi)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True

RENDERER = renderer(screen)
InputProcessor = input_processor()
load_config("key_config.json")

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        # this one checks for the window being closed
        if event.type == pygame.QUIT:
            running = False
            # close out of midi stuff
            if midi_enabled:
                midi_enabled = False
                midi_input.close()
                pygame.midi.quit()
            pygame.quit()
        # add any other events here (keys, mouse, etc.)
        InputProcessor.main(event)

    if midi_enabled:
        # check midi events
        if midi_input.poll():
            midi_events = midi_input.read(1000)
            for event in midi_events:
                InputProcessor.midi(event)
                # print(pygame.midi.midi_to_ansi_note(event[0][1]))

    screen.fill(BGCOLOR)

    RENDERER.process_input(InputProcessor.getcharacter())
    RENDERER.main()
    # after drawing, flip the display
    pygame.display.flip()
