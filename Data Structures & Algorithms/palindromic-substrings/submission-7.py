class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            #odd e.g aba
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            #even e.g abba
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
                
        return count

        #time complexity: O(n^2) with n being lengtn of s due to looping through s, and the cost of each iteration is n+n (as worst case scenario having to expand pointers essentialy checking out all indexes of s). n+n concludees to o(n), but o(n * o(n)) = o(n^2)

        #spcace complexity:o(1). no additional space used which is proportinal to length of input, and all operations are o(1) constant as using pointers to point to an elements char
