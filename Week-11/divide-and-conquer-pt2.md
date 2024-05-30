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

Some observations:

1. Every point in MS of the whole is in Left MS or Right MS
2. Every point in Right MS is in MS of whole
3. Every point in Left MS is either in MS of whole or dominated by p, in which case, p is the left most point in Right MS.

Then, our conquer step would be:

1. Find the leftmost point $p$ in right MS
2. Compare every point $q$ in the Left MS to this point - If q.y > p.y, add q to the merged MS
3. Add every point in right MS to the Merged MS

Base case:
A set containing a single point

### Maxima-set: Analysis

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/mset.png" width="350" height="auto">
</p>

## Integer Multiplication

Given: two n-digit integers x and y

Problem: compute the product x y

### Naive approach

Assume that two digits can be multiplied or added in constant time. We perform O(n^2) operations to compute the product.

### Divide and conquer

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/mult.png" width="350" height="auto">
</p>

We can compute the product of two n-digit numbers by making 4 recursive calls on n/2 digit numbers and then combining the solutions to the subproblems.

### Implementation

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/muimp.png" width="350" height="auto">
</p>

## Master Theorem

Let f(n) and T(n) be defined as follows:
T(n) =
Case 1: aT(n/b) + f(n) if n >= d
Case 2: c if n < d

Depending on a, b and f(n), the recurrence solves to one of three cases:

1. if $f(n) = O(n^{log_{b}a-\epsilon})$ for $\epsilon > 0$, then $T(n) = \Theta(n^{log_{b}a})$ (this just means, that if c is less than the log value, then the overall time complexity takes the dominant log value)
2. if $f(n) = \Theta(n^{log_{b}a}log^{k}n)$, for $k \ge 0$ then $T(n) = \Theta(n^{log_{b}a} log^{k+1}n)$. (this just means, if f(n) is some multiple of logn, then the time complexity is the log value to the power of k + 1)
3. if $f(n) = \Omega(n^{log_{b}a+\epsilon})$ and $\epsilon > 0$ then $T(n) = \Theta(f(n))$ (this just means, if c is greater than the log value, then the overall time complexity takes the dominant c value)

$8T(n/2) + n^2$

$$
a = 8
b = 2
f(n) = n^2
log_{b}a = log_{2}8 = 3
f(n) = n^2
$$

$\text{if the } log_{b}a \text{ value is greater than } f(n) \text{ then it is case 1}$

\[ T(n) = aT\left(\frac{n}{b}\right) + f(n) \]

In your case:

- \( a = 2 \)
- \( b = 2 \)
- \( f(n) = O(n) \)

The Master Theorem provides three cases for solving such recurrences:

1. **Case 1**: If \( f(n) = O(n^c) \) where \( c < \log_b a \)
2. **Case 2**: If \( f(n) = O(n^c) \) where \( c = \log_b a \)
3. **Case 3**: If \( f(n) = O(n^c) \) where \( c > \log_b a \)

### Step 1: Compute \( \log_b a \)

Here, \( a = 2 \) and \( b = 2 \):

\[
\log_b a = \log_2 2 = 1
\]

### Step 2: Compare \( f(n) \) with \( n^{\log_b a} \)

In this case, \( f(n) = O(n) \), which is equivalent to \( n^1 \).

Thus, we compare \( n^1 \) with \( n^{\log_2 2} = n^1 \):

\[
f(n) = O(n) \implies f(n) = O(n^1)
\]

Since \( f(n) = O(n^1) \) and \( \log_b a = 1 \), we fall into **Case 2** of the Master Theorem.

### Step 3: Apply Case 2 of the Master Theorem

**Case 2** states that if \( f(n) = \Theta(n^{\log_b a}) \), then:

\[
T(n) = \Theta(n^{\log_b a} \log n)
\]

Since \( \log_b a = 1 \):

\[
T(n) = \Theta(n^1 \log n) = \Theta(n \log n)
\]

### Conclusion

Therefore, the solution to the recurrence relation \( T(n) = 2T(n/2) + O(n) \) using the Master Theorem is:

\[
T(n) = \Theta(n \log n)
\]

Let's solve the recurrence relation \( T(n) = 2T(n/2) + n \log n \) using the Master Theorem.

### Step 1: Identify the parameters

The recurrence relation is of the form:
\[ T(n) = aT\left(\frac{n}{b}\right) + f(n) \]

For this recurrence:

- \( a = 2 \)
- \( b = 2 \)
- \( f(n) = n \log n \)

### Step 2: Compute \( \log_b a \)

\[
\log_b a = \log_2 2 = 1
\]

### Step 3: Compare \( f(n) \) with \( n^{\log_b a} \)

Here, \( f(n) = n \log n \) and \( n^{\log_b a} = n^1 = n \).

We need to compare \( f(n) = n \log n \) with \( n \).

### Step 4: Determine which case of the Master Theorem applies

- **Case 1**: If \( f(n) = O(n^c) \) where \( c < \log_b a \)
- **Case 2**: If \( f(n) = \Theta(n^{\log_b a}) \)
- **Case 3**: If \( f(n) = \Omega(n^c) \) where \( c > \log_b a \)

Let's see which case applies:

1. **Case 1**: If \( f(n) = O(n^c) \) where \( c < \log_b a \)

   Here, \( f(n) = n \log n \) and \( \log_b a = 1 \). Since \( n \log n \) grows faster than \( n \), this case does not apply.

2. **Case 2**: If \( f(n) = \Theta(n^{\log_b a}) \)

   Here, \( f(n) = n \log n \) and \( n^{\log_b a} = n \). Since \( n \log n \) grows faster than \( n \), this case does not apply either.

3. **Case 3**: If \( f(n) = \Omega(n^c) \) where \( c > \log_b a \)

   Here, \( f(n) = n \log n \) and \( n^{\log_b a} = n \). Since \( n \log n \) grows faster than \( n \), this falls under Case 3.

### Case 3 of the Master Theorem states:

If \( f(n) = \Omega(n^c) \) where \( c > \log_b a \), and if \( af(n/b) \leq kf(n) \) for some \( k < 1 \) and sufficiently large \( n \), then:
\[
T(n) = \Theta(f(n)) = \Theta(n \log n)
\]

### Verification of Regularity Condition

The regularity condition requires:
\[
af(n/b) \leq kf(n)
\]

Here:
\[
2 \cdot \frac{n}{2} \log \left(\frac{n}{2}\right) \leq k \cdot n \log n
\]

Simplifying the left side:
\[
n \log \left(\frac{n}{2}\right) = n \log n - n \log 2 = n \log n - n
\]

So we need:
\[
n \log n - n \leq k n \log n
\]

For large \( n \), this holds if \( k \) is chosen appropriately (e.g., \( k = 1 \)).

### Conclusion

The solution to the recurrence relation \( T(n) = 2T(n/2) + n \log n \) is:
\[
T(n) = \Theta(n \log n)
\]

Thus, this recurrence relation falls into **Case 2** of the Master Theorem as well.

## Selection

Given an unsorted array A holding n numbers and an integer k, find the kth smallest number in A.

Our trivial solution is to sort the elements and return the kth element.

Can we do better than $O(nlogn)$? We can, with divide and conquer.

### Algorithm Description:

1. Find median of array, [n/2], and split the array into numbers which are less than A[n/2] and larger than A[n/2]. Note these sub-arrays are still unsorted, however, they are split by the median.
2. If k is <= to n/2 (index of median), then we will recursively find the element on the half with the smaller numbers. If k is > to n/2, then we will recursively find the element on the half with the larger numbers.
3. Return value of recursive calls

### Selection Time Complexity

Divide step (find median and split) takes at least $O(n)$ time.
Recur step (solve left or right subproblem) takes $T(n/2)$.
Conquer (return recursive result) takes $O(1)$.

If we could compute the median in $O(n)$ time, then the time complexity would be $T(n) = T(n/2) + O(n)$ for $n>1$, and $O(1)$ for $n = 1$.

### Approximating the median

We don't need the exact median - suppose we could find in $O(n)$ time, an element $x$ in $A$ such that:

$$
|A| / 3 \leq rank(A, x) \le 2|A| / 3
$$

Then we get the recurrence:

$$
T(n) = \\
\text{case 1: } T(2n/3) + O(n) \text{ for } n > 1 \\
\text{case 2: } O(1) \text{ for } n = 1
$$

This solves to $T(n) + O(n)$.
