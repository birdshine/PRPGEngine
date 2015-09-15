"""
Dice rollers used for all random chance occurrences in the game engine.
randint from random is imported for use.
"""

from random import randint

class Die:
    """Represents a single die."""

    def __init__(self, sides=100):
        """Set the number of sides (default: 100)"""
        self.sides = sides

    def roll(self, num=1, mod=0):
        """Rolls default 1 die with a default modification 0."""
        num = num
        mod = mod
        mod_roll = []
        for i in range(1,num+1):
            roll = (randint(1,self.sides) + mod)
            if roll < 1:
                roll = 1
            mod_roll.append(roll)  
        return(mod_roll)

    def roll_player(self, num=1, mod=0):
        """Roll that reports numbers for player."""
        num = num
        mod = mod
        roll_list = []
        for i in range(1,num+1):
            roll = randint(1,self.sides)
            print('You roll a %s.' % roll)
            mod_roll = roll + mod
            if mod_roll < 1:
                mod_roll = 1
            roll_list.append(mod_roll)
            if mod > 0 or mod < 0:
                print('Total after modification: %s' % mod_roll)
        return roll_list

    def roll_sum(self, num=2, mod=0):
        """Dice roll that returns sum of all dice."""
        num = num
        mod = mod
        roll_sum = 0
        for i in range(1,num+1):
            roll = (randint(1,self.sides) + mod)
            if roll < 1:
                roll = 1
            roll_sum += roll
        return roll_sum

    def roll_sum_player(self, num=2, mod=0):
        """Dice roll that adds sum and reports for player."""
        num = num
        mod = mod
        roll_sum = 0
        for i in range(1,num+1):
            roll = randint(1,self.sides)
            print('You roll a %s.' % roll)
            new_roll = roll + mod
            if new_roll < 1:
                new_roll = 1
            roll_sum += new_roll
            if mod > 0 or mod < 0:
                print('Total after modification: %s.' % new_roll)
        print('Total: %s.' % roll_sum)
        return roll_sum

"""Define the most commonly used die."""
hundredDie = Die()
twentyDie = Die(20)
twelveDie = Die(12)
tenDie = Die(10)
eightDie = Die(8)
sixDie = Die(6)
coinDie = Die(2)

"""Copyright Patrick Morgan 2015, you may use, edit, and
distribute non-commercially.
"""
