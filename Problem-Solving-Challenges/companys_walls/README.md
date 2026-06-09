# Shaparak Wall Perimeter

In this problem, a wall is made of several rows of 1×1 square bricks. For each row, a continuous range of bricks is painted.

The task is to calculate the total perimeter of the painted area.

## Input Format

The first line contains an integer `n`, representing the number of rows.

The next `n` lines each contain two integers:

```text
li ri
```
which indicate that in row i, the bricks from li to ri - 1 are painted.

## Example
 
Input:
```text
3
2 5
3 6
1 2
```
Painted bricks:
Row 1: 2, 3, 4
Row 2: 3, 4, 5
Row 3: 1

Output:
16