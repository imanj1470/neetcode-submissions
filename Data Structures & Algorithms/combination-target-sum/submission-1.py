class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        print([0,1,2][:1])

        finalResults = []
        def checkPath(options, resultArr, currentTarget):
            if currentTarget == 0:
                #print("target achieved (0)")
                return
            

            #print(f"LOOKING AT OPTIONS: {options}. TARGET:{currentTarget}, current res {resultArr}")
            for i, option in enumerate(options): #bug: each iteration adds onto the sum, when it shouldnt
                workingSum = option
                
                ''' print(
                    f"working option {option}, working sum{workingSum}, for target {currentTarget}, curr array {resultArr}"
                ) '''
                if workingSum == currentTarget:
                    finalResults.append(resultArr + [option])
                    #print("solution found", finalResults[0])
                    return

                if workingSum > currentTarget:  # all options to right are greater
                    #print("all options to right are greater, skipping")
                    return
                elif workingSum < currentTarget:
                    newTarget = currentTarget - workingSum
                    ''' print(
                        "new branch, viable path^, digging into",
                        options[: i + 1],
                        "with a new target",
                        newTarget,
                    ) '''
                    
                    res = checkPath(options[:i+1], resultArr + [option], newTarget)
            return resultArr

        checkPath(nums, [], target)
        print("FINAL RESAULTS", finalResults)
        return finalResults
