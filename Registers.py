from MemLoc import MemLoc


class ProgramCounter(MemLoc):
    def __init__(self):
        super().__init__(0, 99, 0)

    def incr(self):
        self.write(self.read() + 1)


class AddressRegister(MemLoc):
    def __init__(self):
        super().__init__(0, 99, 0)


class InstructionRegister(MemLoc):
    def __init__(self):
        super().__init__(0, 9, 0)


class Accumulator(MemLoc):
    def __init__(self):
        super().__init__(-999, 999, 0)
