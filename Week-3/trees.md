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