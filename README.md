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



## Code Cleanup Suggestions

The code is fundamentally sound. The following improvements are recommended for better maintainability:

1. **Centralise global state** – Encapsulate `line`, `quad_id`, `temp_counter`, `param_count`, `retflag`, `f_check`, `fp_count`, and `quad_list` in a `CompilerState` class.

2. **Consolidate table management** – Let the `scope` class own the offset counter and the stack; use `symbol_table` only as the main interface for searching.

3. **Optimise the lexer** – Replace `file.seek(-1, 1)` with a lookahead queue (e.g. `collections.deque`) to avoid brittle backtracking.

4. **Create quad helper functions** – Add `new_label()` and `emit_jump(label)` to improve readability when generating control flow.

5. **Refactor `quadconverter`** – Split the large if/else chain into small helper methods like `_gen_add()`, `_gen_param()`, etc.

6. **Use caching** – Decorate `is_not_integer()` with `@lru_cache(maxsize=None)` for repeated checks.

7. **Standardise string literals** – Prefer double quotes (`"..."`) consistently.

## Authors

- **Michalis Miaris**
- **Ilias Georgiadis**

## Acknowledgements

Developed as a term project for the **Compilers** course (Spring 2024) at the Department of Computer Science & Engineering, University of Ioannina.  
Instructor: Prof. G. Manis.
