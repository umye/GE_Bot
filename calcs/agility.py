# Agility rooftop course calculator

from calcs.experience import level_to_xp
from helpers.hiscore import Hiscore

DRAYNOR_LEVEL = 10
DRAYNOR_LAP = 120
AL_KHARID_LEVEL = 20
AL_KHARID_LAP = 180
VARROCK_LEVEL = 30
VARROCK_LAP = 238
CANIFIS_LEVEL = 40
CANIFIS_LAP = 240
FALADOR_LEVEL = 50
FALADOR_LAP = 440
SEERS_LEVEL = 60
SEERS_LAP = 570
POLLNIVEACH_LEVEL = 70
POLLNIVEACH_LAP = 890
RELLEKKA_LEVEL = 80
RELLEKKA_LAP = 780
ARDOUGNE_LEVEL = 90
ARDOUGNE_LAP = 793


class Agility(Hiscore):
    """ Agility rooftop course calculator """

    def __init__(self, username):
        super().__init__(username)

    def determine_course(self):
        """ Determines highest level course user can use and sets lap xp"""
        if self.agility_level < DRAYNOR_LEVEL:
            self.next_course = "Draynor"
            return None
        elif self.agility_level < AL_KHARID_LEVEL:
            self.lap_xp = DRAYNOR_LAP
            self.next_course = "Al Kharid"
            return "Draynor"
        elif self.agility_level < VARROCK_LEVEL:
            self.lap_xp = AL_KHARID_LAP
            self.next_course = "Varrock"
            return "Al Kharid"
        elif self.agility_level < CANIFIS_LEVEL:
            self.lap_xp = VARROCK_LAP
            self.next_course = "Canifis"
            return "Varrock"
        elif self.agility_level < FALADOR_LEVEL:
            self.lap_xp = CANIFIS_LAP
            self.next_course = "Falador"
            return "Canifis"
        elif self.agility_level < SEERS_LEVEL:
            self.lap_xp = FALADOR_LAP
            self.next_course = "Seers"
            return "Falador"
        elif self.agility_level < POLLNIVEACH_LEVEL:
            self.lap_xp = SEERS_LAP
            self.next_course = "Pollniveach"
            return "Seers"
        elif self.agility_level < RELLEKKA_LEVEL:
            self.lap_xp = POLLNIVEACH_LAP
            self.next_course = "Rellekka"
            return "Pollniveach"
        elif self.agility_level < ARDOUGNE_LEVEL:
            self.lap_xp = RELLEKKA_LAP
            self.next_course = "Ardougne"
            return "Rellekka"
        else:
            self.lap_xp = ARDOUGNE_LAP
            self.next_course = "level 99"
            return "Ardougne"

    def xp_needed_to_level_up(self):
        """ Returns the amount of xp needed to level up """
        return level_to_xp(self.agility_level + 1) - self.agility_xp

    def laps_to_level_up(self):
        """ Returns number of laps on highest available course to level up """
        return self.xp_needed_to_level_up() // self.lap_xp + 1

    def laps_to_next_course(self):
        """ Returns number of laps until user can access next course """
        if self.determine_course() == 'Draynor':
            return (level_to_xp(20) - self.agility_xp) // self.lap_xp + 1
        elif self.determine_course() == 'Al Kharid':
            return (level_to_xp(30) - self.agility_xp) // self.lap_xp + 1
        elif self.determine_course() == 'Varrock':
            return (level_to_xp(40) - self.agility_xp) // self.lap_xp + 1
        elif self.determine_course() == 'Canifis':
            return (level_to_xp(50) - self.agility_xp) // self.lap_xp + 1
        elif self.determine_course() == 'Falador':
            return (level_to_xp(60) - self.agility_xp) // self.lap_xp + 1
        elif self.determine_course() == 'Seers':
            return (level_to_xp(70) - self.agility_xp) // self.lap_xp + 1
        elif self.determine_course() == 'Pollniveach':
            return (level_to_xp(80) - self.agility_xp) // self.lap_xp + 1
        elif self.determine_course() == 'Rellekka':
            return (level_to_xp(90) - self.agility_xp) // self.lap_xp + 1
        else:
            return (level_to_xp(99) - self.agility_xp) // self.lap_xp + 1

# Ex
# 70 Agility (blah xp)
# number laps on current course to level up
# number laps to next course
