import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # If the list is empty
        if len(self.storage) <= 0:
            # Add the first item to the list (head)
            return self.storage.add_to_head(value)
        # If the list already contains data
        elif len(self.storage) > 0:
            # Add an item to the back of the stack (tail)
            return self.storage.add_to_tail(value)
        # Else return nothing
        else:
            return None

    def pop(self):
        # If the size of the list is greater than zero
        if len(self.storage) > 0:
            # Remove the item at the back of the stack (tail)
            return self.storage.remove_from_tail()
        # Else return nothing
        else:
            return None

    def len(self):
        # Returns the number of items in the stack
        return len(self.storage)

## ------------------------------------------------------------
## ------------------------Regular List-----------------------
## ------------------------------------------------------------

    # def __init__(self):
    #     self.size = 0
    #     # Why is our DLL a good choice to store our elements?
    #     self.storage = []

    # def push(self, value):
    #     # If the list is empty or contains data
    #     if len(self.storage) >= 0:
    #         # Add an item to the back of the stack
    #         self.storage.append(value)
    #         # Increases the size of the list by one
    #         self.size += 1
    #     else:
    #         return None

    # def pop(self):
    #     # If the size of the list is greater than zero
    #     if len(self.storage) > 0:
    #         # Shrink our list by one
    #         self.size -+ 1
    #         # Remove the item at the back of the stack (tail)
    #         return self.storage.pop()
    #     # Else return nothing
    #     else:
    #         return None

    # def len(self):
    #     # Returns the number of items in the stack
    #     return len(self.storage)