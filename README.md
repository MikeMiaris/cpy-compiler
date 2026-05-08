# cpy-compiler

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![RISC-V](https://img.shields.io/badge/Target-RISC--V-green)](https://riscv.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](/LICENSE)

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
