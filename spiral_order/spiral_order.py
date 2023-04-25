class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        dirs = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 0),  # up
        ]
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for j in range(n)] for i in range(m)]
        i = 0
        j = -1
        idx = 0
        values = []
        while len(values) < m * n:
            # try to go in dir
            i += dirs[idx][0]
            j += dirs[idx][1]
            if (
                i in range(0, len(matrix))
                and j in range(0, len(matrix[i]))
                and not visited[i][j]
            ):
                values.append(matrix[i][j])
                visited[i][j] = True
            # switch to new dir
            else:
                i -= dirs[idx][0]
                j -= dirs[idx][1]
                idx = (idx + 1) % len(dirs)
        return values
