# High alch calculator

from calcs.experience import LEVEL_99, level_to_xp, xp_to_level
from helpers.ge import GrandExchange
from helpers.hiscore import Hiscore

HIGH_ALCH_XP = 65
ALCHS_PER_HR = 1200


class Alchemy(Hiscore, GrandExchange):
    """ High alch calculator """

    def __init__(self, username):
        self.username = username

    async def fetch(self):
        """ Fetch the results """
        Hiscore.__init__(self, self.username)
        GrandExchange.__init__(self, "Nature rune")
        await Hiscore.fetch(self)
        await GrandExchange.fetch(self)

    def alchs_to_level_up(self):
        """ Returns number of alchs needed to level up """
        needed = level_to_xp(xp_to_level(self.magic_xp) + 1) - self.magic_xp
        return (needed // HIGH_ALCH_XP) + 1

    def price_to_level_up(self):
        """ Returns gp needed to level up """
        return self.current_price * self.alchs_to_level_up()

    def time_to_level_up(self):
        """ Returns time to level up in hours """
        return self.alchs_to_level_up() / ALCHS_PER_HR

    def alchs_to_level_99(self):
        """ Returns number of alchs needed for level 99 """
        needed = LEVEL_99 - self.magic_xp
        return (needed // HIGH_ALCH_XP) + 1

    def price_to_level_99(self):
        """ Returns gp needed to level up """
        return self.current_price * self.alchs_to_level_99()

    def time_to_level_99(self):
        """ Returns time to level up in hours """
        return self.alchs_to_level_99() / ALCHS_PER_HR
