# Statement

You’re given an **(m×n)** matrix where each cell of the matrix can have one of three values:

    00 represents an empty cell

    11 represents a fresh orange

    22 represents a rotten orange

Every minute, an orange becomes rotten if it’s adjacent to a rotten orange in any direction. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Constraints:

    m==m== grid.length

    n==n== grid[i].length

    1≤m1≤m, n≤10n≤10

    grid[i][j] is 00, 11, or 22.
