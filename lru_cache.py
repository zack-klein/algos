"""
https://leetcode.com/problems/lru-cache/
"""


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.storage = {}
        self.usage_queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.storage:
            # Reorder the queue
            queue_position = self.usage_queue.index(key)  # $$$, optimize
            self.usage_queue.pop(queue_position)
            self.usage_queue.append(key)
            return self.storage[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.storage) == self.capacity and key not in self.storage:
            lru = self.usage_queue.pop(0)
            del self.storage[lru]

        self.storage[key] = value

        if key in self.usage_queue:
            queue_position = self.usage_queue.index(key)  # $$$, optimize
            self.usage_queue.pop(queue_position)

        self.usage_queue.append(key)
