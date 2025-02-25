"""
Plugin Manager for dynamically loading commands from the commands directory.
"""
import importlib
import pkgutil
import sys
from typing import Dict, Type
from .command_interface import CommandInterface
from . import commands  # The parent module that contains all plugin modules

class PluginManager:
    """Loads and stores command plugins dynamically from the commands package."""

    @staticmethod
    def load_plugins() -> Dict[str, Type[CommandInterface]]:
        """
        Dynamically imports all modules in the 'commands' package
        and returns a dictionary {command_name: command_class}.
        """
        plugin_dict = {}

        # Iterate through all modules in the commands package
        package_path = commands.__path__
        for _, module_name, _ in pkgutil.iter_modules(package_path):
            full_module_name = f"{commands.__name__}.{module_name}"
            # Import the module
            importlib.import_module(full_module_name)

        # Inspect all loaded modules in commands.__dict__ to find CommandInterface subclasses
        for _, obj in commands.__dict__.items():
            if isinstance(obj, type) and issubclass(obj, CommandInterface) and obj is not CommandInterface:
                # obj is a valid command class, store it with its name as the key
                plugin_dict[obj().name.lower()] = obj

        return plugin_dict
