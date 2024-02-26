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

## Index-Based Lists (List ADT)
An index-based list typically supports the following operations:

```size```  (int) number of elements in the store
```isEmpty()``` (boolean) whether or not the store is empty