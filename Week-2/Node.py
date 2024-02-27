from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):

    def __init__(self, value: T, next: 'Node[T]' = None):
        """
        Initialisation of the node which sets the value held by the node as well the the element it is linked to.
        :param value: the value of the node
        :param next: the next element after the node
        """
        self._value = value
        self._next = next
    
    def get_value(self) -> T:
        """
        Getter method for the value of the node
        :return: the value of the node
        """
        return self._value
    
    def set_value(self, value: T) -> None:
        """
        Setter method for the value of the node
        :param value: the value to set the node to.
        """
        self._value = value
    
    def get_next(self) -> T:
        """
        Returns the next node linked to the current Node.
        :return: Node which follows this given node.
        """
        return self._next
    
    def set_next(self, next: 'Node[T]') -> None:
        """
        Sets the next node linked to the current node.
        :param next: The node that comes after the current one
        """
        self._next = next
