**RISC-V Instruction Set Architecture (ISA) Implementation for RARS Simulation**

This project provides a detailed implementation of the RISC-V ISA, designed to seamlessly integrate with the RARS simulator. By accurately emulating RISC-V instructions, this library enables you to execute and analyze RISC-V assembly programs within a familiar environment.

**Key Features**

* **Comprehensive Instruction Coverage:**  Supports a wide range of RISC-V instructions, including arithmetic (ADD, SUB, etc.), logical (AND, OR, XOR), memory (LB, LW, SB, SW), control flow (BEQ, BNE, JAL, JALR), and system calls (ECALL).
* **Register & Memory Emulation:** Faithfully replicates RISC-V register behavior and memory interactions, ensuring accurate execution results.

**How to Use**

1. **Import:**  Include the `Memoria.py` (if used) and `instrucao.py` files into your RARS project. Ensure you have `code.bin` (instructions) and `data.bin` (data) files exported from RARS in the same directory as your main Python script.
2. **Initialization:** Load instruction and data memory:
   ```python
   import Memoria as mem

   mem.carregarCodigo() 
   mem.carregarData() 
   ```
3. **Execute Instructions:**
   ```python
   import Registradores as reg
   
   reg.run()  
   ```

**Example Usage**

```python
import Memoria as mem  # If you have a separate memory module
import instrucao as inst
import Registradores as reg  # Assuming you have a module to handle register execution

# 1. Load instructions and data from RARS exports (code.bin, data.bin)
mem.carregarCodigo()
mem.carregarData()

# 2. Initialize and run the simulator
reg.run() 

# The simulator will now execute your RISC-V assembly program
```



**Why This Project is Valuable**

* **Learning Resource:** Gain a deeper understanding of RISC-V architecture, assembly language programming, and computer architecture principles.
* **Testing & Debugging:**  Thoroughly test and debug your RISC-V assembly programs within RARS before deploying to real hardware.
* **Customization:** Adapt and extend the implementation to explore variations of the RISC-V ISA or support additional instructions.

**Demonstrated Skills**

* **Computer Architecture:** Deep understanding of RISC-V architecture, instruction formats, and execution pipeline.
* **Assembly Language:**  Proficiency in writing and analyzing RISC-V assembly code.
* **Python:** Expertise in Python for implementing the ISA logic and data structures.
* **Software Engineering:**  Excellent coding practices, attention to detail, and ability to create well-structured, maintainable code.


