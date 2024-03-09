from typing import Generic, TypeVar, List
T = TypeVar('T')

"""
Tree Node
---------

This node represents a node in a Tree
Each node contains a value, a pointer to its parent and a list of children.
"""

class Node(Generic[T]):

    _value: T
    _parent: 'Node(T)'
    _children: List['Node[T]']
    _subtree_size: int

    """
    Node Class
    -init: Sets the basic information such as the value it holds and the next element
    -get_value: retrieves value of node
    -set_value: sets value for a certain node
    -get_parent: retrieves parent of node
    -add_child: adds the child node to list of children
    -get_children: returns the list of children
    -num_children: returns the number of children belonging to a node
    -is_internal: checks if the node is a non-leaf
    -is_external: checks if node is lead
    -is_root: checks if node is root
    """

    def __init__(self, value: T, parent: 'Node[T]' = None) -> None:
        """
        Initialization of the node, sets the value held by the node
        as well as the element it is linked to.
        :param value: the value of the node
        :param parent: parent of the node
        """
        self._value = value
        self._parent = parent
        self._children = []
        self.subtree_size = 1

    def get_value(self) -> T:
        """
        Getter method for the value of the node
        :return: the value of the node, which can be any data type T
        """
        return self._value
    
    def set_value(self, value: T) -> None:
        """
        Setter method for the value of the node
        :param value: the value we want to set the node to
        """
        self._value = value
    
    def get_parent(self) -> 'Node[T]':
        """
        Returns the parent of the node.
        :return: Node which is the parent of the given node
        """
        return self._parent
    
    def get_subtree_size(self) -> int:
        """
        Return subtree size of node
        :return: Integer that is the node's subtree size
        """
        return self.subtree_size
    
    def set_subtree_size(self, value: int) -> None:
        """
        Set subtree size to specified node.
        :param value: value to set the size to
        """