# Lists

## Abstract Data Types (ADT)
Type defined in terms of its data items and associated operations, not in implementation. 

They are supported by many languages.

**Benefits of ADT Approach**:
- Code is easier to understand if different issues are separated
- Client can be considered at a higher, more abstract level
- Many different systems can use the same library
- Choices of implementation with performance tradeoffs

**ADT Challenges**:
- Specify how to deal with boundary cases
    - something that normally doesn't happen but we need to account for
    - what to do if ```reserve(x, y)``` is invoked when ```x``` is already occupied

- Do we need a new ADT? Can we use an existing one, and rename operations and tweak error-handling?

## Abstract data types and Data structures
An **abstract data type (ADT)** is a specification of the desired behaviour from the point of view of the user of the data. Something like an ```integer```, ```float```, or ```string```.

A **data structure** is a concrete representation of data, and this is from the point of view of an implementer, not a user.

### ADT in programming (python)
ADT is given as an *abstract base class (abc)*.

An *abc* declares methods (with names and signatures) without providing code, and we can't construct instances.

A data structure implementation is a class that inherits from the abc, provides code for all the required methods, and has a constructor.

Client code can have variables which are instances of the data structure class, and can call methods on the variables

### Index-Based Lists (List ADT)
An index-based list typically supports the following operations:

- ```size``` (int) number of elements in the store
- ```isEmpty()``` (boolean) whether or not the store is empty
- ```get(i)``` return element at index ```i```
- ```set(i,e)``` replace element at index ```i``` with element ```e```, and return element that was replaced
- ```add(i,e)``` insert element ```e``` at index ```i``` existing elements with ```index ≥ i``` are shifted up
- ```remove(i)``` remove and return the element at index ```i```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/list-operations.png" alt="comparison" width="350" height="auto">
</p>

### Array-based Lists
An option for implementing the list ADT is to use an array ```A```, where ```A[i]``` stores (*a reference to*) the element with index ```i```. If array has size ```N```, then we can represent lists of size ```n ≤ N```. Large ```N``` is the size of the data structure while small ```n``` is the size of the list.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/array-based-list.png" alt="comparison" width="350" height="auto">
</p>

#### Array-based Lists: ```get(i)```
The ```get(i)``` and ```set(i,e)``` methods are easy to implement by accessing ```A[i]```. Must check that ```i``` is a legitimate index (```0≤i≤n```).

Both operations can be carried out in constant time ```O(1)```, independent of size of array.

**Psuedo-code**:
```
def get(i)
# input: index i
# output: ith element in list
    if i < 0 or i >= n then
        return "index out of bound"
    else
        return A[i]
```

Time complexity is ```O(1)``` constant time, independent of size of array ```N``` or represented list ```n```.

#### Array-based Lists: ```set(i,e)```
Go to the position in the array ```A[i]``` and set equal to the value of ```e```.

**Psuedo-code**:
```
def set(i,e):
# input: index i and value e
# output: update ith element in list to e
    if i < 0 or i >= n then
        return "index out of bound
    result = A[i]
    A[i] = e
    return result
```

Time complexity is ```O(1)``` constant time, independent of size of array ```N``` or represented list ```n```.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/set-method.png" alt="comparison" width="350" height="auto">
</p>

#### Array-based Lists: ```add(i,e)```
In an operation ```add(i,e)```, we must make room for the new element, by shifting forward ```n-i``` elements ```A[i],...,A[n-1]```.

We also must check that there is space, such that ```n < N```.

The worst case scenario is adding an element to the start of the list, in which case we need to move all elements, which is moving ```n-1``` elements, which is time complexity of ```O(n)``` in the worst case.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/add-method.png" alt="comparison" width="350" height="auto">
</p>

**Psuedo-code**:
```
def add(i,e):
    if n = N then
        return "array is full"
    if i < n then
        for j in [n-1, n-2, ..., i] do
            A[j + 1] = A[j]
    A[i] = e
    n = n + 1
```

#### Array-based Lists: ```remove(i)```
In an operation ```remove(i)```, we need to fill the hole left at position ```i``` by shifting backward ```n - i - 1``` elements ```A[i+1],...,A[n-1]```.

We must also check that ```i``` is a legititmate index where ```0<=i<n```

**Psuedo-code**:
```
def remove(i):
    if i<0 or i>=n
        return "index out of bound"
    e = A[i]
    if i < n-1
        for j in [i, i+1,..., n-2] do
            A[j] = A[j+1]
    n = n-1
    return e
```

Time complexity is ```O(n)``` in the worst case

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/remove-method.png" alt="comparison" width="350" height="auto">
</p>

### Summary of static Array-based Lists
Limitations:
- can represent lists up to capacity of the array (```n vs N```)

Space complexity:
- space used is ```O(N)```, whereas we would like it to be ```O(n)```

Time complexity:
- both ```get(i)``` and ```set(i,e)``` take ```O(1)``` time
- both ```add(i,e)``` and ```remove(i)``` take ```O(n)``` in the worst case

### Positional Lists
ADT for a list where we store elements at "positions".

Position models the abstract notion of place where a single object is stored within a container data structure.

Unlike index based lists, this keeps referring to the same entry even after insertion/deletion happens elsewhere in the collection.

These are used for more dynamic sizes of data structures, whereas an index based, (static) list has a fixed size of ```N```.

Position offers just one method:
- ```element()```: return the element stored at the position entrance.

- ```size``` (int) number of elements in the store
- ```isEmpty()``` (boolean) whether or not the store is empty
- ```first()``` return **position** of first element *(null if empty)*
- ```last()``` return **position** of lasy element *(null if empty)*
- ```before(p)``` return **position** immediately before ```p``` *(null if ```p``` is first)*
- ```after(p)``` return **position** immediately after ```p``` *(null if ```p``` is last)*
- ```insertBefore(p, e)``` insert ```e``` in front of the element at position ```p```.
- ```insertAfter(p, e)``` insert ```e``` following the element at position ```p```.
- ```remove(p)``` remove and return the element at index ```ip```

### Singly Linked Lists
A fundamental data structure, contains a series of ```Nodes```, each with a reference to the next node. The list is captured by reference (```head```) to the first ```Node```.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/singly-linked-list.png" alt="comparison" width="350" height="auto">
</p>

#### Node implements Position
Each ```Node``` in a singly linked List stores:
- its element, and
- a link to the next ```node```.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/node.png" alt="comparison" width="350" height="auto">
</p>

#### Advice on working with linked structures
- Draw the diagram showing the state
- Show a location where you place carefully each of the instance variables (including references to nodes)
- Be careful to step through dotted accesses e.g. p.next.next
- Be careful about assignment to fields e.g. ```p.next = q``` or ```p.next.next = r```

#### Linked List: ```first()```
```first()```: return position of first element, null if empty.

The time complexity is ```O(1)```.

#### Linked List: ```last()```
```last()```: return position of last element, null if empty.

The time complexity is ```O(n)```.

#### Linked List: ```insertFirst()```
1. instantiate a new node ```x```.
2. set ```e``` as element of ```x```.
3. set ```x.next``` to point to (old) ```head``` (node)
4. update list's head to point to ```x```

The time complexity is ```O(1)```.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/insertFirst.png" alt="comparison" width="350" height="auto">
</p>

#### Linked List: ```removeFirst()```
1. update ```head``` to point to next ```node```
2. delete former first ```node```

The time complexity is ```O(1)```.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/removeFirst.png" alt="comparison" width="350" height="auto">
</p>

#### Linked List: ```insertBefore()```
```insertBefore()```: insert ```e``` in front of the element at position ```p```

1. create node x with value e
2. find node with position p (e.g. node d)
3. point node x to node d
4. find previous predecessor of node d, by traversing through the linked list, starting from the head (e.g. node c)
5. point node c to node x.

The time complexity is ```O(n)```. There is no constant-time way to find the predecessor of a node in a Singly Linked List.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/insertBefore.png" alt="comparison" width="350" height="auto">
</p>

### Doubly Linked Lists
A natural way to implement a positional list is with a doubly-linked list, so it is easy to quick to find the position before

Each ```Node``` in a ```Doubly Linked List``` stores
- its element, and
- a link to ```previous``` and ```next``` node

- A sequence of Nodes, each with preference to ```prev``` and to ```next```
- List captured by references, to its **Sentinel Nodes**
- We also have a ```header``` *(only has a next)* and a ```trailer``` *(only has a prev)*

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/doubly-linked-list.png" alt="comparison" width="350" height="auto">
</p>

#### Doubly Linked List: ```insertBefore(p,e)```
1. instantiate new Node ```x``` with element ```e```
2. update ```x.previous``` to point to ```p.previous```
3. update ```x.next``` to point to ```p```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/insertBeforedoubly.png" alt="comparison" width="350" height="auto">
</p>

4. update ```p.prev.next``` to point to ```x``` (finds the node originally before ```p```, then makes that node point to ```x``` as its next)
5. update ```p.prev``` to point to ```x```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/insertbeforedoubly2.png" alt="comparison" width="350" height="auto">
</p>

**Pseudo-code**:
```
def insert_before(pos, elem)
  // insert elem before pos
  // assuming it is a legal pos
    new_node <- create a new node
    new_node.element <- elem
    new_node.prev <- pos.prev
    new_node.next <- pos
    pos.prev.next <- new_node
    pos.prev <- new_node

    return new_node
```

#### Doubly Linked List: ```remove(p)```
1. point p.prev.next to p.next
2. point p.next.prev to p.prev
3. return removed element

**Pseudo-code**:
```
def remove(pos)
  // remove pos from the list
  // assuming it is a legal pos

    pos.prev.next <- pos.next
    pos.next.prev <- pos.prev

    return pos.element
```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/removedoubly.png" alt="comparison" width="350" height="auto">
</p>

### Performance
A **doubly linked list** can perform all of the accessor and update operations for a positional list in constant time ```O(1)```.

Space complexity is ```O(n)```.

Time complexity is ```O(1)```.

|Method             |Time   |
|-------------------|-------|
|first()            |O(1)   |
|last()             |O(1)   |
|before(p)          |O(1)   |
|after(p)           |O(1)   |
|insert_before(p,e) |O(1)   |
|insert_after(p,e)  |O(1)   |
|remove(p)          |O(1)   |
|size()             |O(1)   |
|is_empty()         |O(1)   |

### Array vs Linked List
**Linked List**
- good match to positional ADT
- efficient insertion and deletion
- simpler behaviour as collection grows
- modifications can be made as collection iterated over
- space not wasted by list not having maximum capacity

**Arrays**
- good match to index-based ADT
- caching makes traversal fast
- no extra memory needed to store pointers
- allow random access (retrieve element by index)

## Iterators
Abstracts the process of stepping through a collection of elements one at a time, by extending the concept of position.

Implemented by maintaining a cursor to the *"current"* element.

Two notions of iterator:
- snapshot freezes the contents of the data structure
- dynamic follows changes to the data structure

### Iterators in Python

```iter(obj)``` returns an **iterator** of the object collection.

To make a class *iterable*, define the method: ```__iter__(self)```.

The method ```__iter__(self)``` returns an object having a ```next()``` method

Calling ```next()``` returns the next object and advances the cursor or raises ```StopIteration()```.

```
for x in obj:
    // process x
```

is equivalent to

```
it = x.__iter__()
try:
    while True:
    x = it.next()
    // process x
except StopIteration:
    pass
```

## Stacks and queues
These ADTs are restricted forms of List, where insertions and removals only happen in particular locations
- stacks follow last-in-first-out (LIFO)
- queues follow first-in-first-out (FIFO)

We use these less general ADT:
- operations names are part of computing culture
- numerous application
- simpler/more efficient implementations than List

### Stack ADT
**Main stack operations**:
- ```push(e)```: inserts an element, ```e```
- ```pop()```: removes and returns the last inserted element

**Auxilliary stack operations**:
- ```top()```: returns the last inserted element without removing it
- ```size()```: returns the number of elements stored
- ```isEmpty()```: indicates if it is empty

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/stackprocess.png" alt="comparison" width="350" height="auto">
</p>

**Stack applications**:
Direct applications:
- Keep track of a history that allows undoing (e.g. text editor)
- Chain of method calls in a language supporting recursion
- Context free grammars

Indirect applications:
- Auxillary DS
- Component of other DS

### Method Stacks
The runtime environment keeps track of the chain of active methods with a stack, allowing **recursion**.

When a method is called, the system pushes on the stack, a frame containing:
- local variables and return value
- program counter

When a method ends, we pop its frame and pass control to the method on top.

#### Stack implementation based on arrays
A simple way of implementing the Stack ADT uses an array:
- Array with capacity ```N```
- Add elements from left to right
- A variable ```t``` keeps track of the index of the top element.

```
def size()
    return t + 1

def pop()
    if isEmpty() then
        return null
    else
        t = t - 1
        return S[t+1]
```

### Queue ADT
Like a "one-way" array"

**Main queue operations**:
- ```enqueue(e)```: inserts element ```e```, at the end of the queue
- ```dequeue(e)```: removes and returns element at the front of the queue

**Auxillary queue operations**:
- ```first()```: returns the element at the front without removing
- ```size()```: returns the number of elements stored
- ```isEmpty()```: indicates if there are no elements

**Boundary cases**
- Attempting execution of dequeue or first on empty queue brings error or returns null

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/queueprocess.png" alt="comparison" width="350" height="auto">
</p>

**Queue applications**:
Buffering packets in streams such as video or audio

Direct applications:
- Waiting lists, bureaucracy
- Access to shared resources (e.g., printer)
- Multiprogramming

Indirect application:
- Part of other DS

#### Queue implementation based on arrays
Use array of size ```N``` in a circular fashion.
Two variables keep track of the front and size
- ```start```: index of the front element
- ```end```: index past the last element
- ```size```: number of stored elements

These are related as follows:
```end = (start + size) mod N```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/queueimplementation.png" alt="comparison" width="350" height="auto">
</p>

**Wrapped-around configuration**
- Enqueue ```N``` elements
- Dequeue ```k < N``` elements
- Enqueue ```k' < k``` elements

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/wrapped.png" alt="comparison" width="350" height="auto">
</p>

#### Queue Operations: ```enqueue(e)```
Return error if array is full. Or grow underlying array as a dynamic array

```
def enqueue(e)
    if size = N then
        return "Queue full"
    else
        end = (start + size) % N // mod N
        Q[end] = e
        size = size + 1
```