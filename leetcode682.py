"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.
"""


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = []
        for op in ops:
            # the part that tricked me was checking negative numbers.
            # actually we only want to check if the string contains digits, if it does,
            # then we can pass it to int()
            # or we can leave it to the "else" condition to avoid checking.
            if op.lstrip("-").isdigit():
                result.append(int(op))
            elif op == "C":
                result.pop()
            elif op == "D":
                result.append(result[-1] * 2)
            elif op == "+":
                result.append(result[-1] + result[-2])
        return sum(result)

