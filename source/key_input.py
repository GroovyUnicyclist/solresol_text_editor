# key_input

# solresol text editor v0.1. released 5/1/2020 (dd/mm/yyyy)
# base code and keyboard support by CUBE
# midi support by GroovyUnicyclist
# all stenograph images by misolsi misido, owner of the la lasiresa discord server

import pygame
import pygame.midi
import constants as c
import json

class input_processor:
    def __init__(self):
        self.character = ""

    def main(self, event):
        tempchar = ""
        if event.type == pygame.KEYDOWN:
            if event.key in c.inputmap:
                tempchar = c.inputmap[event.key]
            pygame.time.delay(150)

        if tempchar == self.character:
            self.character = ""
        else:
            self.character = tempchar

    def midi(self, event):
        tempchar = ""
        # checks if the midi event is a note on event from any of the channels (1-16 corresponds to 144-159)
        if 144 <= event[0][0] <= 159:
            note = event[0][1]
            # print (event)
            if note in c.midiinputmap:
                tempchar = c.midiinputmap[note]
            pygame.time.delay(150)

        if tempchar == self.character:
            self.character = ""
        else:
            self.character = tempchar

    def getcharacter(self):
        return self.character

def load_config(filname):
    data = json.load(open(filname))

    for key in c.allinputs:
        keycode = c.pygame_key_map[data["keyboard"][key]]
        midicode = c.midi_key_map[data["midi"][key]]
        value = c.inputmap[key]
        del c.inputmap[key]
        del c.midiinputmap[key]
        c.inputmap[keycode] = value
        c.midiinputmap[midicode] = value
