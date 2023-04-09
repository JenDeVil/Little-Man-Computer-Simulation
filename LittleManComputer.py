import os
from Memory import Memory
from ProgramCounter import ProgramCounter


class LittleManComputer:
    def __init__(self):
        self.memory = Memory(100)
        self.pc = ProgramCounter()
        self.out_vals = []
        self.in_vals = []

    def display(self, width: int = None):
        if width is None:
            width = 10

        os.system("cls")

        # Display the memory
        loc_width = self.memory.mem()[0].getMaxStrWidth()

        for loc in range(len(self.memory.mem())):
            if loc != 0 and loc % width == 0:
                print()

            print("[" + self.memory.mem()[loc].getValueStr(), end="] ")
        print("\n")

        # Display the registers
        print("PC [" + self.pc.getValueStr() + "]")

        # Display the in and out lines
        print("\n-- In  --")
        for i in range(len(self.in_vals)):
            print("[" + str(i) + "] " + str(self.in_vals[i]))
        print("---------")

        print("\n-- Out --")
        for o in range(len(self.out_vals)):
            print("[" + str(o) + "] " + str(self.out_vals[o]))
        print("---------")

    def loc(self, idx) -> int:  # Get the value at the memory location at idx
        return self.memory[idx]

    def setloc(self, idx, val):  # Set the value at the memory location at idx to val
        self.memory[idx] = val
