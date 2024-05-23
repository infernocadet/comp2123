# Divide and Conquer

**Divide and Conquer** algorithms can normally be broken into three parts:

1. **Divide**: If it is a base case, solve directly, otherwise break up the problem into several parts
2. **Recur/Delegate**: Recursively solve each part (each sub-problem)
3. **Conquer**: Combine the solutions of each part into the overall solution.

## Divide

If it is a base case, solve directly.

Typical base case: Subproblem of constant size, usually 0 or 1 elements, for which you can compute the solution explicitly.

Otherwise, we will break the problem up into different subproblems - several parts.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/div.png" width="350" height="auto">
</p>

## Recur / Delegate

We then recursively solve each part, each sub-problem. The sub-problems are solved by the Recursion Fairy, similar to induction hypothesis, so we don't have to worry about them. We just assume that a solution will be given to us.

## Conquer

We then merge all the solutions together.

## Searching A Sorted Array

Given: A sorted sequence $S$ of $n$ numbers, stored in an array.
Problem: Given a number $x$, is $x$ in $S$?

### Binary Search Pseudocode

```
def binary_search(A, left, right, x)

if left = right:
    return unsuccessful

mid = (left + right) / 2
if x < A[mid]:
    return binary_search(A, left, mid, x)
else if x > A[mid]:
    return binary_search(A, mid + 1, right, x)
else:
    return mid
```

### Binary Search Correctness

**Invariant**: If x is in A before the divide step, then x is in A after the divide step.

- if A[n/2] > x, then x must be in A[0 to n/2-1]
- if A[n/2] < x, then x must be in A[n/2+1 to n-1]

## Recurrence formula

An easy way to analyse the time complexity of a divide-and-conquer algorithm is to define and solve a recurrence

Let $T(n)$ be the running time of the algorithm, we need to find out:

- Divide step cost in terms of n
- Recur step(s) cost in terms of T(smaller values)
- Conquer step const in terms of n

Together with information about the base case, we can set up a recurrence for $T(n)$ and solve it.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/tn.png" width="350" height="auto">
</p>

### Binary Search on an array complexity analysis

**Divide step**: (find middle and compare to x): $O(1)$
**Recur step**: (solve left or right subproblem): $T(n/2)$
**Conquer step**: (return answer from recur step): $O(1)$

Now we set up the recurrence for $T(n)$:
\[
T(n) =
\begin{cases}
T(n/2) + O(1) & \text{for } n > 1 \\
O(1) & \text{for } n = 1
\end{cases}
\]

This solves to \[T(n) = O(\log n)\] as we can only halve the input $O(logn)$ times before reaching a base case.

## Proof by Unrolling

For **$T(n) = T(n/2) + O(1)$**,

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/unroll.png" width="350" height="auto">
</p>

### Binary search on a linked list complexity analysis

**Divide step**: (find middle and compare to x): $O(n)$
**Recur step**: (solve left or right subproblem): $T(n/2)$
**Conquer step**: (return answer from recur step): $O(1)$

We can now set up the recurrence for $T(n)$:

\[
T(n) =
\begin{cases}
T(n/2) + O(n) & \text{for } n > 1 \\
O(1) & \text{for } n = 1
\end{cases}
\]

This solves to $T(n) = O(n)$ since to access the next index, we end up with n/2 + n/4 + n/8
