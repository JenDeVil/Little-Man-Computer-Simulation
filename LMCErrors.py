class MemoryIndexError(IndexError):
    def __init__(self, key: int, max_idx: int):
        self.message = "Index out of range of memory\nGiven index [" + str(key) + \
                       "]\nMemory range [0, " + str(max_idx - 1) + "]"
        super().__init__(self.message)


class MemoryLocationValueError(ValueError):
    def __init__(self, min_val: int, max_val: int, val: int):
        self.message = "Value out of bounds for memory location\n" \
                       "Location bounds [" + str(min_val) + ", " + str(max_val) + \
                       "]\nGiven value [" + str(val) + "]"
        super().__init__(self.message)
