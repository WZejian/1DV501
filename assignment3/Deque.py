from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as first entry in deque
    def add_first(self, n):
        newnode = Node(n, None)      # Node to be added
        if self.head is None:        # An empty list
            self.head = newnode
        else:
            newnode.nxt = self.head
        self.head = newnode
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt       # Move to the next node
        s += "}"
        return s

    # Add element n as last entry in deque
    def add_last(self, n):
        newnode = Node(n, None)
        if self.head is None:     # An empty list
            self.head = newnode
        else:
            self.tail.nxt = newnode
        self.tail = newnode
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            node = self.tail
            return node.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            node = self.head
            return node.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        elif self.size == 1:
            rtn_val = self.head.value
            self.head = None
            self.tail = None
            self.size = 0
            return rtn_val      # Return the removed value
        else:
            rtn_val = self.head.value
            node = self.head
            node = node.nxt     # Move to the next node
            self.head = node
            self.size -= 1
            return rtn_val

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None

        elif self.size == 1:
            rtn_val = self.head.value
            self.head = None
            self.tail = None
            self.size = 0
            return rtn_val    # Return the deleted value
        else:
            node = self.head
            for i in range(self.size-2):
                node = node.nxt
            delete = node.nxt    # Node to be deleted
            node.nxt = delete.nxt = None  # By-pass node to be deleted
            self.tail = node
            self.size -= 1
            return delete.value
