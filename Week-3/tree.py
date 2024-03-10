
from treenode import Node
from typing import Generic, TypeVar, List

T = TypeVar('T')

"""
Tree
---------

This is the tree file which is the main data structure for this lesson. The tree 
contains a root node and each node can have an arbitrary number of children.

Your task is to implement the basic functions below.
"""

class Tree(Generic[T]):
    _size: int
    _root: Node[T]

    """
    Tree Class
    Holds nodes, which can have an arbitrary number of children, unless it is
    a leaf node, then it has 0 children.

    Each node in the Tree is type <class Node> defined in 'node.py'
    -init: sets up tree with specified root node
    -get_size: get size of tree
    -is_empty: check if tree is empty
    -is_root: check if node is root
    -is_leaf: check if node is lead
    -add_node: add given node as a child of specified parent
    -remove_node: remove node and the subtree rooted at that node from the tree
    -preorder: preorder traversal of tree
    -postorder: postorder traversal of tree
    """

    def __init__(self, root: Node[T]) -> None:
        """
        Initialise the Tree
        :param root: root node of the tree
        """
        self._root = root
        self._size = 0
        if root != None:
            self._size = 1
        
    def get_root(self) -> Node[T]:
        """
        Return the root node of the tree
        :return: root node
        """
        return self._root
    
    def get_size(self) -> int:
        """
        Return the size of the tree
        :return: size of tree
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Return true if tree is empty. Otherwise return false
        :return: True if tree is empty
        """
        return (self._size == 0)
    
    def is_root(self, p: Node[T]) -> bool:
        """
        Return true if given node is root of tree.
        :param p: node to check if is root of tree
        """
        return (p == self._root)
    
    def is_leaf(self, p: Node[T]) -> bool:
        """
        Check whether the given node p is a leaf node
        :param p: node to be checked
        """
        return (p.is_external())
    
    def add_node(self, p: Node[T], parent: Node[T]) -> None:
        """
        Add child node to a node in the tree
        Increase size of the tree by 1 as well
        :param p: the node to be added
        :param parent: parent of the node to be added
        """
        parent.add_child(p)
        p._parent = parent
        self._size += 1

        while parent:
            parent._subtree_size += 1
            parent = parent.get_parent()
    
    def remove_node(self, p: Node[T]) -> None:
        """
        Remove the entire subtree rooted at the given node from the tree
        If p is the root node, set the tree's root to be None
        Make sure each node's subtree size is appropriately updated
        :param p: Node to be removed from tree
        """

        if (self._root == p):
            self._root = None
            self._size = 0
        else:
            parent = p.get_parent()
            if parent:
                parent._children().remove(p)
                p._parent = None

                # updating subtree size for all ancestors
                while parent:
                    parent._subtree_size -= p._subtree_size()
                    parent = parent.get_parent()
            self._size -= p._subtree_size
        p._subtree_size = 0
        
    def preorder(self, p: Node[T], ls: List[Node[T]]) -> None:
        """
        Preorder traversal of the tree
        :param p: the node to visit
        :param ls: Add nodes in preorder fashion to this supplied list
        Note: Add a newly visited node to the end of the supplied list
        """
        if self.is_empty():
            return ls
        root = self._root
        if root == p:
            ls.append(p)
            return ls
        
        for child in root.get_children():
            preorder()
        

        """
        what do i want this algorithm to do:
        so it is gonna preorder traverse the tree until it reaches a certain node
        start at root
        visit each child
        add each node visited to a visited list
        if the current node
        """
        

        

        