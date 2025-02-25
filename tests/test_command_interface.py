import pytest
from app.command_interface import CommandInterface

def test_command_interface_cannot_instantiate():
    """Trying to instantiate CommandInterface should fail because it's abstract."""
    with pytest.raises(TypeError) as exc:
        CommandInterface()
    assert "abstract" in str(exc.value)