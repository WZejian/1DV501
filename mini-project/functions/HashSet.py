from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hs_val = 0
        for e in word:
            hs_val += ord(e)
        return hs_val

    # Doubles size of bucket list
    def rehash(self):
        buck_cp = self.buckets.copy()
        self.buckets.clear()
        self.buckets = [[] for i in range(self.size*2)]
        for lst in buck_cp:
            for name in lst:
                self.add(name)
        self.size = len(self.buckets)//2

    def add(self, word):
        if self.size == len(self.buckets):
            self.rehash()
        n = self.get_hash(word) % len(self.buckets)
        if word not in self.buckets[n]:
            self.buckets[n].append(word)
            self.size += 1

    def to_string(self):
        string = '{'
        for lst in self.buckets:
            for s in lst:
                string += s + ' '
        string += '}'
        return string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hash_val = self.get_hash(word)
        n = hash_val % len(self.buckets)
        bucket = self.buckets[n]
        if word in bucket:
            return True
        return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        hash_val = self.get_hash(word)
        n = hash_val % len(self.buckets)
        bucket = self.buckets[n]
        if word in bucket:
            bucket.remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        size = 0
        for ls in self.buckets:
            if len(ls) > size:
                size = len(ls)
        return size
