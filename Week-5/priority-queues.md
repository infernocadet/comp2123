# Priority Queues

## Priority Queue ADT
A priority queue is a type of ADT map which stores a sorted collection of key-value items, where we can only remove the smallest key.

Priority queue comes from the fact that keys determine the **priority** used to pick elements to be removed.

- ```insert(k,v)```: insert item with key ```k``` and value ```v```
- ```remove_min()```: remove and return the item with smallest key ```k```
- ```min()```: return item with smallest key
- ```size()```: return how many items are stored
- ```is_empty()```: test is queue is empty

We can also have a **max** version of this **min** version but we cannot use both versions at once.

#### Example

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/prioq.png" width="350" height="auto">
</p>

### Application: Stock Matching Engines
Stock trading systems use **matching engines**, which match the stock trades of buyers and sellers.

Buyers post bids to buy a number of shares of a given stock at or below a specified stock price.

Sellers post offers (asks) to sell a number of shares of a given stock at or above a specified price.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/sme.png" width="350" height="auto">
</p>

Buy and sell orders are organised according to a **price-time priority**, where price has highest priority and time is used to break ties.

When a new order is entered, the matching engine determines if a trade can be immediately executed, and if so, performs the apprioriate matchs according to price-time priority.

A matching engine can be implemented with two **priority queues**, one for buy orders and one for sell orders.

This data structure performs element removals based on priorities assigned to elements, when they are inserted.

```python
while True:
    bid = buy_orders.remove_max()
    ask = sell_orders.remove_min()
    if bid.price ≥ ask.price:
        trade(bid, ask)
    else:
        buy_orders.insert(bid)
        sell_orders.insert(ask)
```

## Sequence-based Priority Queue

#### Unsorted list implementation:
- ```insert()``` takes $O(1)$ time as we can insert the item at the beginning of the sequence.
- ```remove_min()``` and ```min()``` run in $0(n)$ time since we have to traverse the entire list to find the smallest key

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/unsqu.png" width="350" height="auto">
</p>

#### Sorted list implementation
- ```insert()``` runs in $O(n)$ time since we have to find the place to insert the item
- ```remove_min()``` and ```min()``` run in $O(1)$ time as the smallest key is at the beginning

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/sque.png" width="350" height="auto">
</p>

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/qusum.png" width="350" height="auto">
</p>

## Priority Queue Sorting

We can use a priority queue to sort a list of keys:
1. iteratively insert keys into an empty priority queue
2. iteratively ```remove_min()``` to get the keys in sorted order

```python
def priority_queue_sorting(A):
    pq = new priority queue
    n = size(A)
    for i in [0, n]:
        pq.insert(A[i])
    for i in [0, n]:
        A[i] pq.remove_min()
```

Regardless if we use an unsorted or sorted list, sorting will take $O(n^2)$, as either one of the ```for loops``` will take $O(n^2)$ time *(refer to the above table of time complexity of common methods)*.

### Selection Sort

Consider storing the elements of $P$ and their keys in an unordered list, $S$. Let's say that $S$ is a general lsit implemented with either an array or whatever doubly-linked list it doesn't matter. The elements of $S$ are pairs $(k,e)$ where $e$ is an element of $P$ and $k$ is its key. 

A simple way of implementing method ```insert(k,e)``` of $P$ is to add the new pair object $p=(k,e)$ at the end of list $S$. This takes $O(1)$ time. This means that $S$ will be unsorted. However ```remove_min()``` must inspect all elements of $S$ and hence takes $O(n)$ time. 

If we implement the priority queue $P$ with an unsorted list, then the first phase of ```pq-sort``` takes $O(n)$ time, for we can insert each element in constant time. IN the second phase, assuming we can compare two keys in constant time, the running time of each ```remove_min()``` operation is proportional to the number of elements currently in $P$. The bottleneck computation in this implementation is a "selection" of the minimum element from an unsorted list. This sorting algorithm is better known as **selection-sort**.

The size of $P$ starts at $n$ and decreases which each remove_min() until it becomes 0. The first remove_min() operation takes $O(n)$ time, the second take s$O(n-1)$ and so on, until the last operation takes $O(1)$. Therefore the total time take is proportional to the sum:

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/mathsum.png" width="350" height="auto">
</p>

Hence, the second phase, ```remove_min()``` takes $O(n^2)$ time. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/selectiondia.png" width="350" height="auto">
</p>

This illustration above shows a selection-sort run on list $S$. This follows the two-phase ```PQ-SORT``` and uses a priority queue $P$ implemented with an unsorted list. We repeatedly remove the first element from $S$ and insert it into $P$. $P$ essentially is a copy of $S$. We then repeatedly perform ```remove_min()``` operations on $P$ and add it to $S$.

A variant of ```pq-sort``` using unsorted sequence implementation:
1. insert elements with ```n``` ```insert()``` operations takes $O(n)$ time
2. removing elements with ```n``` ```remove_min()``` operations takes $O(n^2)$ time

```python
def selection_sort(A):
    n = size(A)
    for i in (O, n):
        # find index s of the smallest element in A[i:n]
        s = i
        for j = i + 1 to n:
            if A[j] < A[s]:
                s = j
        if i != s:
            # swap A[i] and A[s]
            t = A[s]; A[s] = A[i]; A[i] = t
    return A
```

The selection-sort algorithm, which is an ***in-place*** algorithm, is where the input list $S$ is given as an array $A$ and only a constant amount of memory is used in addition to that used by $A$. In each iteration, $A[1, i-1]$ is the sorted portion and $A[i, n]$ is the unsorted priority queue.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/seleg.png" width="350" height="auto">
</p>

### Insertion Sort

An alternative implementation of priority queue $P$ uses a list $S$ where we store items ordered by key values. The first element in $S$ is always the an element with smallest key in $P$. We can implement ```remove_min()``` by removing the first element in $S$. Assuming that $S$ is implemented with a linked list or an array which supports constant-time front-element removal, finding and removing the minimum in $P$ takes $O(1)$ time. However, the ```insert()``` method of $P$ requires we scan through the list $S$ to find the appropriate place to insert the new element and key. This takes $O(n)$ time, where $n$ is the number of elements in $P$ at the time the method i executed. 

If we implement priority queue $P$ using a sorted list, then we improve the running time of the second-phase of ```PQ-Sort``` to $O(n)$, as each operation for ```remove_min()```takes $O(1)$ time. However now the first phase becomes the bottleneck. The running time of each ```insert()``` operations is proportional to the number of elements currently in the priority queue. This sorting algorithm is known as ***insertion-sort***, and the bottleneck is the repeated insertion of a new element at the appropriate position in the list. 

Whilst both ***insertion-sort*** and ***selection-sort*** have upperbounds of $O(n^2)$ time, selection-sort always takes $\Omega(n^2)$ time, whilst, if the list is in reversed order, insertion-sort takes $O(n)$ time.

```python
def insertion_sort(A):
    #input: array A, of n elements
    #output: ordering of A so that elements are nondecreasing
    for i in (2, n):
        x = A[i]
        # put x in right place in A[1, i], moving larger elements up if needed
        j = i
        while j > 1 and x < A[j-1]:
            A[j] = A[j-1] # move A[j-1] up one cell
            j -= 1
        A[j] = x
    return A
```

The insertion-sort algorithm is an ***in-place*** algorithm, and there is only a constant amount of extra memory used. In each iteration, $A[1...i-1]$ is the sorted priority queue and $A[i...n]$ is the unsorted input list.

## Heap Data Structure (min-heap)

An implementation of a priority queue which is efficient for both the ```insert(k,e)``` and ```remove_min()``` operations is to use a **heap**. We can perform insertions and removals in logarithmic time. We abandon the idea of storing elements and keys in a list and store elements and keys in a binary tree instead.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/heap.png" width="350" height="auto">
</p>


A **heap** is a binary tree $T$ which stores a collection of keys at its internal nodes, and satisfies two additional properties: a relational property defined in terms of the way keys are stored in T and a structural property defined in terms of $T$ itself. The relational property for T is the following:

#### Heap-Order Property
| :bulb:  In a heap $T$, for every node $v$ other than the root, the key stored at $v$ is greater than or equal to the key stored at $v$'s parent.  |
|-----------------------------------------|

As a consequence of this property, keys encountered on a path from the root to a leaf node are in non-decreasing order. A minimum key is always stored at the root of $T$. We also want $T$ to have the minimum height possible, by enforcing another structural property:

#### Complete Binary Tree
| :bulb:  A binary tree $T$ with height $h$ is *complete* if the levels $0, 1, 2..., h$ have the maximum number of nodes possible, that is, level $i$ has $2^i$ nodes, for $0 ≤ i ≤ h-1$, and for the level $h-1$, all the internal nodes are to the left of external nodes.|
|-----------------------------------------|

By saying that all the internal nodes on level $h-1$ are to the left, we mean that all the internal nodes on this level will be visited before any external nodes in an inorder traversal. The ***last node*** of $T$ is the right-most, deepest internal node of $T$.

### Minimum of a Heap
The root always holds the smallest key in the heap.

**Proof**: Suppose the minimum key is at some internal node $x$. Because of the heap property, as we move up, the keys can only get smaller. If $x$ is not the root, then the parent holds a smallest key. 

### Height of a Heap
A heap storing $n$ keys has height of $log(n)$.

**Proof**: Let $h$ be the height of a heap storing $n$ keys. Since there are $2^i$ keys at depth $i = 0, ..., h-1$ and at least one key at depth $h$, we have $n >= 1 + 2 + 4 + ... + 2^{h-1} + 1$, thus $n >= 2^h$, and hence $log(n) >= h$.

## Insertion into a Heap
In order to store a new key-element pair $(k,e)$ in $T$, we need to add a new internal node to $T$. To keep $T$ as a complete binary tree, we must add this new node so that it becomes the new last node of $T$. We must identify the correct external node $z$ and insert the new element at $z$. 

This is usually the external node immediately right of the last node $w$.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/heapins.png" width="350" height="auto">
</p>

### Up-Heap Bubbling

After inserting, we need to restore the heap-order property.