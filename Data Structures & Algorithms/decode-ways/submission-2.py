class Solution:
    def numDecodings(self, s: str) -> int:
        #could use hashset and use not in for quicker, so less casting

        mem = {}

        def decode(inp) -> int:
            if len(inp) == 0:
                return 1
            if inp == '0':
                return 0

            if inp in mem:
                return mem[inp]

            countA, countB = 0, 0
            if int(inp[0]) > 0 and int(inp[0]) <= 26:
                countA = decode(inp[1:])

            if len(inp) > 1 and int(inp[0]) > 0 and int(inp[0:2]) <= 26:
                countB = decode(inp[2:])

            mem[inp] = countA + countB
            return countA + countB
  
        if s != '0':
            return decode(s)
        else:
            return 0

        #time complexity: O(n) with n being length of s, would be o(2^n) as 2 differnet branching paths, however using memoization to store the result of substring, and the combinations are reducing by 1 or 2 chars at the begninnigng, so the first branch checking first char only after 2 paths deep would meet the branch which is checking the first 2 chars, hence maximum would iterate through the substring once

        #space complexity: o(n) with n as length of s - only 1 root to leaf branch is stored in mem  at any point during the recursion, and mem has max n items
            

        