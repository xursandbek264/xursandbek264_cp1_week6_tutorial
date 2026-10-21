def treasure_positions(grid):
    result=[]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==1:
        result.append((row, col))
    return result
grid = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 0]
]

positions=treasure_positions
