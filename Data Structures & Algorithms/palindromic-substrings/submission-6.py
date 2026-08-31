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

