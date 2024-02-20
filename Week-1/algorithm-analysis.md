<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>

# Algorithm Analysis

## Algorithms
Algorithms are a **set of instructions used to solve a problem**.

## Data Structures
Data structures are formats for storing, managing, working with or structuring data or information.
Every data structure has advantages and disdvantages.

### Arrays

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/Screenshot%202024-02-19%20at%2011.48.14%20pm.png" alt="array" width="350" height="auto"/>
</p>

An array is a contiguous block of memory, which stores a collection of elements of same memory size and data type.

*Pros*: Highly efficient in accessing elements.

*Cons*: Fixed size once initialised.

### Linked List

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/Screenshot%202024-02-20%20at%2012.02.46%20am.png" alt="linked-list" width="350" height="auto">
</p>

A linked list is a data structure consisting of nodes, which contain a data field and a reference to the next node in the list.
It is a linear collection of data elements, whose order is not given by their physical placement in memory.

*Pros*: Dynamic sizing.

*Cons*: Low efficiency in accessing elements compared to array.

## Psuedocode

We can now try to put algorithm into psuedocode, a flexible style of code logic.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/Screenshot%202024-02-20%20at%2012.35.14%20am.png" alt="algorithm-psuedocode" width="350" height="auto">
</p>

When this *Insertion Sort Algorithm* is adapted into Python for example, it'll look like this:

```python
# Insertion Sort
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = key
```

**Control flow**

- if ... then ... [else ...]
- while ... do ...
- repeat ... until ...
- for ... do ...
- indentation replaces braces

**Method call**

- method (arg [, arg...])

**Return value**

- return *expression*

## Three Abstractions

### Computational problem
- defines a computational task
- specifies what the input is, and what the output should be

### Algorithm
- a step-by-step recipe to go from input to output (**what** your solution does)
- different from implementation

### Correctness and complexity analysis
- a formal proof that the algorithm solves the problem (**why** is what your solution does correct)
- analytical bound on the resources it uses
- what the running time of the algorithm is

#### Example

*Computational problem*: 
We are given an array *A* of integers and we need to return the maximum.

*Algorithm*: 
We go through all elements of the array in order, and keep track of the largest element.
For each position *i*, we check if the value stored at *A[i]* is larger than our current max, and if so update the max.
Then we return the maximum we found.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/Screenshot%202024-02-20%20at%201.19.01%20am.png" alt="psuedocode" width="350" height="auto">
</p>

*Correctness*:
We maintain the following invariant: after the *k*-th iteration, *max* stores the maximum of the first *k* elements.

Prove using induction: $$\text{when }k=0,\text{ }max = -∞$$ which is the maximum of the first 0 elements.

Assume the invariant holds for the first *k* iterations, and show that it holds after the *(k+1)th* iteration. In that iteration, we compare *max* to *A[k]* and update *max* if *A[k]* is larger. Hence, *max* is the maximum of the first *k+1* elements.

The **invariant** implies that after *n* iterations, *max* contains the maximum of the first *n* elements.

#### Example

*Motivation*
- we have information about the daily fluctuation of a stock price
- we want to evaluate our best possible single-trade outcome

*Input*
- an array with *n* integer values A[0], A[1], ..., A[n-1]

*Task*
- find indices: $$0 <= i <= j < n$$
which maximises
$$A[i] + A[i+1]+ ... A[j]$$

In simple english, this just means: given an array A of integers, find a pair of indexes, i and j, such that the sum of A[i] + A[i+1] + ... A[j] is maximised. So, both i and j can point to the same value and sum it twice, or they can be right next to each other, or if all the values are positive, then i and j can extend over the whole range of the array.

### Naive algorithm
High level description:
    - Iterate over every pair $$0 <= i <= j < n$$
    - For each, compute $$A[i] + A[i+1]+ ... A[j]$$
    - Return the pair with the maximum value

#### Naive preprocessing (psuedocode)
<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/naive%20preprocessing.png" alt="naive psuedocode" width="350" height="auto">
</p>

## Efficiency

**Definition**
*An algorithm is efficent if it runs quickly on real input instances.*

This is not a good definition because it is not easy to evaluate:
- instances considered
- implementation details
- hardware it runs on

Our definition should be **implementation independent**:
- count number of "steps"
- bound the algorithm's **worst case performance**

**An algorithm is efficient if it achieves qualitatively better worst-case performance than a brute-force approach**

Not a good definition because it is subjective:
- brute-force approach is ill-defined
- qualitatively better is ill-defined

Our definition should be **objective**:
- not tied to a strawman baseline
- independently agreed upon

### Definition
An algorithm is efficient if it runs in **polynomial time**; that is, on an instance of size *n*, it performances no more than *p(n)* steps for some polynominal:
$$p(x)=a_{d}x^{d}+\dots+a_{1}x+a_{0}

This gives us some information about the expected behaviour of the algorithm, and is useful for making predictions and comparing different algorithms.