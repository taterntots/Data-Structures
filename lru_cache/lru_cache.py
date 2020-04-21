import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit # Limit Keeps track of the maximum number of nodes available to hold
        self.size = 0 # Size keeps track of the number of nodes
        self.list = DoublyLinkedList() # DLL that holds key:value pairs in the correct order
        self.hash_storage = {} # Dictionary to store key:value pairs

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If the key is not in our hash table
        if key not in self.hash_storage:
            # Do nothing (nothing to retrieve)
            return None
        # If the key is in our hash table
        else:
            # Move it to the front (head)
            self.list.move_to_front(self.hash_storage[key])
            # Return that keys value
            return self.hash_storage[key].value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # If the key-value pair is already in our cache
        if key in self.hash_storage:
            # Replace the old key's value with the new one
            self.hash_storage[key].value = (key, value)
            # Move the updated key:value pairing to the front
            self.list.move_to_front(self.hash_storage[key])
            return
        
        # If the cache is at maximum capacity
        if self.size == self.limit:
            # Remove the oldest entry from the cache dictionary and DLL to make room (tail)
            del self.hash_storage[self.list.tail.value[0]] # Removes LRU from the cache dictionary
            self.list.remove_from_tail() # Removes LRU from the DLL
            # Decrease the size of the cache by one
            self.size += 1
        
        # Otherwise add the new key-value pair to the cache and move to front (head)
        self.list.add_to_head((key, value)) # adds to the DLL
        self.hash_storage[key] = self.list.head # adds to the cache dictionary
        # Increase the size of the cache by one
        self.size += 1