# ----------------------------------------------------
# Intuition:
#
# 1. Naive Buffer Using None Sentinel:
#    - Cache the peeked value in a variable initialized to None.
#    - If None means "no cached value", but if the underlying iterator
#      can return None as a valid element, this breaks.
#    - Simple, but limited to iterators that never return None.
#
# 2. Robust Buffer Using Boolean Flag:
#    - Use a boolean flag _has_peeked to explicitly track whether
#      the peeked value is buffered.
#    - Works correctly even if the iterator returns None as a valid value.
#    - Slightly more code, but safer and more general.
# ----------------------------------------------------

# ----------------------------------------------------
# 1. Naive Approach (None sentinel)
# Time: O(1) per operation, Space: O(1)
# ----------------------------------------------------
class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        if self.iterator.hasNext():
            self.next_elem = self.iterator.next()
        else:
            self.next_elem = None 

    def peek(self):
        if not self.hasNext():
            raise Exception("No elements left to peek")
        return self.next_elem

    def next(self):
        curr = self.next_elem
        if self.iterator.hasNext():
            self.next_elem = self.iterator.next()
        else:
            self.next_elem = None

        return curr

    def hasNext(self):
       return self.next_elem is not None

# ----------------------------------------------------
# 2. Robust Approach (explicit boolean flag)
# Time: O(1) per operation, Space: O(1)
# ----------------------------------------------------
class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        self._has_peeked = False
        self._peek_val = None

    def peek(self):
        if not self._has_peeked:
            self._peek_val = self.iterator.next()
            self._has_peeked = True
        return self._peek_val

    def next(self):
        if self._has_peeked:
            self._has_peeked = False
            return self._peek_val
        return self.iterator.next()

    def hasNext(self):
        return self._has_peeked or self.iterator.hasNext()


# ----------------------------------------------------
# Example usage and test cases:
# ----------------------------------------------------

if __name__ == "__main__":
    # Mock Iterator class for testing
    class Iterator:
        def __init__(self, nums):
            self.nums = nums
            self.index = 0

        def hasNext(self):
            return self.index < len(self.nums)

        def next(self):
            val = self.nums[self.index]
            self.index += 1
            return val

    nums = [1, 2, 3]

    # Using robust PeekingIterator
    iter_obj = PeekingIterator(Iterator(nums))

    print(iter_obj.peek())   # Output: 1 (peek does not advance)
    print(iter_obj.next())   # Output: 1 (returns peeked value)
    print(iter_obj.next())   # Output: 2
    print(iter_obj.peek())   # Output: 3
    print(iter_obj.hasNext()) # Output: True
    print(iter_obj.next())   # Output: 3
    print(iter_obj.hasNext()) # Output: False
