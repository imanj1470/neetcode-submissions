class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hashset = {}
        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                curr = board[y][x]
                if curr not in hashset:
                    hashset[curr] = [[x,y]]
                else:
                    hashset[curr].append([x,y])

        def findNeighbours(coord: Tuple[int,int], nextLetter):
            res = []
            x=coord[0]
            y=coord[1]
            if y > 0 and board[y-1][x] == nextLetter: #up
                res.append(tuple((x,y-1)))
            if y < len(board) - 1 and board[y+1][x] == nextLetter: #down
                res.append(tuple((x,y+1)))
            if x < len(board[0]) - 1 and board[y][x+1] == nextLetter: #right
                res.append(tuple((x+1,y)))
            if x > 0 and board[y][x-1] == nextLetter: #left
                res.append(tuple((x-1,y)))
            return res

        def searchWord(coord, wordRemaining, used):
            if len(wordRemaining) < 1:
                return True
            
            nextPaths = findNeighbours(coord, wordRemaining[0])

            used.add(tuple(coord))

            for coord in nextPaths:
                if coord in used:
                    continue
                if searchWord(coord, wordRemaining[1:], used) == True:
                    return True
                else:
                    used.remove(coord)
        
        if word[0] not in hashset:
            return False
        for coord in hashset[word[0]]:
            if searchWord(coord, word[1:], {tuple(coord)}) == True:
                return True
        return False

