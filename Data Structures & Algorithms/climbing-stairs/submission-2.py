class Solution:
    def climbStairs(self, n: int) -> int:
        journey = []
        
        def findJourney(current, target, path):
            if current == target:
                #print("target achieved:", target)
                journey.append(path)
                return path
            #print(f"Looking at {current}, for target {target}, curr path {path}")
            if current + 1 <= target:
                #print("1 works")
                res = findJourney(current + 1, target, path + [1])
                #journey.append([1] + res)
            else:
                #print(f"overstepped, curr {current+1}, target {target}")
                pass
            if current + 2 <= target:
                #print("2 works")
                res = findJourney(current + 2, target, path + [2])
                #journey.append([2] + res) 
            else:
                #print(f"overstepped, curr {current+2}, target {target}")
                pass

            #print("working path after hop:", path)
            return path

        result = findJourney(0, n, [])
        return len(journey)
        