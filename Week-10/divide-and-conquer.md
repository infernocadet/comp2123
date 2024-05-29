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

$$
T(n) =
\begin{cases}
T(n/2) + O(1) & \text{for } n > 1 \\
O(1) & \text{for } n = 1
\end{cases}
$$

This solves to $$T(n) = O(\log n)$$ as we can only halve the input $O(logn)$ times before reaching a base case.

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

## Merge Sort

1. Divide the array into 2 halves
2. Recur recursively and sort each half
3. Conquer two sorted halves to make a single sorted array

### Merge Sort Pseudocode

```
def merge_sort(S):

    # base case
    if |S| < 2 then
        return S

    # divide
    mid = |S| / 2
    left = S[:mid]
    right = S[mid:]

    # recur
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # conquer
    return merge(sorted_left, sorted_right)
```

### How to Merge

Input: Two sorted lists
Output: A new, merged, sorted list

To merge, we use:

- $O(n)$ comparisons
- An array to store results

**Merge algorithm**:

- Keep track of the smallest element in each sorted half with a pointer
- Insert smallest of two elements into the resultant array
- Repeat until done

```
def merge(L, R):
    result = array of length (|L| + |R|)
    l, r = 0, 0
    while l + r < |result|:
        index = l + r
        if r >= |R| or (l < |L| and L[l] < R[r]):
            result[index] = L[l]
            l += 1
        else:
            result[index] = R[r]
            r += 1
    return result
```

### Merge Correctness

Induction Hypothesis:

- After the i-th iteraiton, our result contains the i smallest elements in sorted order

Base case:

- After 0 iterations, the result is empty, so the hypothesis holds

Induction:

- Assume Induction Hypothesis holds after iteration k, prove it after iteration k+1
- Since both halves are sorted and we add the smallest element not already in result, result now contains the k+1 smallest elements
- Sorted order follows from the fact btoh halves themselves are dorted, meaning that adding the smallest element implies sorted order of result

### Merge Sort Complexity analysis

Divide Step (find middle and split): $O(n)$ time
Recur Step (sort left and right halves): $2T(n/2)$ time
Conquer Step (merge subarrays): Takes $O(n)$ time

Now, we have to set up the recurrence for $T(n)$:
T(n) =
Case 1: 2T(n/2) + O(n) for n > 1
Case 2: O(1) for n = 1

This solves to $T(n) = O(nlogn)$

Broken down:
The divide step involves finding the middle of the array and splitting the array into two halves - which takes linear time O(n) because we need to iterate through each element to split the array into two different arrays. However, this is not directly included in the recurrence relation because it is a constant time operation relative to the size of the problem. The Recur step involves recursively sorting the left and right halves. Each recursive call operates on a half sixed array, and there are 2 halves, so the total time for this step is 2T(n/2). The conquer step is executed at the end of the sort, and merges the two sorted halves together. This takes linear time O(n).

In the case that n > 1, we would have to divide, recur and conquer, and hence this is where we get "Case 1: 2T(n/2) + O(n) for n > 1". In the case that n = 1, this is the base case, for arrays of size 1 which are already sorted. Then we use Master Theorem to solve the recurrence relation, where according to the Master Theorem, if f(n) is in O(n^c) where c = log_b(a), then the time complexity of the algorithm is O(n^c log n).

To solve the recurrence relation \( T(n) = 2T(n/2) + O(n) \) using the method of unrolling (also known as the expansion method), follow these steps:

### Step 1: Expand the Recurrence

First, expand the recurrence for a few levels:

1. **Initial recurrence**:
   \[
   T(n) = 2T\left(\frac{n}{2}\right) + O(n)
   \]

2. **First expansion**:
   \[
   T\left(\frac{n}{2}\right) = 2T\left(\frac{n}{4}\right) + O\left(\frac{n}{2}\right)
   \]
   Substituting this back into the original recurrence:
   \[
   T(n) = 2\left(2T\left(\frac{n}{4}\right) + O\left(\frac{n}{2}\right)\right) + O(n)
   \]
   Simplifying:
   \[
   T(n) = 4T\left(\frac{n}{4}\right) + 2O\left(\frac{n}{2}\right) + O(n)
   \]

3. **Second expansion**:
   \[
   T\left(\frac{n}{4}\right) = 2T\left(\frac{n}{8}\right) + O\left(\frac{n}{4}\right)
   \]
   Substituting this back:
   \[
   T(n) = 4\left(2T\left(\frac{n}{8}\right) + O\left(\frac{n}{4}\right)\right) + 2O\left(\frac{n}{2}\right) + O(n)
   \]
   Simplifying:
   \[
   T(n) = 8T\left(\frac{n}{8}\right) + 4O\left(\frac{n}{4}\right) + 2O\left(\frac{n}{2}\right) + O(n)
   \]

### Step 2: Generalize the Pattern

From the expansions, we can see a pattern forming. At the \( k \)-th expansion, the recurrence looks like:

\[
T(n) = 2^k T\left(\frac{n}{2^k}\right) + \sum\_{i=0}^{k-1} 2^i O\left(\frac{n}{2^i}\right)
\]

### Step 3: Determine the Base Case

We continue expanding until \( \frac{n}{2^k} \) reaches the base case, typically \( T(1) \). Assuming \( T(1) = O(1) \), we set \( \frac{n}{2^k} = 1 \). Solving for \( k \):

\[
k = \log_2 n
\]

### Step 4: Substitute and Sum the Series

Substituting \( k = \log_2 n \):

\[
T(n) = 2^{\log*2 n} T(1) + \sum*{i=0}^{\log_2 n - 1} 2^i O\left(\frac{n}{2^i}\right)
\]

Since \( 2^{\log_2 n} = n \) and \( T(1) = O(1) \):

\[
T(n) = n O(1) + \sum\_{i=0}^{\log_2 n - 1} O(n)
\]

### Step 5: Simplify the Sum

Each term in the sum \( O(n) \) is added \( \log_2 n \) times:

\[
\sum\_{i=0}^{\log_2 n - 1} O(n) = O(n) \cdot \log_2 n
\]

### Step 6: Combine the Results

Combining these results, we get:

\[
T(n) = O(n) + O(n \log_2 n)
\]

Since \( O(n \log_2 n) \) dominates \( O(n) \):

\[
T(n) = O(n \log n)
\]

Therefore, the solution to the recurrence relation \( T(n) = 2T(n/2) + O(n) \) using unrolling is \( T(n) = O(n \log n) \).

## Quick Sort

1. Divide: Choose a random element from the list as the **pivot**. Partition the elements into 3 lists: those less than the pivot, those equal to the pivot, and those greater than the pivot.
2. Recur: Recursively sort the less than and greater than lists.
3. Conquer: Join the sorted 3 lists together

Quick sort doesn't allocate any external space and it sorts the array in-place.

### Quick Sort Complexity Analysis

Divide step (pick pivot and split) takes $O(n)$ time
Recur step (solve left and right subproblems) takes T(nL) + T(nR) time
Conquer step (merge subarrays) takes $O(n)$ time

To set up a recurrence for $T(n)$:

E[T(n)]:
Case 1: E[T(nL) + T(nR)] + O(n) for n > 1
Case 2: O(1) for n = 1

This solves to E[T(n)] = O(nlogn) expected time

We've looked at a couple of sorting algorithms:

- Insertion Sort and Selection Sort (with priority queues) which complete in n^2 time
- Merge sort which completes in nlogn time
