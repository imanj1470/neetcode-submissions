class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = {}
        def findSub(i: int, progress: int) -> int:
            if progress == len(t): #sol found so incrementing and returning
                return 1
            if i == len(s): #if sol found it returns above
                return 0

            if (i, progress) in mem: #if call already found
                return mem[(i, progress)]
            
            #optimisations
            if len(t) - progress > len(s) - i:
                return 0

            res = findSub(i+1, progress)            #try skip and investigate

            if s[i] == t[progress]: #add it to subarray and ivnestigate
                res += findSub(i+1, progress + 1)

            mem[(i, progress)] = res
            return mem[(i, progress)]

        return findSub(0, 0)

        #time complexity: O(n*m): reucrsive, however using memoization to store result of each unique call, with teh max amount of unique calls being n*m with them being length of s, t respectively
        #space: o(n*m) -  the additonal mem var is similar max size n*m as storinbg result of all calculations, which is max gonna be n*m times.
