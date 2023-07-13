from collections import deque
def min_minutes_to_rot(grid):
    fresh_oranges = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fresh_oranges += 1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                queue = deque([(r, c, 0)])
                visited = set()               
                
                while queue:
                    r, c, minutes = queue.popleft()
                    pos = r,c                    
                    deltas = [(1,0), (0,1), (-1, 0), (0, -1)]
                    for delta in deltas:
                        delta_row, delta_col = delta
                        neighbor_row = delta_row + r
                        neighbor_col = delta_col + c
                        neighbor_pos = neighbor_row, neighbor_col
                        col_inbounds = 0 <= neighbor_col < len(grid)
                        row_inbounds = 0 <= neighbor_row < len(grid[0])
                        if col_inbounds and row_inbounds and grid[neighbor_row][neighbor_col] == 1 and neighbor_pos not in visited:
                            visited.add(neighbor_pos)
                            queue.append((neighbor_row, neighbor_col, minutes + 1))
                if len(visited) == fresh_oranges:
                    return minutes                
            continue
    
    return -1
