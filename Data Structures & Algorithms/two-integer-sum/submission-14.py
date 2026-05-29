class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enumeratedNums = enumerate(nums)
        sortedNums = sorted(enumeratedNums, key = lambda enumeratedNums: enumeratedNums[1])
        uniqueNumbers = set(nums)
        i=0
        j = 1
        while i < j:
            if target - sortedNums[i][1] not in uniqueNumbers: 
                i += 1
                j = i + 1

            #print("i,j", i,j)
            currentSum = sortedNums[i][1] + sortedNums[j][1]
            #print("current Sum: ", currentSum)
            if currentSum == target:
                return sorted([sortedNums[i][0], sortedNums[j][0]])
            if currentSum < target and j < len(nums)-1:
                comeBackFlag = False
                j +=1
                #print("j++")
            else: # if j hit ceiling or overstepped, come back to sensible value
                i += 1
                while sortedNums[i][1] + sortedNums[j][1] > target:
                    j -= 1
                #print("i++, j = i+1")
        return []