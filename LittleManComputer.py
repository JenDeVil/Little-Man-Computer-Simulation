import os
from Memory import Memory
from Registers import ProgramCounter, InstructionRegister, AddressRegister, Accumulator
from LMCErrors import BadInstructionError


class LittleManComputer:
    def __init__(self):
        self.memory = Memory(100)
        self.pc = ProgramCounter()
        self.ir = InstructionRegister()
        self.ar = AddressRegister()
        self.ac = Accumulator()
        self.stp = 0
        self.out_vals = {}
        self.in_vals = {}

    def display(self, width: int = None):
        if width is None:
            width = 10

        os.system("cls")

        # Display the memory
        loc_width = self.memory.mem()[0].getMaxStrWidth()

        for loc in range(len(self.memory.mem())):
            if loc != 0 and loc % width == 0:
                print()

            print("[" + str(self.memory.mem()[loc]), end="] ")
        print("\n")

        # Display the registers
        print("PC [" + str(self.pc) + "]\nIR [" + str(self.ir) + "] AR [" + str(self.ar) + "]")
        print("AC [" + str(self.ac) + "]")

        # Display the in and out lines
        print("\n-- In  --")
        for addr in self.in_vals:
            print("[" + str(addr) + "] " + str(self.in_vals[addr]))
        print("---------")

        print("\n-- Out --")
        for addr in self.out_vals:
            print("[" + str(addr) + "] " + str(self.out_vals[addr]))
        print("---------")

    def excecute(self):
        # 1. Check the program counter for the memory location that contains the program instruction.
        # 2. Fetch the instruction from the memory location pointed to by the program counter and write it to the
        #    instruction and address register.
        loc = self.pc.read()
        instruction = str(self.memory.mem()[loc])

        if int(instruction) < 0:  # Checking for a bad instruction.
            raise BadInstructionError(loc, int(instruction))

        self.ir.write(int(instruction[1]))
        self.ar.write(int(instruction[2:]))

        # 3. Increment the program counter.
        self.pc.incr()

        # 4. Decode the instruction in the instruction register.
        match self.ir.read():
            case 1:
                add_val = self.read(self.ar.read())
                self.ac.add(add_val)
            case 2:
                sub_val = self.read(self.ar.read())
                self.ac.sub(sub_val)
            case 3:
                self.write(self.ar.read(), self.ac.read())
            case 4:
                raise BadInstructionError(self.pc.read() - 1, self.ir.read())
            case 5:
                self.ac.write(self.read(self.ar.read()))
            case 6:
                self.pc.write(self.ar.read())
            case 7:
                if self.ac.read() == 0:
                    self.pc.write(self.ar.read())
            case 8:
                if self.ac.read() > 0:
                    self.pc.write(self.ar.read())
            case 9:
                match str(self.ar):
                    case "01":
                        inp = int(input("\nTaking Input: "))
                        self.in_vals[self.pc.read() - 1] = inp
                        self.ac.write(inp)
                    case "02":
                        self.out_vals[self.stp] = self.ac.read()
                    case "22":
                        self.out_vals[self.stp] = chr(self.ac.read())
            case 0:
                if str(self.ar) == "00":
                    return True
        self.stp += 1

    def read(self, idx) -> int:  # Get the value at the memory location at idx
        return self.memory[idx]

    def write(self, idx, val):  # Set the value at the memory location at idx to val
        self.memory[idx] = val
