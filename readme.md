# Homework 5: Command Pattern & Plugins

In this assignment, we transform a single-run calculator script into a **continuously running application** with a **Command Pattern** and **Plugin Architecture**. We also achieve **100% test coverage** through comprehensive unit and functional tests.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Key Features](#key-features)  
3. [Directory Structure](#directory-structure)  
4. [Installation & Setup](#installation--setup)  
5. [How to Run](#how-to-run)  
6. [Commands & Usage](#commands--usage)  
7. [Testing & Coverage](#testing--coverage)  
8. [Design & Architecture](#design--architecture)  
9. [References & Additional Info](#references--additional-info)

---

## Project Overview

This project builds on a basic calculator (from Homework 4) and adds:

- A **REPL (Read-Eval-Print Loop)** to continuously accept user commands.  
- A **Command Pattern** design, allowing each calculator operation to be a separate “command” class.  
- A **Plugin Architecture** that dynamically discovers and loads commands from a `commands` directory.  
- **Exception handling** for various error cases (e.g., invalid input, zero-division).  
- **Comprehensive tests** that provide near- or exactly **100%** coverage using `pytest` and `pytest-cov`.

---

## Key Features

1. **Command Pattern**  
   - Each operation (add, subtract, multiply, etc.) is in its own class implementing a shared interface (`CommandInterface`).

2. **Plugin Manager**  
   - Dynamically loads any command plugin placed in the `app/commands/` folder.  
   - Makes adding new commands (e.g., power, root) as simple as creating a new file with a command class.

3. **Interactive REPL**  
   - Runs continuously, prompting the user to enter commands.  
   - Handles errors gracefully (e.g., unknown command, invalid input) without crashing.  

4. **Tests & 100% Coverage**  
   - Unit tests for each command.  
   - Integration tests for the REPL flow (via `capfd`, `monkeypatch`).  
   - Achieves **100%** coverage after thorough testing of success paths, error paths, and edge cases.

---

## Directory Structure

A typical layout:

```
calc_design_patterns/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── app/
│   ├── __init__.py            # Contains the main REPL (App.start)
│   ├── plugin_manager.py      # Dynamically loads command plugins
│   ├── command_interface.py   # Abstract base for all commands
│   └── commands/
│       ├── __init__.py
│       ├── add_command.py
│       ├── subtract_command.py
│       ├── multiply_command.py
│       ├── divide_command.py
│       └── menu_command.py
├── tests/
│   ├── test_app.py
│   ├── test_command_interface.py
│   ├── test_commands.py
│   └── conftest.py
├── main.py
├── pytest.ini
├── requirements.txt
├── .coveragerc
├── .pylintrc
└── readme.md
```

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone url
   cd calc_design_patterns
   ```

2. **Create & Activate a virtual environment**:
   ```bash
   python -m venv hw5
   source hw5/bin/activate       # Mac/Linux
   hw5\Scripts\activate          # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

From the project root directory:

```bash
python main.py
```

You’ll see:

```
Welcome to the Interactive Calculator!
Type 'menu' to see available commands or 'exit' to quit.
>>>
```

Enter commands (e.g., `add 5 3`), or type `exit` to terminate.

---

## Commands & Usage

Here are the built-in commands:

1. **add**  
   - **Usage**: `add <num1> <num2>`  
   - **Example**: `add 5 3` → `5 + 3 = 8`

2. **subtract**  
   - **Usage**: `subtract <num1> <num2>`  
   - **Example**: `subtract 8 2` → `8 - 2 = 6`

3. **multiply**  
   - **Usage**: `multiply <num1> <num2>`  
   - **Example**: `multiply 4 5` → `4 * 5 = 20`

4. **divide**  
   - **Usage**: `divide <num1> <num2>`  
   - **Example**: `divide 20 4` → `20 / 4 = 5`

5. **menu** (Bonus)  
   - Lists all available commands.  
   - **Usage**: `menu`

6. **exit**  
   - Exits the REPL.

**Error cases**:
- **Divide by zero** → `Error: Cannot divide by zero.`  
- **Invalid numeric input** → `Error: Invalid numeric input for ___ command.`  
- **Unknown command** → `Unknown command. Type 'menu' to see available commands, or 'exit' to quit.`  
- **Wrong number of arguments** → `Error: Usage: <command> <num1> <num2>`

---

## Testing & Coverage

1. **Run all tests**:
   ```bash
   pytest
   ```
   This discovers and runs tests in the `tests/` folder.

2. **Run coverage**:
   ```bash
   pytest --cov=app --cov-report=term-missing
   ```
   Displays which lines are covered or missing coverage.  
   Expected result:
   ```
   ---------- coverage: ...
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
app/__init__.py                       29      0   100%
app/command_interface.py               6      0   100%
app/commands/__init__.py               6      0   100%
app/commands/add_command.py           17      0   100%
app/commands/divide_command.py        19      0   100%
app/commands/menu_command.py          13      0   100%
app/commands/multiply_command.py      17      0   100%
app/commands/subtract_command.py      17      0   100%
app/plugin_manager.py                 18      0   100%
----------------------------------------------------------------
TOTAL                                142      0   100%
   ```

3. **Test files**:
   - **`test_app.py`** → REPL-level tests (monkeypatched user inputs).
   - **`test_commands.py`** → Command class tests (AddCommand, etc.).
   - **`test_command_interface.py`** → Ensures the abstract base class can’t be instantiated.

---

## Design & Architecture

1. **Command Pattern**  
   - Each calculator operation is a class implementing `CommandInterface`.  
   - The REPL queries a `commands_dict` for a matching command name, instantiates it, and calls `.execute()`.

2. **Plugin Architecture**  
   - `PluginManager` scans `app/commands/` submodules.  
   - Any new `.py` file that defines a `CommandInterface` subclass is automatically discovered.

3. **REPL**  
   - Continuously reads user input, splits into `<command> <args>`.  
   - If valid, calls the appropriate command; otherwise shows an error.  
   - Exceptions from commands are caught and printed gracefully.

4. **Exception Handling**  
   - `ValueError` for known invalid conditions (e.g., “Usage,” “Cannot divide by zero,” “Invalid numeric input”).  
   - `Exception` catch-all to handle truly unexpected errors with `Unexpected error: ...`.

---

## References & Additional Info

- **Pytest**: [https://docs.pytest.org/](https://docs.pytest.org/)  
- **Pytest-Cov**: [https://pytest-cov.readthedocs.io/](https://pytest-cov.readthedocs.io/)  
- **Faker** (optional) for generating test data: [https://faker.readthedocs.io/](https://faker.readthedocs.io/)  
- **Design Patterns**: [Gamma et al., *Design Patterns* (1994)](https://en.wikipedia.org/wiki/Design_Patterns)  
- **GIL & Multiprocessing** (bonus lecture): [YouTube Video](https://www.youtube.com/watch?v=m4zDBk0zAUY)
