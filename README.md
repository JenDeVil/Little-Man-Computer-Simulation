# Little-Man-Computer-Simulation
This is a console adaptation of the Little man computer simulation recreated in Python, based off of the Javascript application by Peter Higginson at https://peterhigginson.co.uk/lmc, which is in turn based off of the origonal design created by Dr. Stuart Madnick in 1965.

The Little man computer simulation is a (very simple) simulation of a computer using the Von Neumann architecture. The computers specifications are as follows

- 100 main memory locations (with bounds of -999 to 999)
- A `Program Counter (PC)` (with bounds of 0 to 99)
- An `Instruction Register (IR)` (with bounds of 0 to 9)
- An `Address Register (AR)` (with bounds of 0 to 99)
- An `Accumulator (AC)` (with bounds of -999 to 999)
- An `Arithmatic Logic Unit` (OK, *technically* it's in the program, but it isn't it's own class and the registers themselves do the maths, which is bad ik, but cut me some slack? tbh, it'd be easy to implement, might do that in a 1.x version)

The simulator also contains extra bits such as `in_vals`, `out_vals` and the `stp` variable, which we'll get onto when talking about the classes.

# Instruction Set

Note: `x` means *any* digit of that many characters long, for example `xx` is any value from `00` to `99`. Opcodes and Operands are ***never*** negative

| Opcode | Operand | Mnemonic code | Description |
|  :--:  |  :---:  |     :---:     | :---------- |
| *1* | `xx` | **ADD** | Adds the value stored in the memory location `xx` to whatever value is currently stored in the accumulator and stores it there |
| *2* | `xx` | **SUB** | Subtracts the value stored in the memory location `xx` from whatever value is currently stored in the accumulator and stores it there |
| *3* | `xx` | **STA** | Stores the value in the accumulator to the memory location `xx` (destructive) |
| *4* | | | This is an unused code and gives an error |
| *5* | `xx` | **LDA** | Load the value from memory location `xx` (non-destructive) and enter it in the accumulator (destructive) |
| *6* | `xx` | **BRA** | Sets the program counter to the given address `xx` |
| *7* | `xx` | **BRZ** | If the accumulator contains the value 000 then set the program counter to the given address `xx` |
| *8* | `xx` | **BRP** | If the accumulator contains a value between 000 and 999, then set the program counter to the given address `xx` |
| *9* | `01` | **INP** | Get an input from the user and store it in the accumulator. |
| *9* | `02` | **OUT** | Output the value of the accumulator |
| *0* | `00` | **HLT** | Stop working |
| *0* | `01` | **COB** | Stop the program |
