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