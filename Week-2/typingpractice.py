'''
A Python script to help me understand the "typing" module in Python.
'''

# 1. Basic Type Hints
def greet(name: str) -> str:
    return f"Hello, {name}"
    # Here we annotate the expected data type of input
    # and output

# 2. Explore Common Types

from typing import List, Dict, Tuple, Set

def process_items(items: List[int]) -> None:
    pass

def scores() -> Dict[str, int]:
    return {"Alice": 90, "Bob": 95}

def coordinates() -> Tuple[int, int, int]:
    return (10, -1, 5)

def unique_numbers() -> Set[int]:
    return {1, 2, 3, 4}

# 3. Learn about Optional and Union Types

from typing import Optional, Union

customers_db = {
    1: {"name": "Alice", "age": 30, "email": "alice@example.com"},
    2: {"name": "Bob", "age": 25, "email": "bob@example.com"},
}

def find_customer(customer_id: int) -> Optional[Dict[str, str]]:
    """Fetch cx info using customer ID.
    Args: customer_id (int)
    Returns:
    Optional[Dict[str, str]]: Cx info, if found, if nothing, then None
    """

    return customers_db.get(customer_id, None)

def process_data(data: Union[str, List[str]]) -> None:
    # Function can handle both a string, or a list of strings
    pass

print(find_customer(0))
print(find_customer(1))

# 4. Get Familiar with Generics

from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

'''
TypeVar is a function used to define a generic type variable.
Allows us to write functions, methods, and classes which can operate
on any type, with the specific type being determined
when the function is called or class is instantiated.
'''