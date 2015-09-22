import dice
import string
import random
import rooms

""" This module creates, tracks, and handles all the objects
in the game. This could by anything that's not a room, including
the player, the items, and an object for the game itself.
Objects will house 'attributes' that will serve as the
variables and controls for much of the work of the game.s
"""

def id_generator(size=7, chars=string.ascii_uppercase + string.digits):
    """Generates a seven string ID of uppercase characters and integers
    unless given the arguments 1) the length 2) characters to choose from
    in generation. h/t to the internet.
    """
    return ''.join(random.choice(chars) for _ in range(size))

"""I understand that globals are no longer in fashion.
If there is a better way to do this please get at me.
This is a master dictionary of all rooms created.
"""
OBJECTS_MASTER_DICT = {}
SKILLS_MASTER_DICT = {
    'athletics': False,
    'alchemy': False,
    'awareness': False,
    'barter': False,
    'block': False,
    'dodge': False,
    'heal': False,
    'marksman': False,
    'melee': False,
    'operate vehicle': False,
    'repair': False,
    'ride': False,
    'sense motive': False,
    'sleight of hand': False,
    'sneak': False,
    'speech': False,
    'survival': False,
    'traps': False,
    'unarmed': False
    }

class Object:
    """ This class represents an in game object This is anything that's
    not a room, ranging from the player, to items, and more.
    """

    def __init__(self, alias, desc, inroom=False, visible=True, hasinv=False):
        """Creates object with a unique ID, alias, description,
        whether or not it has a inroom description and if it is
        visible.
        """
        self.id = id_generator()
        self.alias = alias
        self.desc = desc
        self.in_room = inroom
        self.visible = visible
        self.current_room = None
        if hasinv is True:
            self.inv = []
        self.skill_interact = SKILLS_MASTER_DICT
        OBJECTS_MASTER_DICT[self.id] = self.alias

    def look_at(self):
        """Provide description of object."""
        print('You look at the %s:' % self.alias)
        print(self.desc)

    def new_skill_interaction(self, skill):
        """Add new skill interaction to object."""
        self.skill_interact[skill] = True

class Character(Object):
    """A character object."""

    def __init__(self, alias, desc, gender, inroom=False, visible=True,
                       hasinv=False, convo=False, merchant=False
                       ):
        """Creates character who's default unspeaking and not a
        merchant.
        """
        Object.__init__(self, alias, desc, inroom=False, visible=True, hasinv=False)
        self.gender = gender
        self.convo = convo
        self.merchant = merchant
        self.skills = {}
        """Create baseline level for skills."""
        for key in SKILLS_MASTER_DICT:
            self.skills[key] = 15

    def change_skill(self, skill, mod):
        """Modify character's skill."""
        self.skills[skill] += mod

    def roll_skill(self,skill):
        skill = skill
        dc = self.skills[skill]
        roll = dice.d100.roll_player()
        print('Your skill level in %s is %s.' % (skill, dc))

        
"""Copyright Patrick Morgan 2015. This program was created in an effort to learn
how to code with the Python language. You may freely use, edit, and redistribute.
"""
