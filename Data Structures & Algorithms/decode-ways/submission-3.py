class Solution:
    def numDecodings(self, s: str) -> int:
        #could use hashset and use not in for quicker, so less casting

        mem = [-1] * len(s) #is it len+1?

        def decode(i: int) -> int:
            if len(s) <= i:
                return 1
            if s[i] == '0':
                return 0

            if mem[i] != -1:
                return mem[i]

            countA, countB = 0, 0
            if int(s[i]) > 0 and int(s[i]) <= 26:
                countA = decode(i+1)

            if i < len(s) - 1 and int(s[i]) != 0 and int(s[i] + s[i+1]) <= 26:
                countB = decode(i+2)

            mem[i] = countA + countB
            return countA + countB
  
        if s != '0':
            return decode(0)
        else:
            return 0

        #time complexity: O(n) with n being length of s, would be o(2^n) as 2 differnet branching paths, however using memoization to store the result of substring, and the combinations are reducing by 1 or 2 chars at the begninnigng, so the first branch checking first char only after 2 paths deep would meet the branch which is checking the first 2 chars, hence maximum would iterate through the substring once

        #space complexity: o(n) with n as length of s - only 1 root to leaf branch is stored in mem  at any point during the recursion, and mem has max n items
            

        