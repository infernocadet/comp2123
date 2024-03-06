cSpell:ignore Preorder, Postorder

# Trees
*Content covered*:
- Definition and terminology
- Applications
- Tree ADT
- Tree traversal algorithms
- Binary trees
- Implementing trees
- Recursive code on trees

## Introduction to Trees
A tree is an abstract model of a **hierarchical structure**. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/trees.png" alt="comparison" width="350" height="auto">
</p>

A tree consists of nodes with a parent-child relation.
- if ```u``` is a ```parent``` of ```v```, then ```v``` is a ```child``` of ```u```.
- a ```node``` has at most **one** parent in a tree.
- a ```node``` can have 0, one or more children.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/structure.png" alt="comparison" width="350" height="auto">
</p>

### Formal definition
A ```tree T``` is made up of a set of ```nodes``` endowed with a **parent-child** relationship with the following properties:
- if ```T``` is *non-empty*, it has a special ```node``` called the ```root``` which **has no parent**
- every ```node v``` of ```T``` other than the root has a unique ```parent```
- following the parent relation always leads to the root. the tree is **non-cyclical**

### Tree Terminology
We can classify ```nodes``` into three **categories**:
- **Root**: ```node``` without a ```parent``` (would be A in this diagram)
- **Internal Node**: ```node``` with at least one child (A, B, C, F)
- **External/Lead Node**: ```node``` without children (E, I, J, K, G, H, D)

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/treediagram.png" alt="comparison" width="350" height="auto">
</p>

We can extend the parent-child relation to capture indirect relations:
- **Ancestors**: parent, grandparent, great-grandparent etc (e.g., ancestors of F are A, B)
- **Descendants**: child, grandchild, great-grandchild etc (e.g. descendants of B are E, F, I, J, K)
- **Siblings**: two nodes with the same parent (e.g. B and D)

More fine-grained location concepts:
- **Depth of a node**: number of ancestors of a node, not including itself (e.g. ```depth(F) = 2```)
- **Level**: set of nodes with a given depth (e.g., {E, F, G, H} are level 2)
- **Height of a tree**: maximum depth of a tree (e.g., 3)

Substructures of a tree:
- **Subtree**: tree made up of some node and its *descendants*. e.g., subtree *rooted* at C is {C, G, H}
- **Edge**: pair of nodes ```(u, v)``` such that one is the parent of the other
- **Path**: sequence of nodes, such that 2 consecutive nodes in the sequence have an edge, e.g. ```(<E, G, F J>)```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/treeterm.png" alt="comparison" width="350" height="auto">
</p>

### Tree facts
- If a node ```X``` is an ancestor of node ```Y```, then ```Y``` is a descendant of ```X```
- Ancestor/descendant relations are transitive
- Every node is a descendant of the ```root```
- There may be nodes where neither an ancestor of the other
- Every pair of nodes has at least one common ancestor
- The **lowest common ancestor (LCA)** of ```x``` and ```y``` is a node ```z``` such that ```z``` is the ancestor of ```x``` and ```y``` and no descendant of ```z``` has that property.

## Ordered Trees
Sometimes, the order of siblings matter.

In an **ordered tree**, there is a prescribed order for each node's children.

In a diagram, this ordering is usually represented by the left to right arrangement of nodes.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/orderedtree.png" alt="comparison" width="350" height="auto">
</p>

These can be applied in a file structure, document structure or even a **Phrase structure tree**.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/phase.png" alt="comparison" width="350" height="auto">
</p>

## Tree ADT (Abstract Data Type)
- Position as Node abstraction.
- **Generic methods**:
    - integer ```size()```
    - boolean ```isEmpty()```
    - Iterator ```iterator()```
    - Iterable ```positions()```
- **Access methods**:
    - Position ```root()```
    - Position ```parent(p)```
    - Iterable ```children(p)```
    - Integer ```numChildren(p)```
- **Query methods**:
    - boolean ```isInternal(p)```
    - boolean ```isExternal(p)```
    - boolean ```isRoot(p)```

### Node object
Node object implementation has the following attributes:
- ```value```: the value associated with the Node
- ```children```: ```set``` or ```list``` of ```children``` of this node
- ```parent```: *(optional)* the parent of the node

```
def is_external(p):
    # test is p is a leaf
    return p.children.is_empty()

def is_root(p):
    # test is p is root
    return p.parent = null
```

## Traversing trees

A **traversal** visits the nodes of the tree in a *systematic manner*.

A tree is more complex, and allow more than one natural way to traverse it:
- **pre-order**
- **post-order**
- **in-order** (for binary tree)

### Preorder Traversal
To do a preorder traversal, starting at a given ```node```, we visit the node **before** visiting its descendants.

If a tree is ordered, visit the child subtrees in the prescribed order.

By **visiting**, we mean do work on the node. So we see the node, process it etc:
- print node data
- aggregate node data
- modify node data

and then we can visit the child!

```
def pre_order(v):
    visit(v)
    for child w in v.children:
        pre_order(w)
```

Here, nodes are numbered in the order they are visited when we call ```pre_order()``` at the root.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/preorder.png" alt="comparison" width="350" height="auto">
</p>

### Postorder Traversal
To do a postorder traversal, starting at a given node, we visit the node **after** the descendants.

If tree is ordered, visit the child subtrees in the prescribed order.

Visit does work on the node:
- print node data
- aggregate node data
- modify node data

```
def post_order(v)
    for child w in v.children:
        post_order(w)
    visit(v)
```

## Binary trees

A **binary tree** is an ordered tree with the following properties:
- Each internal node has **at most TWO children**
- Each child node is labeled as a ```left child``` or ```right child```
- Child ordering is left followed by right

The right/left subtree is the subtree root at the right/left child.

A tree is **proper** is every internal node has two children

### Binary tree application: Arithmetic expression tree

Binary tree associated with arithmetic expression:
- internal nodes: operators
- external nodes: operands

An example arithmetic expression tree for $$(2 * (a - 1) + (3 * b))$$

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/arithmetic.png" alt="comparison" width="350" height="auto">
</p>

### Binary tree application: Decision tree

Tree associated with a decision process
- internal node: question with yes/no answer
- external node: decision

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/dining.png" alt="comparison" width="350" height="auto">
</p>

### Binary Tree Operations
A **binary tree** extends the Tree operations, meaning it inherits all normal methods of a tree.

Additional methods a binary tree can heave include:
- position ```leftChild(p)```
- position ```rightChild(p)```
- position ```sibling(p)```

return ```null``` when there is no ```left```, ```right```, or ```sibling``` of ```p```.

