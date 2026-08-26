class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = {}
        unique = sorted(set(nums))
        result = []

        def findSolutions(target, current, i):
            if target < 0:
                return None
            if target == 0:
                result.append(current)
                return

            for i in range(i, len(unique)):
                res = target - unique[i]
                if res in solutions:
                    continue
                
                elif res < 0:
                    break
                
                findSolutions(res, current + [unique[i]], i)
                

        findSolutions(target, [], 0)

        return result