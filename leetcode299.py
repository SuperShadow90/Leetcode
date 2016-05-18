class Solution(object):
    def getHint(self, secret, guess):
        a, b = 0, 0
        d = {}
        for digit in secret:
            if digit not in d:
                d[digit] = 1
            else:
            d[digit] += 1
        for digit in guess:
            if d[digit] > 0:
                b += 1
                d[digit] -= 1
        length = len(secret)
        for i in range(length):
            if secret[i] == guess[i]:
                a += 1
                b -= 1
        return "{0}A{1}B".format(a, b)
