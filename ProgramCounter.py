from MemLoc import MemLoc


class ProgramCounter(MemLoc):
    def __init__(self):
        super().__init__(0, 99, 0)

    def incr(self):
        self.setValue(self.getValue() + 1)
