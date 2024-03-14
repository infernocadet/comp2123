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

a) upperbound the running time of the algorithm in terms of $n$ using $O$-notation.

b) lowerbound the running time of the algorithm in terms of $n$ using $\Omega$ notation.


### Problem 2 (25 points)

Consider a stack where each element stores an integer value. We want to extend the stack ADT we saw in the lectures with the additional operations listed below. The operations should run in O(1) time and the running time of the other stack operations should remain the same as those of a regular stack:

```Count()``` returns the number of items on the stack

```Sum()``` returns the sum of all elements on the stack

```Average()``` returns the average of all the elements on the stack

For each operation, describe their implementation in English, argue the correctness and the running time. 


### Problem 3 (25 points)

As input we are given a *sorted* array $B$ containing $n$ positive integers, together with an integer $m$. The aim is to compute how many indices $i$ and $j$ (with $i < j$) there are such that the sum of the $i$th and the $j$th element of $B$ is at least $m$, i.e., $A[i] + A[j] >= m$. For full marks, your algorithm needs to run in $O(n)$ time.

Example:
$B = [1, 4, 4, 6], m = 7 → \text{ return } 4$

a) Design an algorithm that solves the problem.

b) Argue the correctness of your algorithm.

c) Analyse the running time of your algorithm.

