"""
Defines the Command interface for the command pattern.
"""

from abc import ABC, abstractmethod
from typing import List

class CommandInterface(ABC):
    """Abstract base class for commands."""

    @property
    @abstractmethod
    def name(self) -> str: # pragma: no cover
        """Command name (e.g., 'add')"""
        raise NotImplementedError

    @abstractmethod
    def execute(self, args: List[str]) -> str: # pragma: no cover
        """
        Execute the command with the given arguments.
        Returns a string message or result to print.
        """
        raise NotImplementedError
