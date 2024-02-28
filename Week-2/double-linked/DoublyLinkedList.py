from typing import Generic, TypeVar
from Node import Node

T = TypeVar('T')

"""
Doubly Linked List
----------

This class will represent your Doubly Linked List and will contain Nodes from the Node class which you have created.
It supports operations to get first and last element, get elements before and after a particular node, insert
nodes, remove a node, return the size of the doubly linked list and also check if list is empty.
"""

class DoublyLinkedList(Generic[T]):
    _size: int
    _head: Node[T]
    _tail: Node[T]

    def __init__(self, head: Node[T] = None) -> None:
        """
        The initialisation of the DoublyLinkedList sets the first node of the structure.
        :param head: the front node of the linked list
        """
        self._size = 1 if head else 0
        self._head = head
        self._tail = head
    

    def first(self) -> Node[T]:
        """
        Returns the first node of the linked list
        :return: the node at the front of the list
        """
        return self._head
    

    def last(self) -> Node[T]:
        """
        Return the last node of the linked list
        :return: the node at the end of the list
        """
        return self._tail
    

    def before(self, p: Node[T]) -> Node[T]:
        """
        Returns the node immediately before node p and returns None if there are no nodes prior.
        :param p: the given node
        :return: the node before the given node, P, or none if no nodes prior.
        """
        if p == self.first():
            return None
        elif p.get_prev() == None:
            return None
        return p.get_prev()
    

    def after(self, p: Node[T]) -> Node[T]:
        """
        Returns the node immediately after node p and returns None if there are no nodes after.
        :param p: the given node
        :return: the node after the given node, P, or none if no nodes after.
        """
        if p == self.last():
            return None
        elif p.get_next() == None:
            return None
        return p.get_next()
    

    def insert_before(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately after the node p.
        If the list is empty and p is None, insert e at the front of the list.
        Otherwise, if the list is not empty and p is None, return None.
        :param p: the node we want to insert e before
        :param e: the node we want to insert after p
        """
        if p == None:
            if self._size == 0:
                e.set_next(self._head)
                self._head = e
                self._size += 1
                return
            else:
                return None
        
        e.set_next(p)
        e.set_prev(p.get_prev())
        p.get_prev().set_next(e)
        p.set_prev(e)

        self._size += 1
        
    
    def insert_after(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately after the node p.
        If the list is empty and p is None, insert e at the front of the list.
        Otherwise, if the list is not empty and p is None, return None.
        :param p: The node we want to insert e after.
        :param e: The node to insert.
        """
        if p == None:
            if self._size == 0:
                e.set_next(self._head)
                self._head = e
                self._size += 1
                return
            else:
                return None
        
        e.set_next(p.get_next())
        e.set_prev(p)
        p.get_next().set_prev(e)
        p.set_next(e)

        if p == self.last():
            self._tail = e
        
        self._size += 1
    

    def remove(self, p: Node[T]) -> Node[T]:
        """
        Removes the node p from the doubly linked list and returns it.
        If p is not valid, return None
        :param p: the position of the node to be removed
        :return: the node that was removed
        """
        if self._size == 0 or p is None:
            return None


        if self.first() == p:
            if self.last() == p:
                self._head = None
                self._tail = None
                self._size -= 1
                return p
            self._head = p.get_next()
            p.get_next().set_prev(None)
            p.set_next(None)
            self._size -= 1
            return p
        if self.last() == p:
            self._tail = p.get_prev()
            p.get_prev().set_next(None)
            p.set_prev(None)
            self._size -= 1
            return p
        
        p.get_prev().set_next(p.get_next())
        p.get_next().set_prev(p.get_prev())
        p.set_next(None)
        p.set_prev(None)
        self._size -= 1
        return p


    def size(self) -> int:
        return self._size

    
    def is_empty(self) -> bool:
        return (self._size == 0)


        
        
