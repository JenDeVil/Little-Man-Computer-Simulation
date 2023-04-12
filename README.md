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


