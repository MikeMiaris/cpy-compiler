# cpy-compiler

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![RISC-V](https://img.shields.io/badge/Target-RISC--V-green)](https://riscv.org/)

**cpy-compiler** is a complete compiler for the **cpy** language, a small, educational programming language developed for the "Compilers" course at the University of Ioannina. It translates `.cpy` source files directly into **RISC-V assembly**, suitable for execution on simulators like RARS or actual hardware.

---

## Features

- **Full Compilation Pipeline** – From source `.cpy` to executable `.asm` code.
- **Nested Scopes** – Full support for lexical scoping (static PASCAL-style) with correct handling of non‑local variables.
- **Rich Feature Set** – Implements `if`‑`elif`‑`else`, `while` loops, integer operations (including `//` division), boolean logic (`and`, `or`, `not`), and standard I/O.
- **Robust Error Checking** – Performs lexical, syntactic, and semantic analysis, catching invalid characters, undeclared identifiers, type mismatches, and function argument count errors.
- **Human‑Readable Output** – Generates clean, well‑documented intermediate `.int` (quadruples) and symbol table `.sym` files for debugging.

---

##  Getting Started

### Prerequisites

- **Python 3.8+**
- A **RISC-V Simulator**: [RARS](https://github.com/TheThirdOne/rars) (recommended) or a GCC toolchain with QEMU.

### Installation & Usage

1. **Clone the repository**  
   ```bash
   git clone https://github.com/MikeMiaris/cpy-compiler.git
   cd cpy-compiler

2. **Run the compiler on a valid .cpy source file**

bash
python src/cpy_4735_4645.py tests/test.cpy
This generates three files:

test.asm – final RISC‑V assembly output

test.int – listing of the intermediate quadruples

test.sym – dump of the symbol tables for each lexical scope

3. **Execute the assembly (using RARS)**

Open test.asm in the RARS application

Click Assemble

Click Run or Execute

## Language Quick Reference (cpy)
Variables – Must be declared with #int.

Global variables – Declared at the top level, then accessed inside functions via the global keyword.

Functions – Defined with def name(params):. A function’s body is enclosed within #{ ... #}.

Input / Output – x = int(input()) and print(expression).

Comments – Enclosed within ## (e.g., ## This is a comment ##).

## Authors

- **Michalis Miaris**
- **Ilias Georgiadis**

## Acknowledgements

Developed as a term project for the **Compilers** course (Spring 2024) at the Department of Computer Science & Engineering, University of Ioannina.  
Instructor: Prof. G. Manis.
