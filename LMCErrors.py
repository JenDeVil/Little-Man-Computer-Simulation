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


class BadInstructionError(ValueError):
    def __init__(self, address: int, instruction: int):
        self.message = "Bad instruction at address " + str(address) + "\nInstruction [" + str(instruction) + "]"
        super().__init__(self.message)


class AdditionError(ArithmeticError):
    def __init__(self, register_value, value, max_value, ):
        self.message = "Value too big for memory location\n" + \
                       "Value in register [" + str(register_value) + "]\n" + \
                       "Max value [" + str(max_value) + "]\nGiven value [" + str(value) + "]"
        super().__init__(self.message)


class SubtractionError(ArithmeticError):
    def __init__(self, register_value, value, min_value):
        self.message = "Value too small for memory location\n" + \
                       "Value in register [" + str(register_value) + "]\n" + \
                       "Min value [" + str(min_value) + "]\nGiven value [" + str(value) + "]"
        super().__init__(self.message)
