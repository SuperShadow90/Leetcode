"""
Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        this is a naive and slow solution.
        maybe the solution will be faster if we use java and StringBuilder?
        """
        if not s or s == "":
            return s

        words = s.strip().split(" ")
        reversed_words = []
        for word in words:
            reversed = "".join([word[i] for i in range(len(word) - 1, -1, -1)])
            reversed_words.append(reversed)
        return " ".join(reversed_words)

    def alternative(self, s):
        """
        this is an alternative pythonic solution
        It's slightly faster than the previous solution even though they use essentially the same idea.
        But this solution eliminates all verbose steps.
        """

        return " ".join(map(lambda x: x[::-1], s.split(" ")))