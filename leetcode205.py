class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lens = len(s)
        d = {}
        for i in range(lens):
            if s[i] not in d:
                if t[i] in d.values():
                    return False
                else: 
                    d[s[i]] = t[i]
                    
            else:
                if d[s[i]] != t[i]:
                    return False
        return True