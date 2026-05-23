class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def findRemaining(num):
            if num <= 2:
                return num
            
            if num not in cache:
                cache[num] = findRemaining(num -1) + findRemaining(num -2)
            return cache[num]
        return findRemaining(n)