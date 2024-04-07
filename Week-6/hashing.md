# Hashing & Hash tables

## Application - Network Routers

Network routers process multiple streams of packets at high speed. To process a packet with destination ```k```, and data payload ```x```, a router must determine which outgoing link to send the packet along.

Such a system needs to support:

- destination-based lookups ```get(k)``` operations that return the outgoing link for destination ```k```
- updates to the routing table, ```put(k, c)``` operations where ```c``` is the new outgoing link for destination ```k```.

We want to achieve $O(1)$ time for both operations - ideally.

### Recall: Maps

A map models a searchable collection of key-value pairs.
Main ops:

- search
- insert
- delete

### Recall: Map Operations

- ```get(k)```: if map has entry with key ```k```, return its value, else return null
- ```put(k,v)```: insert entry ```(k,v)``` in map if key ```k``` is not already in map, then return null else return old value associated with k
- ```remove(k)```: if map has an entry with key ```k```, remove from map and return its associated value
- ```size()```
- ```is_empty()```
- ```entries()```: returns an iterable collection of the entries in M
- ```keys()```: returns an iterable collection of keys in M
- ```values()```: returns values

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/mapops.png" width="450" height="auto">
</p>

## Simple List-Based Map

We can implement a map using an unsorted list (doubly linked) in arbitrary order

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/lbmap.png" width="450" height="auto">
</p>

### Performance of List-Based Map

Performance:

- ```put()``` takes $O(1)$ time if the key doesn't exist yet, we can insert the item at the beginning or end of sequence.
- ```put()```, ```get()``` and ```remove()``` take $O(n)$ time since in the worst case, we must traverse the entire sequence of look for an item with the given key

The unsorted list implementation is only effective for maps of small size or for maps in which puts are the most common operations, while searches and removals are rare (e.g. a historical record of logins)

### Simple Implementation with restricted keys

Maps support the abstraction of using keys as addresses to get items.

Consider a restricted setting, in which a map with $n$ items with keys in a range from $0$ to $N-1$, for some $N \ge n$.

- Implement using an array with size $N$
- Key can be index so entries can be located directly
- O(1) get put and remove operations

The only drawback is that usually $N$ has to be **a lot** larger than $n$. Take for example, StudentID is 9 digits, so a Map with StudentID key can be stored in an array of $1,000,000,000$ entres.

#### Analysis of this structure

Has a really good worst-case runtime, however, bad space utilisation when key set is sparse in the space of possible keys such as SID. Unable to handle more general keys like strings

## Hash Functions and Hash Tables

To get around these issues, we use a **hash function** $h$ to map keys to corresponding indices in an array A.

$h$ is a mathematical function which always gives the same output for any particular $x$ and $h$ is fairly efficient to compute.

We call this data structure a **hash table**.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/htab.png" width="350" height="auto">
</p>

A **hash function** $h$ maps keys of a given type to integers in a fixed interval [0, N-1].

- E.g. $h(x) = x \text{ mod } N$
- the integer $h(x)$ is the **hash value** of key $x$

A **hash table** for a given key type $K$ consists of:

- hash function $h: K \rightarrow [0, N-1]$
- array (called table) of size $N$
- ideally, item $(x, o)$ stored at $A[h(x)]$

Example:
We design a hash table for a map storing entries as SIDs (student ids, a nine-digit positive integer). Our hash table uses an array of size $N=10000$ and the hash function $h(x) = \text{ last four digits of \textbf{x}}$

### Choice of hash functions

We will use simple (and not good) choices that can be calculated by hand

- e.g. for an unbounded integer key in array of size 11, we might use remainder mod 11 as hash function
- e.g. for string key, in array of size 10, we might do an example where $h(S) = \text{ position in alphabet of first character mod } 10$

## Arithmetic modulo N

$x mod N$ is mathematical notation for remainder

- if $x = c * N + r \text{ with } 0 \le r < N \text{ then } r = x \text{ mod } N$
- also $r = x - N * \lfloor x/N \rfloor$
- numbers wrap around when working with mod N
- 35 mod 10 = 5
- 20 mod 10 = 0
- the python operator is x % n

## Hash Functions

Many types of keys to start from: integers, floating point numbers, strings, or arbitrary objects (whole binary search tree)

A hash function $h$ is usually the composition of two functions:

- hash code:
  - $h_{1} : \text{ keys } \rightarrow \text{ integers }$
- compression function:
  - $h_{2}: \text{ integers } \rightarrow [0, N-1]$

The goal of the hash function is to *disperse* the keys in a psuedorandom way. In general we want to avoid items being hashed to the same location.

### Common Hash Codes

There are two general approaches that one can take:

- view the key $k$ as a tuple of integers $(x_{1}, x_{2}, ... , x_{d})$ which each being an integer in range $[0, M-1]$ for some $M$.
- view the key $k$ as a possibly very large nonnegative integer.

## Summing Components

In the case where our keys $k$ is a $d$-tuple, of the form: $k = (x_{1}, x_{2}, ... , x_{d})$, where each $x_{i}$ is an integer, one possible hash function we could use is to sum up the different components in each key. That is, we compute $h(k)$ as

$$
h(k) = \sum_{i=1}^{d} x_{i}
$$

or every addition is modulo some integer $p$, where $p$ is a prime, so that the result is in range $[0, p-1]$:

$$
h(k) = \sum_{i=1}^{d} x_{i} \text{ mod } p
$$

A slight variation on this theme is to compute an exclusive-or of all the components of the key, written as

$$
h(k) = \oplus_{i=1}^{d} x_{i}
$$

However these may cause problems because these hash codes are invariant under permutations of the key tuple. E.g., "mate", "meat", "team" etc map to the same hash value.

A better hash code in such case should somehow take into consideration, the position of the $x_{i}$s.

#### Polynomial-Evaluation Functions

Used on keys $k = (x_{1}, x_{2}, ... x_{d})$, for a **given nonzero** constant $a \ne 1$, we define:
$$
h(k) = x_{1}a^{d-1} + x_{2}a^{d-2} + ... + x_{d-1}a^{1} + x_{d}
$$

Now, two permutations of the same tuple dont collide.

Some observations:

- can be evaluated with Horner's algorithm in $O(d)$ time
- arithmetic operations are usually done with modulo p where p is a prime to avoid overflow
- value of a is chosen empirically to avoid collision

## Modular division

For keys $k$ that are (maybe large) positive integers

$$
h(k) = k \text{ mod } N \text{, for some prime number N}
$$

If keys are randomly uniformly distributed $[0, M]$ where $M >> N$, then the probability that two keys collide is $1/N$. Therefore, keys are usually not randomly distributed.

## Universal hash functions

Suppose that $[0, M]$ is the range of our keys and we need a hash function with range in $[0, N-1]$. Let $H$ be a family of such hash functions.

Let $H$ be a family of such hash functions. $H$ is 2-universal if picking $h$ uniformly at random (UAR) from $H$ yields:

$$
Pr[h(i) = h(j)] \le 1/N
$$

Let $h$ be a function chosen UAR from a 2-universal family. Then the expected nuber of collisions for a given key $k$ in a set of $n$ keys is at most $n/N$.

### Random Linear Hash function

Used on keys $k$ that are positive integers:

$$
h(k) = ((a*k+b) \text{ mod } p) \text{ mod } N
$$

for some prime number $p$, and $a$ and $b$ are chosen uniformly at random from $[1, p-1]$ with $a \ne 0$.

If the keys are in the range $[0, M]$ and $p > M$, then the probability that two keys collide is $1/N$.

## Collision Handling

Collisions occurs when two or more elements are hashed to the same location in the array.

A good hash function makes collisions rare, but when they do happen, we need to deal with them:

- separate chaining
- linear probing
- cuckoo hashing

### Separate chaining

Let each cell in the table point to a linked list holding the entries that map there. This linked list is restricted to only hold items $(k, v)$ such that $h(k) = i$.

Get, put and remove operations are delegated to the appropriate list, where put needs to search through the list to replace the existing vlaue of the key if present.

Seperate chaining is simple, but requires additional memory outside the table.

```python
def get(k):
    return A[h[k]].get(k)

def put(k,v):
    return A[h[k]].put(k, v)

def remove(k):
    return A[h[k]].remove(k)
```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/sepc.png" width="350" height="auto">
</p>

#### Performance

Assume our hash function maps $n$ keys to independent uniform values in the range $[0, N-1]$. Let $X$ be a random variable representing the number of items that map to a bucket in the array $A$, then
$$
E(X) = n/N
$$

where $n$ is the number of items in the map, since each of the $N$ locations in $A$ is equally likely for each item to be placed. This parameter $n/N$ is the ratio of the number of items in a hash table $n$, and the capacity of the table, $N$, is called the ***load factor*** of the hash table, written as $\alpha$.

The expected time for hash table operations is $O(1 + \alpha)$, when collisions are handled with separate chaining.

The worst case time is $O(n)$, which happens when all items collide into a single chain.

### Open addressing using Linear Probing

*Open addressing*: the colliding item is placed in a different cell of the table.

*Linear probing*: handles collisions by placing the colliding item in the next (circularly) available cell

- each table cell inspected is referred to as a probe
- colliding items lump together, causing future collisions to cause a longer sequence of probes.

Say we try to insert $k$ into $A[i]$ where $h(k) = i$. If it is occupied, then we try $A[(i+1) \text{ mod } N]$ and so on.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/prob.png" width="350" height="auto">
</p>

This new collision resolution strategy requires that we change the implementation of the ```get(k)```. We must examine consecutive buckets starting from A[h(k)] until we find an item with key equal to $k$ or an empty bucket or N cells have been probed (in which the search was not successful)

```python
def get(k):
    i ← h(k)
    p ← 0
    repeat
        c ← A[i]
        if c.isEmpty():
            return null
        else if c.get_key() = k then
            return c.get_value()
        else
            i ← (i+1) mod N
            p ← p + 1
    until p = N
    return null
```

### Updates with Linear Probing

To handle insertions and deletions, we introduce a special object called ```DEFUNCT``` which replaces deleted elements, to tell them apart from empty cells.

- ```get(k)```: must pass over cells with DEFUNCT and keep probing until the element is found, or until reaching an empty cell
- ```remove(k)```: search for the entry as in ```get(k)```. if found, replace it with special item DEFUNCT and return element ```v```.
- ```put(k, v)```: search for the entry as in ```get(k)```, but remember the index $j$ of the first cell we find that has DEFUNCT or empty.
  - if we find key $k$, replace the value there with $v$ and return the previous value. If we don't find $k$, store ```(k, v)``` in cell with index $j$

#### Performance of linear probing

In the worst case, get, put and remove take $O(n)$ time.

Assuming hash values are uniformly randomly distributed, expected number of probes for each get and put is $\frac{1}{1-\alpha}$ where $\alpha = n/N$ is the load factor of the hash table.

Thus is the load factor is a constant $< 1$, then the expected running time for get and put operations is $O(1)$. Hashing is very fast provided the load factor is not close to 100%, but removals complicate implementation.

### Hash Table implementations

Recall that load factor of a hash table is defined as $\alpha = n/N$.

Experiments and theory suggest that $\alpha$ should be kept not too high:

- Java's HashSet uses chaining with $\alpha < 0.75$ and switches from a linked list to binary search tree if bucket is too large
- Python's dict uses open addressing with $\alpha < 0.66$

When the load factor of a hash table reaches a given bound, the table is replaced with a table twice the size and elements are hashed over to the new table

### Cuckoo hashing

Main problem is that operations take $O(n)$ time in the worst-case. Cuckoo hashing achieves $O(1)$ time for lookup and removal, and expected $O(1)$ for insertions.

Use two hash tables $T_{1}$ and $T_{2}$, each of size $N$.

Use two hash functions $h_{1}$ and $h_{2}$, for $T_{1}$ and $T_{2}$ respectively.

For an item with key $k$, there are only two possible places where we are allowed to store the item: $T_{1}[h_{1}(k)]$ or $T_{2}[h_{2}(k)]$.

This restriction simplifies look up dramatically, while still allowing worst-case $O(1)$ time for get and remove.

e.g. Take each key in set $S = {2, 3, 5, 8, 9}$, they have 2 possible places to go, $T_{1}$ and $T_{2}$.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/cash.png" width="350" height="auto">
</p>

Note 2 and 8 collide in $T_{2}$, but there is no collision for 2 in its alternative location in $T_{1}$.

#### get() &

```python
def get(k):
    if T1[h1(k)] != null and T1[h1(k)].key = k then:
        return T1[h1(k)].value
    if T2[h2(k)] != null and T2[h2(k)].key = k then:
        return T2[h2(k)].value
    return null

def remove(k):
    temp ← null
    if T1[h1(k)] != null and T1[h1(k)].key = k then:
        temp ← T1[h1(k)].value
        T1[h1(k)] ← null
    if T2[h2(k)] != null and T2[h2(k)].key = k then:
        temp ← T2[h2(k)].value
        T2[h2(k)] ← null
    return temp
```

Both of these are simple and run in $O(1)$ time.

#### Idea behind put()

If a collision occurs in the insertion operation in the cuckoo hashing scheme, we evict the previous item in that cell and insert the new one in its place. This forces the evicted item to go it its alternate location in the other table and be inserted there, which may repeat the evicted process.

Eventually, we either find an empty cell and stop or we repeat a previous eviction, which indicates an eviction cycle. If we discover an eviction cycle, then we bail out or rehash all the items into larger tables.

```python
def put(k, v):
    # fit item into T1
    if T1[h1(k)] != null and T1[h1(k)].key = k then:
        T1[h1(k)] ← (k, v)
        return
    # fit item into T2
    if T2[h2(k)] != null and T2[h2(k)].key = k then:
        T2[h2(k)] ← (k, v)
        return
    # start eviction sequence
    i ← 1
    repeat
        if Ti[hi(k)] = null then:
            Ti[hi(k)] ← (k, v)
            return
        temp ← Ti[hi(k)]
        Ti[hi(k)] ← (k, v)
        (k, v) ← temp
        i ← 1 if i = 2 else 2
    until a cycle occurs
    rehash elements
```

### Detecting eviction cycles

We use a counter to track the number of evictions. If we evict enough times, we are guaranteed to have a cycle.

We can an additional flag for each entry. Every time we evict an entry, we flag it. After a successful put, we need to unflag the entries flagged.

### Performance of Cuckoo Hashing

We can show that long eviction sequences happen with very low probability.

Assuming hash values are uniformly randomly distributed, expected time of $n$ put operations is $O(n)$, provided $N> 2n$.

Cucko hashing achieves worst-case $O(1)$ for lookups and removals.

## Set ADT

A **set** ADT is an unordered collection of elements, without duplicates that supports efficient membership tests.

Elements in a set are like keys of a map, without auxiliary values.

- ```add(e)```: add element $e$ to $S$ if not already present
- ```remove(e)```: remove element $e$ from $S$ (if present)
- ```contains(e)```: returns whether $e$ is present in $S$
- ```iterator()```: returns an iterator of the elements of $S$.

There is also support for traditional mathematical set operations such as **union**, **intersection** and **subtraction** of two sets S and T.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/setnot.png" width="350" height="auto">
</p>

- ```addAll(T)```: updates $S$ to include all elements of $T$
- ```retainAll(T)```: updates $S$ to keep only elements that are also elements in $T$
- ```removeAll(T)```: updates $S$ to remove any elements that are also elements in $T$

### Set implemented via Map

- use a map to store the keys, and ignore the value
- allows ```contains(e)``` to be answered by ```get(k)```
- using HashMap for Map gives main Set operations that usually can be performed in $O(1)$ time.

### MultiSet

Like a ```set``` but allows duplicates, also called a ```Bag```. The ```count(e)``` operation returns occurences of $e$ in collection. ```remove(e)``` removes one occurrence (provided $e$ is in collection already)

We implement using Mpa where the element is the key, and the associated value is the number of occurences
