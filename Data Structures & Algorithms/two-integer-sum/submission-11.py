class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enumeratedNums = enumerate(nums)
        sortedNums = sorted(enumeratedNums, key = lambda enumeratedNums: enumeratedNums[1])
        print(sortedNums)
        i=0
        j = 1
        while i < j:
            #print("i,j", i,j)
            currentSum = sortedNums[i][1] + sortedNums[j][1]
            #print("current Sum: ", currentSum)
            if currentSum == target:
                return sorted([sortedNums[i][0], sortedNums[j][0]])
            if currentSum < target and j < len(nums)-1:
                j +=1
                #print("j++")
            else:
                i +=1
                j = i + 1
                #print("i++, j = i+1")
        return []