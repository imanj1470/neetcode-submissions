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
            

        