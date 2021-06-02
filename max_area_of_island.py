'''Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.


Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.


'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])
       
        def traverse(row: int, col: int) -> int:
            '''
                This Function is traverse the 4-directionally (horizontal or vertical) connected elemnets
                until the adjant elements value is 1. and change the visited elements value 1 to 0.
                returns count of elements whose adjacent elements value is 1.
               
            '''
           
            if row < 0 or col < 0 or row >= rows or col >=cols or grid[row][col] == 0:
                return 0
           
            grid[row][col] = 0
            #element + left + down + right + up
            return 1 + traverse(row-1, col) + traverse(row, col-1) + traverse(row+1, col) + traverse(row, col+1)
       
        for row,col in product(range(rows),range(cols)):
            
                if grid[row][col]: result = max(result, traverse(row, col))
        return result
        
