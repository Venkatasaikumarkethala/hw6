import pytest
from app import App

def test_app_successful_add_repl(capfd, monkeypatch):
    """
    Test a successful command in the REPL 
    that returns a normal string result (no exception, not None).
    """
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()

    # Because "add 5 3" was successful, output is "5 + 3 = 8"
    # The REPL prints that string, which covers line 37 
    # (the 'print(output)' inside 'if output is not None').
    assert "5 + 3 = 8" in out
    assert "Exiting the interactive calculator..." in out




def test_app_command_returns_none(capfd, monkeypatch):

    def returns_none(*args, **kwargs):
        return None

    from app.commands.add_command import AddCommand
    monkeypatch.setattr(AddCommand, "execute", returns_none)

    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    App.start()
    out, _ = capfd.readouterr()
    # Because execute() returned None, 
    # the REPL does NOT print a result. 
    # This ensures we also cover the scenario "if output is not None" = False.
    # 
    # There's no direct assertion needed unless you want to verify 
    # that "5 + 3 = 8" is NOT in `out`. 
    # The key is hitting lines 36-37 in coverage.
    assert "5 + 3 = 8" not in out  # Optional check
    # We do expect the welcome and "Exiting..." lines though
    assert "Welcome to the Interactive Calculator!" in out
    assert "Exiting the interactive calculator..." in out




def test_app_value_error_invalid_numeric_repl(capfd, monkeypatch):
    """
    Test an invalid numeric input scenario in the REPL.
    Forces the command to raise a ValueError for 'Invalid numeric input'
    and checks if the REPL prints "Error: <message>".
    """
    inputs = iter(['add abc 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()

    # The "add" command sees "abc" -> raises ValueError("Invalid numeric input for add command.")
    # REPL catches it -> prints "Error: Invalid numeric input for add command."
    assert "Error: Invalid numeric input for add command." in out




def test_app_value_error_add_args_repl(capfd, monkeypatch):
    """
    Trigger ValueError in the REPL by typing 'add 5' 
    which lacks a second operand, causing the command to raise ValueError.
    """
    inputs = iter(['add 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    # The command will raise ValueError("Usage: add <num1> <num2>"),
    # so the REPL prints "Error: Usage: add <num1> <num2>".
    assert "Error: Usage: add <num1> <num2>" in out

def test_app_value_error_divide_by_zero_repl(capfd, monkeypatch):
    """
    Trigger a 'Cannot divide by zero' ValueError in the REPL 
    by typing 'divide 5 0'.
    """
    inputs = iter(['divide 5 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    # The command raises ValueError("Cannot divide by zero."),
    # so the REPL prints "Error: Cannot divide by zero."
    assert "Error: Cannot divide by zero." in out




def test_app_unexpected_exception(capfd, monkeypatch):
    """Force a non-ValueError exception to cover the 'Unexpected error' branch."""
    def raise_unexpected(*_, **__):
        raise ZeroDivisionError("Fake error")

    from app.commands.add_command import AddCommand
    monkeypatch.setattr(AddCommand, "execute", raise_unexpected)

    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    App.start()
    out, _ = capfd.readouterr()
    assert "Unexpected error: Fake error" in out




def test_app_start_exit(capfd, monkeypatch):
    """Test that typing 'exit' correctly exits the REPL."""
    # Make our mock input function accept the prompt argument
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, _ = capfd.readouterr()
    assert "Welcome to the Interactive Calculator!" in out
    assert "Exiting the interactive calculator..." in out


# tests/test_app.py
def test_app_blank_input(capfd, monkeypatch):
    """Test that an empty input does not crash and simply continues the loop."""
    inputs = iter(['', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Welcome to the Interactive Calculator!" in out
    assert "Exiting the interactive calculator..." in out




def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command."""
    inputs = iter(['unknown_cmd', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Unknown command." in out
    assert "Exiting the interactive calculator..." in out
