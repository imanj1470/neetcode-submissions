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
            
            res = findSub(i+1, progress)            #try skip and investigate

            if s[i] == t[progress]: #add it to subarray and ivnestigate
                res += findSub(i+1, progress + 1)

            mem[(i, progress)] = res
            return mem[(i, progress)]

        return findSub(0, 0)

        #time complexity: O(2^n): using recurision where at each path has 2 branches to consider, however this is slightly optimised with memoization as repeat calls won't be made due to result being stored in a dictionary, howwever worst case scenario still results in all paths being searched with O(n*m) with n being size of s and m being size of t o(n^2), but as o(2^n) is larger this is the stated answer
        #space: o(n^2) - - as only 1 root to leaf is stored iin memory from recursion at a point, wiuth mem being of size len input s * len input t 
