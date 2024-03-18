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