# Divide and Conquer Part 2

Recap:
Algorithm design technique.

Follows three steps:

1. Divide: If it is a base case, solve directly, or break up problem into several parts.
2. Recur: Recursively solve each part/sub-problem
3. Conquer: Combine solutions of each part into overall solution

## Maxima-Set (Pareto Frontier)

Definition: A point is a maximum in a set if all other points in the set have either a smaller x-or smaller y-coordinate.

Problem: Given a set S of n distinct points in the plane (2D), find the set of all maximum points.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/ms.png" width="350" height="auto">
</p>

### Naive Solution

The idea is to check every point, one at a time, to see if it a maximum point in the set S.

To check if point p is a maximum point in S, we compare it against every other point:

```python
for q in S:
    if q != p and q.x >= p.x and q.y >= p.y:
        return "No"
return "Yes"
```

### Divide and Conquer Solution

Preprocessing: Sort the points by increasing x coordinate and store them in array. We only do this once. Break ties in x by sorting by increasing y coordinate.

Divide: divide sorted array into two halves

Recur: Recursively find the Maxima Set of each half

Conquer: computer the Maxima Set of the union of the Left and Right MS

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/lr.png" width="350" height="auto">
</p>

We can see that E and F are in the maxima set of the Left set. However, they would not be in the maxima set in the union of the left and right maxima set. What we do, is we take the left most point in the right maxima set, and see which points in the left maxima set it contains.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/maxi.png" width="350" height="auto">
</p>
