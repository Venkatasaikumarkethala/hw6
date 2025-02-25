"""
Command plugin for subtraction.
"""
from decimal import Decimal, InvalidOperation
from typing import List, Dict, Type
from app.command_interface import CommandInterface

class SubtractCommand(CommandInterface):
    """Performs subtraction of two numbers."""

    @property
    def name(self) -> str:
        return "subtract"

    def execute(self, args: List[str], commands_dict: Dict[str, Type] = None) -> str:
        """
        Usage: subtract <num1> <num2>
        """
        if len(args) != 2:
            raise ValueError("Usage: subtract <num1> <num2>")

        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            result = num1 - num2
            return f"{num1} - {num2} = {result}"
        except InvalidOperation:
            raise ValueError("Invalid numeric input for subtract command.")
