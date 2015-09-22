import dice
import string
import random

"""This module creates, tracks, and reports rooms. Everything in 
the engine that's not a room is an object.
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
ROOMS_MASTER_DICT = {'1234567': 'a premade test room'}
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

class Room:
    """Represents a game room.
    Contains dictionaries for exits and contents that are
    not defined at initialize.
    """
    
    def __init__(self, alias, desc):
        """Create room alias and descripion. Id is auto generated.
        Exits and contents will have to be defined with functions.
        """
        rooms_list = []
        self.id = id_generator()
        self.alias = alias
        self.desc = desc
        """Possible self.exits: Up,down,in,out,se,s,sw,w,nw,n,ne,e."""
        self.exits = {}
        self.contents = {'player': 'you'}
        self.skill_interaction = SKILLS_MASTER_DICT
        ROOMS_MASTER_DICT[self.id] = self.alias

    def new_exit(self, direction, alias, locked=False):
        """Creates a new exit within room."""
        self.exits[direction] = [alias,locked]

    def new_skill_interaction(self, skill, dc):
        """Creates a new skill interaction."""
        self.skill_interaction[skill] = [True, dc]

    def look(self):
        "Player looks about the room."
        print('You are in %s.' % self.alias)
        print('')
        print('There are exits to the -')
        exit_search = 0    # Set exit_search variable and search for exits.
        for x in self.exits:
            if self.exits[x] is not None:
                print('%s - %s' % (x, self.exits[x][0]))
                if self.exits[x][1] is True:
                    print('(This exit is locked.)')
                exit_search += 1
        if exit_search == 0:    # There were no additions to exit_search.
            print('There are no exits.')

"""Copyright Patrick Morgan 2015. This program was developed in an effort
to learn to code the Python language. You may freely use, edit, and
distribute.
"""
