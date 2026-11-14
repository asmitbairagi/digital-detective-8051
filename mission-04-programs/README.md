# Mission 4 — How Programs Run

## 1. Objective
To understand how programs are executed, the difference between compilers and interpreters, and how Python runs source code.

## 2. Source Code and Machine Code
- Source code consists of human-readable instructions written by programmers in programming languages.
- Machine code consists of binary instructions that a processor can execute directly.

## 3. Compiler vs Interpreter

**Compiler:**
A compiler translates source code into another form, often machine code or an executable, before execution.

Examples: C and C++.

**Interpreter:**
An interpreter executes a program through a runtime environment.

Example: Python.

Python is commonly called an interpreted language, although standard CPython also uses compilation.

## 4. How Python Executes a Program

In standard CPython:

1. Python reads the source code.
2. The CPython compiler converts it into bytecode.
3. The Python Virtual Machine (PVM) executes the bytecode.
4. The runtime uses native machine instructions executed by the CPU.

## 5. Practical Work

Created the file:

`mission-04-programs/hello.py`

Program:

```python
name = "Digital Detective"

print("Hello from Python")
print(name)
print(2 + 3)
```

Expected output:

```text
Hello from Python
Digital Detective
5
```

Execution command:

```bash
python3 hello.py
```

## 6. Concepts Learned
- Source code is human-readable.
- Bytecode is an intermediate representation.
- The PVM executes Python bytecode.
- The CPU executes native machine instructions.
- Python uses both compilation and interpretation in standard CPython.

## 7. Difficulties and Learning
Initially, I thought Python only interprets code and does not compile it. I learned that CPython first compiles source code into bytecode, which is then executed by the Python Virtual Machine.

I also learned to predict program output before running the code.

## 8. Evidence and Files
- `hello.py` — Python program created and executed during this mission.
- This README — documentation of concepts and practical work.

## 9. Commit Details
To be updated after committing and pushing this mission to GitHub.