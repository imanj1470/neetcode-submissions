class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        finalResults = []
        def checkPath(options, resultArr, currentTarget):
            if currentTarget == 0:
                return
            
            for i, option in enumerate(options):
                workingSum = option

                if workingSum == currentTarget:
                    finalResults.append(resultArr + [option])
                    return

                if workingSum > currentTarget:
                    return
                elif workingSum < currentTarget:
                    newTarget = currentTarget - workingSum

                    res = checkPath(options[:i+1], resultArr + [option], newTarget)
            return resultArr

        checkPath(nums, [], target)
        print("FINAL RESAULTS", finalResults)
        return finalResults
