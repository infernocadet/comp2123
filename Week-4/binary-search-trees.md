# Binary Search Trees
A **binary search tree** is a binary tree which stores **keys** (or **key-value pairs**) and satisfies the following **BST property**:

| :memo: NOTE          |
|:---------------------------|
| For any node v in the tree and and node ```u``` in the left subtree of ```v``` and any node ```w``` in the right subtree of ```v```, ```key(u) < key(v) < key(w)```|

A resulting property is that an **inorder traversal** of a binary search tree visits the keys in increasing order. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bst.png" width="350" height="auto">
</p>

## BST Implementation
To simplify the presentation of the algorithms, we only store keys (or key-value pairs) at **internal nodes**.

**External nodes** do not store items, and with careful coding, can be omitted, using null to refer to the external nodes.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/nullbst.png" width="350" height="auto">
</p>

## Searching with a Binary Search Tree
To search for a key ```k```, trace a downward path starting at the ```root```.

To decide whether to go left or to go right, we compare the key of the current node ```v``` with ```k```.

If we reach an external node, this means that the **key is not** in the data structure.

```
def search(k, v)
    if v.isExternal() then
    # unsuccessful search
    return v
    if k = key(v) then
    # successful search
    return v
    elif k < key(v) then
    # recurse on left subtree
    return search(k, v.left)
    else
    # that is, k > key(v)
    # recurse on right subtree
    return search (k, v.right)
```

## Binary Tree Searching Asymptotic Analysis

Runs in ```O(h)``` time, where ```h``` is the height of the tree.
- worst case is $h = n-1$
- best case is $h <= log_{2}n$

The best case scenario of binary tree searching occurs in a **balanced binary tree**, where the height of the tree is minimised for a given number of elements. The left and right subtrees of every node differ in height by no more than 1. In these trees, the height $h$ is approximately $log_{2}n$. There is a logarithmic relationship because in a perfectly balanced tree, each level doubles the number of nodes from the previous level.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bstanalysis.png" width="350" height="auto">
</p>

## Insertion

To perform operation ```put(k,o)```, we search for key ```k``` (using search).

If ```k``` is found, replace the corresponding value by ```o```.

If ```k``` is not found, let w be the external node reached by the search. Replace ```w``` with an internal node holding ```(k,o)```.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bstinsert.png" width="350" height="auto">
</p>

## Delete

To perform operation ```remove(k)```, search for key ```k``` (using search) to find the node ```w``` holding ```k```.

We distinguish between two cases
- ```w``` has one external child
- ```w``` has two internal children.

If ```k``` is not in the tree, we can throw an exception or do nothing depending on *ADT specs*.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bstinsert.png" width="350" height="auto">
</p>

### Deletion Case 1: One External Child

Suppose that the node ```w``` we want to remove has an external child, which we call ```z```. ```Remember, external children are treated as null.```

To remove ```w```:
- remove ```w``` and ```z``` from the tree
- promote the other child of ```w``` to take ```w```'s place.

This way, we preserve the BST property. 