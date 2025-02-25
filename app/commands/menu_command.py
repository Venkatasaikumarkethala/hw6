"""
Command plugin that lists available commands.
"""
from typing import List, Dict, Type
from app.command_interface import CommandInterface

class MenuCommand(CommandInterface):
    """Lists all available commands (plugins)."""

    @property
    def name(self) -> str:
        return "menu"

    def execute(self, args: List[str], commands_dict: Dict[str, Type] = None) -> str:
        """
        Usage: menu
        If commands_dict is provided, we list them;
        otherwise, let the user know no commands are loaded.
        """
        if args:
            raise ValueError("Usage: menu")

        if not commands_dict:
            return "No commands loaded."

        cmd_list = sorted(commands_dict.keys())
        return "Available commands: " + ", ".join(cmd_list)
