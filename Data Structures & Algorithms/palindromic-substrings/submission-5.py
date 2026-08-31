class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for upper in range(0, len(s)):
            for lower in range(upper, -1, -1):
                subS = s[lower:upper+1]
                if subS == subS[::-1]:
                    count += 1
        return count

        #time complexity: O(n^2) due to the nested loop - where at each index in the loop, im checking it agaisnt the substring from index 0 up to the current index.
        #space complexity: O(1) (constant) - due to the amount of additoinal memory required is not linked to the length of the input, as i am using pointers to refer to the substring, rather than storing it in mem
         #space complexity adjusted to O(n), due to now storing the substring in mem so it doesnt have to be recomputed when reversing it which adds additional performance overhead resulting in "Time limit exceeded"
