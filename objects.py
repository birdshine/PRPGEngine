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

    def __init__(self, alias, desc, inroom=False, visible=True):
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
        self.inv = []
        self.skill_interact = SKILLS_MASTER_DICT
        OBJECTS_MASTER_DICT[self.id] = self.alias

    def look_at(self):
        """Provide description of object."""
        if self.visible == True:
            print('You look at the %s:' % self.alias)
            print(self.desc)

    def new_skill_interaction(self, skill):
        """Add new skill interaction to object."""
        self.skill_interact[skill] = True

    def rename(self,name):
        """Rename object while maintaining original Object ID."""
        for key in OBJECTS_MASTER_DICT:
            if OBJECTS_MASTER_DICT[key] == self.alias:
                OBJECTS_MASTER_DICT[key] = name
                self.alias = name

    def redesc(self,desc):
        """Change object description."""
        self.desc = desc

    def toggle_in_room(self,new_bool):
        """Toggle whether or not object has an in room description."""
        self.in_room = new_bool

    def toggle_visibility(self,new_bool):
        """Toggles visibility."""
        self.visible = new_bool


class Item(Object):
    """An item that can be interacted with or taken into the inventory."""

    def __init__(self, alias, desc, val, interactable=True,
                     container=False, pickup=True, drop=True,
                     give=False
                     ):
        """Creates an item that can possibly interacted with or taken into the inventory
        such as equipment, food, etc."""
        Object.__init__(self, alias, desc, inroom=False, visible=True)
        self.val = val
        self.interactable = interactable
        self.container = container
        self.pick_upable = pickup
        self.dropable = drop
        self.giveable = give
        self.uses = {}

        def change_value(self,val):
            """Sets new value for the item."""
            self.val = val

        def toggle_container(self,new_bool):
            """Toggles whether or not the item is a container."""
            self.container = new_bool

        def toggle_dropable(self,new_bool):
            """Toggle whether or not the item is dropable."""
            self.dropablee = new_bool

        def toggle_pick_upable(self,new_bool):
            """Toggles whether or not the item is pick-upable."""
            self.pick_upable = new_bool

class Character(Object):
    """A character object."""

    def __init__(self, alias, desc, gender, inroom=False, visible=True,
                       convo=False, merchant=False
                       ):
        """Creates character who's default unspeaking and not a
        merchant.
        """
        Object.__init__(self, alias, desc, inroom=False, visible=True)
        self.gender = gender
        self.visible = visible
        self.in_room = inroom
        self.has_convo = convo
        self.is_merchant = merchant
        self.inv = {}
        self.equipment = {
            'head': None,
            'acc': None,
            'body': None,
            'hands': None,
            'feet': None,
            'weapon': None,
            'ring': None,
            'neck': None
            }
        self.skills = {}
        """Create baseline level for skills."""
        for key in SKILLS_MASTER_DICT:
            self.skills[key] = 15
        self.skills_counter = {}
        """Create counter for succesful skill uses."""
        for key in SKILLS_MASTER_DICT:
            self.skills_counter[key] = 0


    def change_skill(self, skill, mod):
        """Modify character's skill."""
        self.skills[skill] += mod

    def roll_skill(self,skill):
        skill = skill
        dc = self.skills[skill]
        roll = min(dice.d100.roll())
        if roll <= dc:
            self.skills_counter[skill] += 1
            if self.skills_counter[skill] >= 5:
                self.change_skill(skill,1)
                self.skills_counter[skill] = 0
            """Determine if roll was a crit, fair, or standard for things like weapons."""    
            if roll <= (dc / 5):
                return 'crit'
            elif roll <= (dc /3):
                return 'good'
            else:
                return True
        else:
            return False

    def give_item(self,item):
        """Add item to the character's inventory."""
        self.inv[item.alias] = item.desc

        
"""Copyright Patrick Morgan 2015. This program was created in an effort to learn
how to code with the Python language. You may freely use, edit, and redistribute.
"""
