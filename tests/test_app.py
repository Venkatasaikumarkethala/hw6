import pytest
from app import App

def test_environment_loaded():
    """Verify that environment variables are loaded into app.env_name."""
    app = App()  # Instantiate
    # Since .env has ENV_NAME="local-development", check that
    assert app.env_name == "local-development"


def test_app_successful_add_repl(capfd, monkeypatch):
    """Test a successful command in the REPL that returns a normal string result."""
    app = App()  # Instantiate
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()  # Call instance method

    out, _ = capfd.readouterr()
    # Because "add 5 3" was successful, output is "5 + 3 = 8"
    assert "5 + 3 = 8" in out
    assert "Exiting the interactive calculator..." in out


def test_app_command_returns_none(capfd, monkeypatch):
    """Force a command to return None and ensure REPL doesn't print a result."""
    def returns_none(*args, **kwargs):
        return None

    from app.commands.add_command import AddCommand
    monkeypatch.setattr(AddCommand, "execute", returns_none)

    app = App()
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()

    out, _ = capfd.readouterr()
    assert "5 + 3 = 8" not in out  # There's no result printed
    assert "Welcome to the Interactive Calculator!" in out
    assert "Exiting the interactive calculator..." in out


def test_app_value_error_invalid_numeric_repl(capfd, monkeypatch):
    """Test an invalid numeric input scenario in the REPL."""
    app = App()
    inputs = iter(['add abc 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()

    out, _ = capfd.readouterr()
    assert "Error: Invalid numeric input for add command." in out


def test_app_value_error_add_args_repl(capfd, monkeypatch):
    """Trigger ValueError by typing 'add 5' with only one operand."""
    app = App()
    inputs = iter(['add 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()

    out, _ = capfd.readouterr()
    assert "Error: Usage: add <num1> <num2>" in out


def test_app_value_error_divide_by_zero_repl(capfd, monkeypatch):
    """Trigger a 'Cannot divide by zero' ValueError in the REPL."""
    app = App()
    inputs = iter(['divide 5 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()

    out, _ = capfd.readouterr()
    assert "Error: Cannot divide by zero." in out


def test_app_unexpected_exception(capfd, monkeypatch):
    """Force a non-ValueError exception to cover the 'Unexpected error' branch."""
    def raise_unexpected(*_, **__):
        raise ZeroDivisionError("Fake error")

    from app.commands.add_command import AddCommand
    monkeypatch.setattr(AddCommand, "execute", raise_unexpected)

    app = App()
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()

    out, _ = capfd.readouterr()
    assert "Unexpected error: Fake error" in out


def test_app_start_exit(capfd, monkeypatch):
    """Test that typing 'exit' correctly exits the REPL."""
    app = App()
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app.start()

    out, _ = capfd.readouterr()
    assert "Welcome to the Interactive Calculator!" in out
    assert "Exiting the interactive calculator..." in out


def test_app_blank_input(capfd, monkeypatch):
    """Test that an empty input does not crash and simply continues the loop."""
    app = App()
    inputs = iter(['', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()

    out, _ = capfd.readouterr()
    assert "Welcome to the Interactive Calculator!" in out
    assert "Exiting the interactive calculator..." in out


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command."""
    app = App()
    inputs = iter(['unknown_cmd', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()

    out, _ = capfd.readouterr()
    assert "Unknown command." in out
    assert "Exiting the interactive calculator..." in out
