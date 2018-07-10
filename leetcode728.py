class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            divisible = True
            r = i
            while r:
                digit = r % 10
                if (digit == 0) or (i % digit != 0):
                    divisible = False
                    break
                else:
                    r = r / 10
            if divisible:
                result.append(i)
        return result