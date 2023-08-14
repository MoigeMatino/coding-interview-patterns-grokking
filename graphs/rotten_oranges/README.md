# Statement

You’re given an **(m×n)** matrix where each cell of the matrix can have one of three values:

    0 represents an empty cell

    1 represents a fresh orange

    2 represents a rotten orange

Every minute, an orange becomes rotten if it’s adjacent to a rotten orange in any direction. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Constraints:

    m= grid.length

    n= grid[i].length

    1≤m1≤m, n≤10n≤10

    grid[i][j] is 0, 1, or 2.
