# Assignment 1
*COMP2123 - 510435765*

## ADVICE
- When designing a DSA:
1. briefly describe general idea
2. develop and elaborate

- Use lecture or textbook for proof

- Prove/explain/motivate answers

- When giving an algorithm, algorithm does not have to be given as psuedo-code or code.

- If you provide psuedo-code or code, then explain code and ideas in plain english.

- Always talk from worst-case analysis

- We are interested in the most efficient DSA

### Problem 1 (10 points)

Consider the following snippet of pseudocode that takes an array of $n$ integers. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/prob1.png" width="auto" height="auto">
</p>

Your task is to:

*a) upperbound the running time of the algorithm in terms of* $n$ *using* $O$*-notation.*

The bulk of this algorithm comprises of a nested for loop. The outer loop uses a pointer $i$ which runs from $0$ to $n-1$ where $n$ is the length of the array. The inner loop uses a pointer $j$ which runs from $i+1$ to $n-1$. Hence the inner loop runs $n-i-1$ times for each iteration of the outer loop.

The worst-case scenario is when we have to process through the full size of the array, i.e. $n$ times.

We can sum the series of how many times the inner loop runs by calculating the series of how many times ```line 5``` runs for each value of $i$ in ```line 4```. This gives us:

$$\sum_{i=0}^{n-1} (n-i-1) = \sum_{i=0}^{n-1} (n-1) - \sum_{i=0}^{n-1} (i)$$

$$= n(n-1) - \frac{(n-1)n}{2}$$

$$= \frac{n(n-1)}{2}$$

$$=O(\frac{1}{2}n^{2} + \frac{1}{2}n)$$

Considering lines 2, 3, 6, 7 and 8 all run in $O(1)$ time, we can drop them and take the most significant order of $n$, hence this algorithm runs in $O(n^2)$ in the worst-case scenario.

*b) lowerbound the running time of the algorithm in terms of* $n$ *using* $\Omega$ *notation.*

Assume for simplicity that $n$ is even. To lowerbound the running time, we consider only the last $n/2$ integers of the array. Since this is part of the full execution, analysing this part gives us a lower bound on the total running time. This gives us:

$$\sum_{i=\frac{n}{2} + 1}^{n-1} (n-i-1) = \sum_{i=\frac{n}{2} + 1}^{n-1} (n-1) - \sum_{i=\frac{n}{2} + 1}^{n-1} (i)$$

Using the arithmetic series:

$$=\frac{n}{4}(2n-2) - \frac{n}{4}(\frac{n}{2} + n)$$



### Problem 2 (25 points)

Consider a stack where each element stores an integer value. We want to extend the stack ADT we saw in the lectures with the additional operations listed below. The operations should run in O(1) time and the running time of the other stack operations should remain the same as those of a regular stack:

```Count()``` returns the number of items on the stack

```Sum()``` returns the sum of all elements on the stack

```Average()``` returns the average of all the elements on the stack

*For each operation, describe their implementation in English, argue the correctness and the running time. *


### Problem 3 (25 points)

As input we are given a *sorted* array $B$ containing $n$ positive integers, together with an integer $m$. The aim is to compute how many indices $i$ and $j$ (with $i < j$) there are such that the sum of the $i\text{th}$ and the $j\text{th}$ element of $B$ is at least $m$, i.e., $A[i] + A[j] >= m$. For full marks, your algorithm needs to run in $O(n)$ time.

Example:
$B = [1, 4, 4, 6], m = 7 → \text{ return } 4$

*a) Design an algorithm that solves the problem.*

*b) Argue the correctness of your algorithm.*

*c) Analyse the running time of your algorithm.*

