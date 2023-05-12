import os
from time import sleep

from Memory import Memory
from Registers import ProgramCounter, InstructionRegister, AddressRegister, Accumulator
from LMCErrors import BadInstructionError, HaltedError


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
        self.prev_frame = []

    def pos(self, x, y):
        return "\033[%d;%dH" % (y, x)

    def draw_frame(self, width: int = None):
        if width is None:
            width = 10

        terminal_size = os.get_terminal_size().columns

        # Display the memory
        loc_width = self.memory.mem()[0].getMaxStrWidth()
        curr_frame = []

        line = ""
        for loc in range(len(self.memory.mem())):
            if loc != 0 and loc % width == 0:
                curr_frame.append(line)
                line = ""

            line += "[" + str(self.memory.mem()[loc]) + "] "
        curr_frame.append("")

        # Display the registers
        curr_frame.append("PC [" + str(self.pc) + "]")
        curr_frame.append("IR [" + str(self.ir) + "] AR [" + str(self.ar) + "]")
        curr_frame.append("AC [" + str(self.ac) + "]")

        # Display the out lines
        curr_frame.append("")
        curr_frame.append("-- Out --")

        out_line = ""
        for addr in self.out_vals:
            out_line += str(self.out_vals[addr])
            if len(out_line) == terminal_size:
                curr_frame.append(out_line)
                out_line = ""
        if out_line != "":
            curr_frame.append(out_line)
        else:
            curr_frame.append(" ")

        curr_frame.append("---------")

        for l in range(min(len(curr_frame), len(self.prev_frame))):  # Loop through the length of the smaller frame
            if curr_frame[l] == self.prev_frame[l]:  # If the lines are identical then just pass the loop
                pass

            if len(curr_frame[l]) <= len(self.prev_frame[l]):  # Find out which line is smaller
                smaller_line = curr_frame[l]
            else:
                smaller_line = self.prev_frame[l]

            for c in range(len(smaller_line)):  # Run through each character in the smaller line
                # When they don't match, replace it with the new character
                if curr_frame[l][c] != self.prev_frame[l][c]:
                    print(self.pos(c + 1, l + 1) + curr_frame[l][c])

            # If the current frame line is bigger than the previous frames line,
            # then add on the extra characters to the line we just drew
            if len(curr_frame[l]) > len(self.prev_frame[l]):
                print(self.pos(len(self.prev_frame[l]), l + 1) + curr_frame[l][c:] + " " * (terminal_size - c - 3))

        for i in range(len(self.prev_frame), len(curr_frame)):  # Draw the extra lines the new frame may add
            print(curr_frame[i] + " " * (terminal_size - len(curr_frame[i])))

        print(self.pos(0, len(curr_frame) + 2) + " " * terminal_size)
        print(self.pos(0, len(curr_frame)))

        self.prev_frame = []
        for line in curr_frame:
            self.prev_frame.append(line)

    def clearInput(self):
        print(self.pos(0, len(self.prev_frame) + 3) + " " * os.get_terminal_size().columns)
        print(self.pos(0, len(self.prev_frame)))

    def excecute(self, show: bool = None, wait: float = None):
        if show is None:
            show = False
        if wait is None:
            wait = -1

        if show:
            if wait < 0:
                input("Press ENTER to fetch instruction")
                self.clearInput()
            else:
                sleep(wait)

        # 1. Check the program counter for the memory location that contains the program instruction.
        # 2. Fetch the instruction from the memory location pointed to by the program counter and write it to the
        #    instruction and address register.
        loc = self.pc.read()
        instruction = str(self.memory.mem()[loc])

        if int(instruction) < 0:  # Checking for a bad instruction.
            raise BadInstructionError(loc, int(instruction))

        self.ir.write(int(instruction[1]))
        self.ar.write(int(instruction[2:]))

        if show:
            self.draw_frame()
            if wait < 0:
                input("Press ENTER to increment PC")
                self.clearInput()
            else:
                sleep(wait)

        # 3. Increment the program counter.
        self.pc.incr()

        if show:
            self.draw_frame()
            if wait < 0:
                input("Press ENTER to decode and excecute instruction")
                self.clearInput()
            else:
                sleep(wait)

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

                        # Tidy the screen after the input is taken
                        self.clearInput()
                    case "02":
                        self.out_vals[self.stp] = self.ac.read()
                    case "22":
                        self.out_vals[self.stp] = chr(self.ac.read())
                    case _:  # Default
                        raise BadInstructionError(self.pc.read() - 1, self.ir.read())
            case 0:
                if str(self.ar) == "00":
                    raise HaltedError()
                elif str(self.ar) == "01":
                    return True
                else:
                    raise BadInstructionError(self.pc.read() - 1, self.ir.read())
        if show:
            self.draw_frame()
            if wait < 0:
                input("Press ENTER to perform next cycle")
                self.clearInput()
            else:
                sleep(wait)
        self.stp += 1

    def read(self, idx) -> int:  # Get the value at the memory location at idx
        return self.memory[idx]

    def write(self, idx, val):  # Set the value at the memory location at idx to val
        self.memory[idx] = val

    def decode_from_file(self, file_name):
        loc = 0
        with open(file_name, "r") as f:
            lines = [line.replace("\n", " ").split(" ") for line in f.readlines()]

        labels = {}
        full_opcodes = ["ADD", "SUB", "STA", "ERR", "LDA", "BRA", "BRZ", "BRP", "HLT", "COB", "INP", "OUT", "OTC"]

        line_num = 0

        for line in lines:
            if line[0] not in full_opcodes and not str.isnumeric(line[0]):
                labels[line[0]] = line_num
            line_num += 1

        for line in lines:
            basic_opcodes = ["-_-", "ADD", "SUB", "STA", "ERR", "LDA", "BRA", "BRZ", "BRP"]

            if line[0] in labels.keys():
                print(str(loc) + " " + str(line))
                line[0] = line[1]
                if len(line) >= 3:
                    line[1] = line[2]

            if line[0] in basic_opcodes:
                opcode = basic_opcodes.index(line[0])
                if str.isnumeric(line[1]):
                    operand = int(line[1])
                else:
                    if line[1] in list(labels.keys()):
                        operand = int(labels[line[1]])
                        print(operand)
                    else:
                        print("Error when parsing line " + str(loc))
                        print(line)
                        exit(0)
            else:
                match line[0]:
                    case "HLT":
                        opcode = 0
                        operand = 0
                    case "COB":
                        opcode = 0
                        operand = 1
                    case "INP":
                        opcode = 9
                        operand = 1
                    case "OUT":
                        opcode = 9
                        operand = 2
                    case "OTC":
                        opcode = 9
                        operand = 22
                    case _:
                        if str.isnumeric(line[0]):
                            opcode = 0
                            operand = int(line[0])
                        else:
                            labels[line[0]] = line_num
            self.memory.mem()[loc].write(opcode * 100 + operand)
            loc += 1

        if loc < 99:
            for i in range(loc, 99):
                self.memory.mem()[loc].write(0)
        input()
