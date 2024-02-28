from typing import Generic, TypeVar

T = TypeVar['T']

class Node(Generic[T]):

    _value: int
    _next: 'Node[T]'
    _prev: 'Node[T]'

    def __init__(self, value: T, next: 'Node[T]' = None, prev: 'Node[T]' = None) -> None:
        """
        Initialisation of a node: sets the value of node and linked elements
        :param value: the value linked to the node
        :param next: the next linked element
        :param prev: the previous linked element
        """
        self._value = value
        self._next = next
        self._prev = prev
    

    def get_value(self) -> T:
        """
        Getter method which returns the value of the node
        :return: the value of the node
        """
        return self._value
    
    
    def set_value(self, value: T) -> None:
        """
        Setter method which sets the value of the node
        :param value: the value to set the node to
        """
        self.value = value

    
    def get_next(self) -> 'Node[T]':
        """
        Returns the node after the current node.
        :return: the node which follows the given node
        """
        return self._next
    

    def set_next(self, next: 'Node[T]') -> None:
        """
        Sets the node which follows the existing node
        :param next: the node following the current one
        """
        self._next = next
    

    def get_prev(self) -> 'Node[T]':
        """
        Getter method which returns the previous node
        :return: the node before the given
        """
        return self._prev

    
    def set_prev(self, prev: 'Node[T]') -> None:
        """
        Setter method which sets the previous node
        :prev: the node before the given
        """
        self._prev = prev