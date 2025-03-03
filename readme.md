# Homework 6: Getting Ready for Production

This project builds on **Homework 5** by adding:

1. **GitHub Actions** for Continuous Integration (CI).  
2. **Environment Variables** stored in a `.env` file for local development.  
3. **Logging** to track application events and errors.

## Table of Contents

1. [Introduction & Requirements](#introduction--requirements)  
2. [Features Added in HW6](#features-added-in-hw6)  
3. [Directory Structure](#directory-structure)  
4. [Setup Instructions](#setup-instructions)  
5. [Usage](#usage)  
6. [Environment Variables](#environment-variables)  
7. [Logging](#logging)  
8. [Continuous Integration (GitHub Actions)](#continuous-integration-github-actions)  
9. [Testing & Coverage](#testing--coverage)  
10. [Conclusions](#conclusions)

---

## 1. Introduction & Requirements

**Goal**: Transform a previously built interactive calculator into a more **production-ready** application. We achieve this by:

1. **Storing configuration** (like environment name) in `.env`, **never** committing it to Git.  
2. **Logging** events and errors to trace the program’s operation.  
3. **Running automated tests** on GitHub automatically for every push, ensuring stable code.

### Prerequisites

- Python 3.10+  
- Understanding of Git, GitHub, and Pytest.

---

## 2. Features Added in HW6

1. **GitHub Actions**: Every push to `main` triggers the workflow in `.github/workflows/python-app.yml`, installing dependencies and running `pytest`.  
2. **Environment Variables**: The file `.env` (excluded from Git via `.gitignore`) sets local dev environment variables (e.g., `ENV_NAME="local-development"`). On GitHub, the same variable is set in the Actions workflow for consistency.  
3. **Logging**: A `logging.conf` file or `logging.basicConfig()` configures logging. We log at levels **INFO**, **WARNING**, **ERROR**, and **EXCEPTION**.

---

## 3. Directory Structure

Below is an abbreviated layout:

```
calc_design_patterns/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── app/
│   ├── __init__.py          # Main application (logging, env loading, REPL)
│   ├── plugin_manager.py    # Dynamically loads commands
│   └── commands/
│       ├── add_command.py
│       ├── divide_command.py
│       ├── menu_command.py
│       ├── multiply_command.py
│       ├── subtract_command.py
│       └── __init__.py
├── tests/
│   ├── test_app.py          # Integration tests for the REPL
│   ├── test_commands.py     # Unit tests for each command
│   ├── test_command_interface.py
│   └── conftest.py
├── main.py                  # Entry point calling `App()`
├── logging.conf             # Optional logging config
├── .env                     # Local dev environment variables (not committed)
├── .gitignore
├── requirements.txt
├── pytest.ini
└── readme.md
```

**Note**: `.env` is **ignored** by Git, so it won’t appear on GitHub.

---

## 4. Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Venkatasaikumarkethala/hw6
   cd hw6
   ```
2. **Create & activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 5. Usage

1. **Add a local `.env` file** for environment variables (see below).  
2. **Run**:
   ```bash
   python main.py
   ```
3. 
   ```
   Welcome to the Interactive Calculator!
   Type 'menu' to see available commands or 'exit' to quit.
   >>>
   ```
4. Example commands:
   - `menu` → `Available commands: add, divide, menu, multiply, subtract`
   - `add 5 6` → `5 + 6 = 11`
   - `divide 5 0` → `Error: Cannot divide by zero.`
   - `unknowncmd 1 2` → `Unknown command. Type 'menu'...`
   - `exit` → Exits the program.

---

## 6. Environment Variables

- Create a **`.env`** file in the project root (not committed).  
- Example:
  ```bash
  ENV_NAME="local-development"
  LOG_LEVEL="INFO"
  ```
- The app code in `app/__init__.py` loads `.env` via `python-dotenv` and sets:
  ```python
  load_dotenv()
  self.env_name = os.getenv("ENV_NAME", "unknown")
  ```
- The test `test_app.py::test_environment_loaded` ensures the environment variable is recognized.  
- On GitHub, the `ENV_NAME` is set in `.github/workflows/python-app.yml` under `env:` so that test doesn’t fail.

---

## 7. Logging

- **Default** logs go to the console.  
- If `logging.conf` exists, a rotating file handler writes logs to `logs/app.log`.
- Example logs:
  ```
  2025-03-03 21:12:38,972 - root - INFO - Environment: local-development
  2025-03-03 21:12:38,972 - root - INFO - Plugin commands loaded.
  2025-03-03 21:12:38,972 - root - WARNING - Unknown command: dicide
  2025-03-03 21:12:56,212 - root - ERROR - ValueError in command 'add': Usage: add <num1> <num2>
  ```

---

## 8. Continuous Integration (GitHub Actions)

- `.github/workflows/python-app.yml` defines a **CI pipeline**:
  ```yaml
  name: Python application
  on:
    push:
      branches: [ "main" ]
    pull_request:
      branches: [ "main" ]
  env:
    ENV_NAME: local-development
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.10
          uses: actions/setup-python@v3
          with:
            python-version: "3.10"
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        - name: Test with pytest --pylint
          run: |
            pytest
  ```
- Whenever changes are pushed to `main`, GitHub installs dependencies and runs tests.  
- We set `ENV_NAME: local-development` so the environment test passes.

---

## 9. Testing & Coverage

- **Run tests locally**:
  ```bash
  pytest --cov=app --cov-report=term-missing
  ```
- **Sample output**:
  ```
  =========================== test session starts ============================
  collected 27 items
  
  tests/test_app.py::test_environment_loaded PASSED
  ...
  ---------- coverage: platform darwin, python 3.11 ----------
  Name                Stmts   Miss  Cover
  ---------------------------------------
  app/__init__.py        50      0   100%
  ...
  TOTAL                163      0   100%
  ```
- On GitHub, check the “Actions” tab to see a similar log. A green check mark indicates all tests passed.

---

## 10. Conclusions

With this Homework 6 submission, we have:

- **Automatic CI** with GitHub Actions, verifying code on every commit.  
- **Environment Variables** for local dev vs. production configuration.  
- **Logging** for diagnostics, debugging, and future data insights.  
- Maintained **100% coverage** from HW5 while adding DevOps features.