# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# 0. make map of visited elements
# 1. get next unvisited node
# 2. BFS from node, mark nodes as visited
# 3. increment island count when done
# 4. go to step 1


from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if len(grid) == 0:
            return 0
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.__bfs(grid, i, j)
                    numIslands += 1
        return numIslands

    def __bfs(self, grid: list[list[str]], i, j):
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            grid[i][j] = "0"
            # left
            if j - 1 >= 0 and grid[i][j - 1] == "1":
                queue.append((i, j - 1))
            # top
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                queue.append((i - 1, j))
            # right
            if j + 1 < len(grid[i]) and grid[i][j + 1] == "1":
                queue.append((i, j + 1))
            # bottom
            if i + 1 < len(grid) and grid[i + 1][j] == "1":
                queue.append((i + 1, j))
