# Homework 5: Command Pattern & Plugins

In this assignment, we transform a single-run calculator script into a **continuously running application** with a **Command Pattern** and **Plugin Architecture**. We also achieve **100% test coverage** through comprehensive unit and functional tests.

---

## 📌 Table of Contents

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

## 🔍 Project Overview

This project builds on a basic calculator (from Homework 4) and adds:

- A **REPL (Read-Eval-Print Loop)** to continuously accept user commands.  
- A **Command Pattern** design, allowing each calculator operation to be a separate "command" class.  
- A **Plugin Architecture** that dynamically discovers and loads commands from a `commands` directory.  
- **Exception handling** for various error cases (e.g., invalid input, zero-division).  
- **Comprehensive tests** that provide **100% test coverage** using `pytest` and `pytest-cov`.  

---

## ⭐ Key Features

### 🔹 **Command Pattern**
- Each operation (`add`, `subtract`, `multiply`, etc.) is in its own class implementing a shared interface (`CommandInterface`).

### 🔹 **Plugin Manager**
- Dynamically loads any command plugin placed in the `app/commands/` folder.  
- Adding new commands (e.g., `power`, `root`) is as simple as creating a new file with a command class.

### 🔹 **Interactive REPL**
- Runs continuously, prompting the user to enter commands.
- Handles errors gracefully (e.g., unknown command, invalid input) without crashing.  

### 🔹 **Tests & 100% Coverage**
- Unit tests for each command.  
- Integration tests for the REPL flow (via `capfd`, `monkeypatch`).  
- Achieves **100%** coverage by thoroughly testing success paths, error paths, and edge cases.  

---

## 📂 Directory Structure

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

## ⚙️ Installation & Setup

### 1️⃣ **Clone the repository**:
```bash
git clone https://github.com/Venkatasaikumarkethala/homework5
cd homework5
```

### 2️⃣ **Create & Activate a virtual environment**:
```bash
python -m venv hw5
source hw5/bin/activate   # Mac/Linux
hw5\Scripts\activate     # Windows
```

### 3️⃣ **Install dependencies**:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

From the project root directory:
```bash
python main.py
```

You'll see:
```
Welcome to the Interactive Calculator!
Type 'menu' to see available commands or 'exit' to quit.
>>>
```

Enter commands (e.g., `add 5 3`), or type `exit` to terminate.

---

## 🔢 Commands & Usage

### 📌 Built-in Commands

| Command   | Usage                  | Example           |
|-----------|------------------------|-------------------|
| **add**   | `add <num1> <num2>`    | `add 5 3` → `8`  |
| **subtract** | `subtract <num1> <num2>` | `subtract 8 2` → `6` |
| **multiply** | `multiply <num1> <num2>` | `multiply 4 5` → `20` |
| **divide** | `divide <num1> <num2>` | `divide 20 4` → `5` |
| **menu**  | Lists all available commands. | `menu` |
| **exit**  | Exits the REPL. | `exit` |

### ⚠️ **Error Cases**
- **Divide by zero** → `Error: Cannot divide by zero.`
- **Invalid numeric input** → `Error: Invalid numeric input for ___ command.`
- **Unknown command** → `Unknown command. Type 'menu' to see available commands, or 'exit' to quit.`
- **Wrong number of arguments** → `Error: Usage: <command> <num1> <num2>`

---

## ✅ Testing & Coverage

### 1️⃣ **Run all tests**:
```bash
pytest
```

### 2️⃣ **Run coverage**:
```bash
pytest --cov=app --cov-report=term-missing
```

#### ✅ Expected Result:
```
collected 26 items                                                                     

tests/test_app.py::test_app_successful_add_repl PASSED                           [  3%]
tests/test_app.py::test_app_command_returns_none PASSED                          [  7%]
tests/test_app.py::test_app_value_error_invalid_numeric_repl PASSED              [ 11%]
tests/test_app.py::test_app_value_error_add_args_repl PASSED                     [ 15%]
tests/test_app.py::test_app_value_error_divide_by_zero_repl PASSED               [ 19%]
tests/test_app.py::test_app_unexpected_exception PASSED                          [ 23%]
tests/test_app.py::test_app_start_exit PASSED                                    [ 26%]
tests/test_app.py::test_app_blank_input PASSED                                   [ 30%]
tests/test_app.py::test_app_start_unknown_command PASSED                         [ 34%]
tests/test_command_interface.py::test_command_interface_cannot_instantiate PASSED [ 38%]
tests/test_commands.py::test_add_command_invalid_numeric PASSED                  [ 42%]
tests/test_commands.py::test_subtract_command_invalid_numeric PASSED             [ 46%]
tests/test_commands.py::test_multiply_command_invalid_numeric PASSED             [ 50%]
tests/test_commands.py::test_menu_command_no_commands_loaded PASSED              [ 53%]
tests/test_commands.py::test_add_command PASSED                                  [ 57%]
tests/test_commands.py::test_add_command_invalid_args PASSED                     [ 61%]
tests/test_commands.py::test_subtract_command PASSED                             [ 65%]
tests/test_commands.py::test_subtract_command_invalid_args PASSED                [ 69%]
tests/test_commands.py::test_multiply_command PASSED                             [ 73%]
tests/test_commands.py::test_multiply_command_invalid_args PASSED                [ 76%]
tests/test_commands.py::test_divide_command PASSED                               [ 80%]
tests/test_commands.py::test_divide_command_by_zero PASSED                       [ 84%]
tests/test_commands.py::test_divide_command_invalid_args PASSED                  [ 88%]
tests/test_commands.py::test_divide_command_invalid_numeric PASSED               [ 92%]
tests/test_commands.py::test_menu_command PASSED                                 [ 96%]
tests/test_commands.py::test_menu_command_invalid_args PASSED                    [100%]

---------- coverage: platform darwin, python 3.11.7-final-0 ----------
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


================================== 26 passed in 0.10s ==================================
```

### 3️⃣ **Test Files**
- `test_app.py` → REPL-level tests (monkeypatched user inputs).
- `test_commands.py` → Command class tests (`AddCommand`, etc.).
- `test_command_interface.py` → Ensures the abstract base class can’t be instantiated.

---

## 🎨 Design & Architecture

- **Command Pattern** → Each calculator operation is a class implementing `CommandInterface`.
- **Plugin Architecture** → `PluginManager` scans `app/commands/` submodules for new commands.
- **REPL** → Continuously reads user input and executes the appropriate command.
- **Exception Handling** → Handles errors gracefully.

---

## 📚 References & Additional Info

- **[Pytest Docs](https://docs.pytest.org/)**  
- **[Pytest-Cov](https://pytest-cov.readthedocs.io/)**  
- **[Design Patterns - Gamma et al.](https://en.wikipedia.org/wiki/Design_Patterns)**  
