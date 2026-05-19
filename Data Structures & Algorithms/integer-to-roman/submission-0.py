class Solution:
    def intToRoman(self, num: int) -> str:
        romanValMap = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
   
        def findClosestRomanInt(inp):
            inp = int(inp)
            keys = list(romanValMap)
            closestDistance = abs(inp - keys[-1]) #largest
            closestKey = keys[-1]
            realDistance = closestDistance
            for i in range(0, len(romanValMap)):
                distance = inp - keys[i]
                if abs(distance) < closestDistance:
                    realDistance = distance
                    closestKey = keys[i]
                    closestDistance = abs(distance)
            print(inp," closest =", romanValMap[closestKey], "at distance", realDistance)
            
            distToReturn = distance
            if inp < 0:
                distToReturn = abs(realDistance)*-1
            else:
                distToReturn = realDistance
            
            return closestKey, distToReturn
    
        def listToString(l):
            return "".join(l)
        def convert(inp): #returns array of roman chars
            if int(inp) == 0:
                return
            chunks = splitInt(inp)
            result = []
            print("Working on ", chunks)
            for chunk in chunks:
                segment = ""
                distance = chunk
                print("current chuhnk", chunk)
                while True:
                    key, distance = findClosestRomanInt(distance)
                    print("working distance", distance)
                    segment += romanValMap[key]

                    if distance == 0:
                        print("distance 0, returning")
                        break
                    elif distance > 0:
                        res = convert(abs(distance))
                        print("suffixing", res)
                        segment += listToString(res)
                        break
                    elif distance < 0:
                        res = convert(abs(distance))
                        print("prefixing", res)
                        segment = listToString(res) + segment
                        break
                print("adding", segment,"for", inp)
                result += segment
            return result

        
        def splitInt(inp):
            res = []
            inpString = str(inp)
            for i in range(0, len(inpString)):
                part = inpString[i] + "0"*(len(inpString)-i-1)
                if int(part) != 0:
                    res.append(part)
            return res    
        
            
        return listToString(convert(num))
        