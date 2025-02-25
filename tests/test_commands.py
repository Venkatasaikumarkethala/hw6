"""
Tests for individual command plugins using direct calls to their execute() methods.
"""
import pytest
from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubtractCommand
from app.commands.multiply_command import MultiplyCommand
from app.commands.divide_command import DivideCommand
from app.commands.menu_command import MenuCommand




def test_add_command_invalid_numeric():
    with pytest.raises(ValueError) as exc:
        AddCommand().execute(["abc", "2"])  # "abc" triggers decimal.InvalidOperation
    assert "Invalid numeric input" in str(exc.value)

def test_subtract_command_invalid_numeric():
    with pytest.raises(ValueError) as exc:
        SubtractCommand().execute(["xyz", "5"])
    assert "Invalid numeric input" in str(exc.value)

def test_multiply_command_invalid_numeric():
    with pytest.raises(ValueError) as exc:
        MultiplyCommand().execute(["foo", "3"])
    assert "Invalid numeric input" in str(exc.value)



def test_menu_command_no_commands_loaded():
    """Test the 'No commands loaded.' branch in MenuCommand."""
    cmd = MenuCommand()
    output = cmd.execute([])  # Not passing a second arg -> commands_dict defaults to None
    assert output == "No commands loaded."





def test_add_command():
    assert AddCommand().execute(["5", "3"]) == "5 + 3 = 8"

def test_add_command_invalid_args():
    with pytest.raises(ValueError) as exc:
        AddCommand().execute(["5"])
    assert "Usage: add <num1> <num2>" in str(exc.value)

def test_subtract_command():
    assert SubtractCommand().execute(["10", "4"]) == "10 - 4 = 6"

def test_subtract_command_invalid_args():
    with pytest.raises(ValueError) as exc:
        SubtractCommand().execute(["10"])
    assert "Usage: subtract <num1> <num2>" in str(exc.value)

def test_multiply_command():
    assert MultiplyCommand().execute(["4", "5"]) == "4 * 5 = 20"

def test_multiply_command_invalid_args():
    with pytest.raises(ValueError) as exc:
        MultiplyCommand().execute(["4"])
    assert "Usage: multiply <num1> <num2>" in str(exc.value)

def test_divide_command():
    assert DivideCommand().execute(["20", "5"]) == "20 / 5 = 4"

def test_divide_command_by_zero():
    with pytest.raises(ValueError) as exc:
        DivideCommand().execute(["10", "0"])
    assert "Cannot divide by zero" in str(exc.value)

def test_divide_command_invalid_args():
    with pytest.raises(ValueError) as exc:
        DivideCommand().execute(["20"])
    assert "Usage: divide <num1> <num2>" in str(exc.value)

def test_divide_command_invalid_numeric():
    with pytest.raises(ValueError) as exc:
        DivideCommand().execute(["abc", "1"])
    assert "Invalid numeric input" in str(exc.value)

def test_menu_command():
    fake_dict = {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand,
        'menu': MenuCommand
    }
    output = MenuCommand().execute([], fake_dict)
    assert "Available commands:" in output
    assert "add" in output
    assert "subtract" in output
    assert "multiply" in output
    assert "divide" in output
    assert "menu" in output

def test_menu_command_invalid_args():
    with pytest.raises(ValueError) as exc:
        MenuCommand().execute(["extra"])
    assert "Usage: menu" in str(exc.value)
