from Node import Node
from typing import Generic, TypeVar

T = TypeVar('T')
"""
Singly Linked List

Each node contains a value, and a link to the next node.
Supports elements to set and get element and operations to set and get the element it is linekd to.

The Singly Linked List contains Nodes from the Node class. It supports operations to get the first and last element, check before and after a particular node, insert an element before or after a particular node, remove a node, check size of list and also check if the list is empty.
"""

class singly_ll(Generic['T']):
    """
    Singly_ll Class
    Holds nodes, which each has a next node unless it is the end node, where the next Node is none.
    """

    _size: int
    _front: Node[T]
    _back: Node[T]

    def __init__(self, first_node: Node[T]) -> None:
        """
        Initialises the Singly LL with the starting node. Front and back are the same node. Size is the number of the nodes in the list.
        :param size: The number of nodes in the list
        :param front: First node of the Linked List
        :param back: Last node of the Linked list
        """
        self._size = 1
        self._front = first_node
        self._back = first_node
    
    
    def first(self) -> Node[T]:
        """
        Returns the first node in the List
        """
        return self._front
    

    def last(self) -> Node[T]:
        """
        Returns the last node in the List
        """
        return self._back
    
    def after(self, p: Node[T]) -> Node[T]:
        """
        Returns the node immediately after node p.
        If p is None return None
        :return: The node after p
        """
        if p == None:
            return None
        return p.get_next()
    
    def insert_after(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately after node P. If p is None, then add e at the first position of the list.
        :param p: Node object which Node e is to be inserted after If None then add e to the first pos
        :param e: Node object to be inserted
        """
        # if there is no p
        if p == None:
            if self._size == 0:
                self._back = e
            else:
                e.set_next(self._front)
            self._front = e
        else:
            e.set_next(p.get_next())
            p.set_next(e)
            if self._back == p:
                self._back = e
        self._size += 1
        
    
    def remove(self, p: Node[T]) -> Node[T]:
        """
        Removes node p from list and joins the node previous from p to the node after p. If p is first node then just remove p and change first accordingly. If p is none return None.
        :param p: Node object that is to be removed
        :return: the node that was removed
        """
     
        if p == None:
            return None

        if self._front == p:
            self._front = p.get_next()
            if self._back == p:
                self._back = None
            self._size -= 1
            return p
        
        current_node = self._front
        while current_node is not None and current_node.get_next() != p:
            current_node = current_node.get_next()
        
        if current_node is None:
            return None
        
        if self._back == p:
            self._back = current_node
        
        current_node.set_next(p.get_next())
        self._size -= 1
        return p
    

    def size(self) -> int:
        """
        Returns the size of the singly linked list
        :return: size of the list
        """
        return self._size
    

    def is_empty(self) -> bool:
        """
        Returns if the singly linked list is empty of not.
        :return: True or False depending if list is empty or not.
        """
        return (self._size == 0)

        
        
    