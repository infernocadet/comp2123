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
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bstdelete0.png" width="350" height="auto">
</p>

### Deletion Case 1: One External Child

Suppose that the node ```w``` we want to remove has an external child, which we call ```z```. ```Remember, external children are treated as null.```

To remove ```w```:
- remove ```w``` and ```z``` from the tree
- promote the other child of ```w``` to take ```w```'s place.

This way, we preserve the BST property. 

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bstdelete1.png" width="350" height="auto">
</p>

### Deletion Case 2: Two Internal Children

Suppose that the node ```w``` we want to remove has two internal children.

To remove ```w```, we 
- find the internal node ```y``` following ```w``` in an ```inorder traversal``` (i.e., ```y``` has the smallest key among the right subtree under ```w```)
- copy the entry from ```y``` into node ```w```
- remove node ```y``` and its left child ```z```, which must be external using the previous case.

This preserves the BST property.

### Deletion Algorithm

```python
def remove(k)
    w = search(k, root)
    if w.isExternal():
        # key was not found
        return null
    elif w has at least one external child:
        remove z
        promote w.child to take w's place
        remove w
    else
        # y is leftmost internal node in the right subtree of w
        y = immediate successor of w
        replace contents of w with entry from y
        remove y
```

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bstdelete2-1.png" width="350" height="auto">
</p>

## Complexity

Consdier a binary search tree with ```n``` items and height ```h```:
- the space used is ```O(n)```
- get, put and remove take ```O(h)``` time

The height ```h``` can be ```n``` in the worst case and approximately ```log(n)``` in the best case.

We hope operations take ```O(logn)``` time but we can only guarantee ```O(n)```. However, the former can be achieved with better insertion techniques (i.e., making sure the tree is balanced.)

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/bstcomplexity.png" width="350" height="auto">
</p>

### Duplicate key values in BST

Our definition says that keys are in **strictly increasing order**:
```key(left descendant) < key(node) < key(right descendant)```

This means, that with this definition, duplicate key values are not allowed. However, it is possible to change it to allow duplicates, but it means for additional complexity in BST implementation.
- Allow left descendants to be equal to parent: ```key(left descendant) ≤ key(node) < key (right descendant)```
- We can use a list to store duplicates.

## Range Queries

A **range query** is defined by two values, $k_{1}$ and $k_{2}$. We are to find all keys ```k``` stored in ```T``` such that $k_{1} <= k <= k_{2}$

E.g., find all cars on eBay priced between 10k and 15k.

The algorithm is a restricted version of inorder traversal.

We use a recursive method, e.g. ```RangeQuery()``` which takes $k_{1}$ and $k_{2}$, and a node ```v```. If the node ```v``` is external, we return. If the node ```v``` is internal:

When at node ```v```:
- if ```key(v) < k1```: recursively search right subtree
- if ```k1 ≤ key(v) ≤ k2```: report ```v``` and recursively search both children of ```v```.
- if ```k2 < key(v)```: recursively search left subtree

``` python
def range_search(T, k1, k2)
    output = List[]
    range_query(T.root, k1, k2)


def range_query(v, k1, k2)
    if v.isExternal():
        return null
    if key(v) > k2:
        range(v.left, k1, k2)
    elif key(v) < k1 then:
        range(v.right, k1, k2)
    else
        range(v.left, k1, k2)
        output.append(v)
        range(v.right, k1, k2)
```

### Performance
Let $P_{1}$ and $P_{2}$ be the binary search paths to $k_{1}$ and $k_{2}$.

We say a node ```v``` is a:
- **boundary node** if ```v``` in $P_{1}$ or $P_{2}$
- inside node if ```key(v)``` in $[k_{1}, k_{2}]$ but not in $P_{1}$ or $P_{2}$
- outside node if ```key(v)``` not in $[k_{1}, k_{2}]$ but not in $P_{1}$ or $P_{2}$

The algorithm only visits boundary and inside nodes and
- $|\text{inside nodes}| <= |\text{output}|$
- $|\text{boundary node}| <= 2*\text{tree height}$

Therefore, since we only spend ```O(1)``` time per node we visit, the total running time of range search is ```O(|output| + treeheight)```.

Thus:
| :memo: NOTE          |
|:---------------------------|
| The space used is ```O(n)```. |
| Operation ```FindAllinRange()``` takes $O(h+s)$ time, where s is the number of nodes reported.  |
| Operations ```insert()``` and ```remove()``` take ```O(h)``` time.

## Maintaining a Balanced BST
Operations on BSTs can take $O(\text{height})$ to run.

Standard insertion implementation can lead to a tree with height $n-1$.

We can implement algorithms that maintain a BST with height $O(height)$ by rebalancing the tree.

This directly translates into $O(log_{2}n)$ for searching.

### Rank-balanced Trees

A family of balanced BST implementations which uses the idea of keeping a "rank" for every node, where ```r(v)``` acts as a proxy measure of the size of the subtree, rooted at ```v```.

Rank-balanced trees aim to reduce the discrepancy between the ranks of the left and right subtrees.
- AVL Trees
- Red-Black Trees

### AVL Trees
AVL trees are rank-balanced trees, where ```r(v)``` is its height of the subtree rooted at ```v```.

**Balance constaint**: The ranks of the two children of every internal node, differ by at most, 1.

<p align="center">
    <img src="https://github.com/infernocadet/comp2123/blob/main/graphics/avl.png" width="350" height="auto">
</p>

### Height of an AVL tree

Fact: The height of an AVL tree storing ```n``` nodes is $O(log_{2}n)$.

Proof by induction:

$$
\text{Let } N(h) \text{ be the minimum number of keys of an AVL tree of height h.}
$$
$$
\text{We easily see that } N(1) = 1 \text{ and } N(2) = 2
$$ 
