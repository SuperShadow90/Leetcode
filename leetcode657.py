"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string.
And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.
"""


from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = Counter(moves)
        if c['L'] == c['R'] and c['U'] == c['D']:
            return True
        else:
            return False

    def alternative(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U':
                x += 1
            elif move == 'D':
                x -= 1
            elif move == 'L':
                y += 1
            elif move == 'R':
                y -= 1
        return x == y == 0