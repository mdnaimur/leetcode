import random


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.list.append(val)
        self.val_to_index[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        last_element = self.list[-1]
        idx_to_remove = self.val_to_index[val]

        if idx_to_remove != len(self.list) - 1:
            self.list[idx_to_remove] = last_element
            self.val_to_index[last_element] = idx_to_remove

        self.list.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Example

random_set = RandomizedSet()

# Insert values
print(random_set.insert(1))  # Expected output: True (1 is inserted)
print(random_set.insert(2))  # Expected output: True (2 is inserted)
print(random_set.insert(3))  # Expected output: True (3 is inserted)

# Try inserting a duplicate value
print(random_set.insert(1))  # Expected output: False (1 is already present)

# Remove a value
print(random_set.remove(2))  # Expected output: True (2 is removed)

# Try removing a value that is not in the set
print(random_set.remove(2))  # Expected output: False (2 is no longer present)

# Get a random element from the set (should return either 1 or 3)
print(random_set.getRandom())  # Expected output: 1 or 3 (randomly chosen)
