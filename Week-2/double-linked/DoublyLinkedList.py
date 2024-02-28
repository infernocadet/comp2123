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
