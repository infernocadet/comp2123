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