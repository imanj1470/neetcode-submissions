class Solution:
    def climbStairs(self, n: int) -> int:
        solutions = []
        cache = {
        } #1: [1], 2: [[1,1],[2]]
        def findJourney(current, path, option):
            print(f"Looking at {current},  curr path {path}")
            if current == 0:
                print("target achieved:")
                solutions.append(path)
                return path

            print("current cache:", cache)
            if current in cache:
                print("usigng cache:", cache[current])
                return cache[current] #distance to find

            if current - option >= 0 and option == 2:
                workingNum = current - option
                key = sum(path) + option
                print(option, " works")
                res1 = findJourney(workingNum, path + [option] , 1)
                res2 = findJourney(workingNum, path + [option] , 2)

                cache[key] = [res1] + [res2]
                print(f"added to cahce key {key} = {cache[key]}")

            if current - option >= 0 and option == 1:
                workingNum = current - option
                key = sum(path) + option

                print(option," works")
                res = findJourney(workingNum,  path + [option], 1)

                cache[key] = res
                print(f"added to cahce key {key} = {cache[key]}")

            print("working path after hop:", path)
            return path

        result = findJourney(n, [], 2)
        print("result:",solutions)
        return len(solutions)
        